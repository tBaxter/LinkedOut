import requests

from bs4 import BeautifulSoup

from flask import Flask, render_template
#from flask_caching import Cache

#from settings import UNSPLASH_API_KEY

app = Flask(__name__)
#app.config['CACHE_TYPE'] = 'simple'  # Choose cache type, e.g., 'simple', 'redis', etc.
#cache = Cache(app)


@app.route("/")
#@cache.cached(timeout=20)  # Cache this view for 60 seconds
def index():
    """
    Search for jobs matching our parameters and return them.
    TO-DO: Capture and store parameters for this search
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    keywords = "director%20of%20software%20engineering"
    location = "Leawood%2C%20Kansas"
    remote = "&f_WT=2"
    hybrid = remote + "%2C3"
    level = "5"
    url = "https://www.linkedin.com/jobs/search/?keywords=" + keywords + "&location=" + location + "&f_E=" + level + remote + hybrid
    print(url)

    r = requests.get(url, headers=headers)
    print(r)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        https://www.linkedin.com/jobs/search/?keywords=director%20of%20software%20engineering&location=Leawood%2C%20Kansas&f_E=5
        
       
    else:
        # we failed to get a good response from linkedin
       
        return "We failed to get a response"


    templateData = {
        'jobs': [],
    }
    return render_template('index.html', **templateData)

@app.route("/about")
def about():
    return render_template('about.html')