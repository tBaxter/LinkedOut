from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from jobsearch.views import JobListView, JobDetailView, import_jobs, reject_job, fetch_job_details, update_job_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', JobListView.as_view(), name='jobs'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),

    path('fetch-details/', fetch_job_details, name="fetch_job"),
    path('import-jobs/', import_jobs, name="import_jobs"),

    path('reject-job/', reject_job, name="reject_job"),
    path('update-job-status/', update_job_status, name="update_job_status"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
