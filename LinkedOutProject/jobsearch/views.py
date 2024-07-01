import requests

from bs4 import BeautifulSoup
from urllib.parse import quote

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .importers import unauthed_li_jobs, headers
from .forms import JobStatusForm
from .models import Job, JobSearch


class JobListView(ListView):
    model = Job
    context_object_name = "jobs"

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user, rejected=False) 
    
    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['jobs_list'] = []
        for item in context['jobs']:
            form = JobStatusForm(instance=item)
            context['jobs_list'].append((item, form))
        return context

class JobDetailView(DetailView):
    model = Job

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        
        return context


@login_required
def import_jobs(request):
    """
    Search for jobs matching our parameters and return them.
    """
    user = request.user
    searches = JobSearch.objects.filter(user=request.user)
    for search in searches:
        keywords = "?keywords=" + quote(str(search.keywords))
        location = "&location=" + quote(str(search.location))
        level = "&f_E=" + search.level
        workplace = "&f_WT=" + search.workplace_type
        recency = '&f_TPR=' + search.recency
        url = "https://www.linkedin.com/jobs/search/" + keywords + location + level + workplace + recency
        print("searching for ", search)
        print(url)
        # first let's do a simple (fast) unauthed check
        jobs = unauthed_li_jobs(url)
        # Now if we can, we'll use selenium for a better auth'ed search
        if user.linkedin_username and user.linkedin_password:
            from .importers import authed_li_jobs
            auth_jobs = authed_li_jobs(user, url)
            jobs.update(auth_jobs)    

        print("found jobs:", len(jobs))
        imported = 0
        if jobs:
            for k, vals in jobs.items():
                try:
                    existing_job = Job.objects.get(title=vals['title'], company=vals['company'])
                except Exception:
                    print("importing ", vals['title'])
                    job = Job (
                        title = vals['title'],
                        link = vals['link'],
                        company = vals['company'],
                        location = vals['location'],
                        pub_date = vals['pub_date'],
                        job_id = k,
                        user=user
                    ) 
                    job.save()
                    imported += 1
            print("Imported:", imported)
        return HttpResponseRedirect(reverse('jobs'))


@login_required
def fetch_job_details(request):
    job = get_object_or_404(Job, pk=request.GET['pk'])
    #print(job)
    r = requests.get(job.get_source_url(), headers=headers)
    if r.status_code != 200:
        return HttpResponse("Failed to get good requests response: ", r.status_code)
    print(r.status_code)
    soup = BeautifulSoup(r.content, "html.parser")
    desc = soup.find('div', class_="description__text")
    #print(desc)
    details = soup.find('div', class_="description__text").find("div", class_="show-more-less-html__markup").text.strip()
    job.details = details
    job.save()
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        print("it's ajax")
        return render(request, 'includes/job_detail_td.html')
    return HttpResponseRedirect(reverse('jobs'))


@login_required
def reject_job(request):
    if request.POST:  
        job = get_object_or_404(Job, user=request.user, pk=request.POST['id'])
        job.rejected=True
        job.save()
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return render(request, 'includes/job_detail_row.html')

    return HttpResponseRedirect(reverse('jobs'))

@login_required
def update_job_status(request):
    if request.POST:  
        job = get_object_or_404(Job, user=request.user, pk=request.POST['id'])
        print(request.POST)
        f = JobStatusForm(request.POST, instance=job)
        f.save()
    return HttpResponseRedirect(reverse('jobs'))