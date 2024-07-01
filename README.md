# LinkedOut
An attempt at wrangling LinkedIn Job Search into something that works for me, since right now none of the search sites really work for me, and I distrust their data collection and storage. I make no promises this will work even remotely for anyone but me.

### Initial thoughts
- Leaning toward a simple Django app with a sqlite DB, most likely running locally. Considered Flask, but I think there will be enough going on that Django makes a better choice.
- Search to bring more matching jobs to me, not just the promoted ones.
- abilty to store multiple search terms/parameters
- ability to say "Never show me this job again"
- Note applied-for jobs ... maybe other notes

### Farther down the road
- storage of resume(s)
- dynamic application?
- textual analysis of job posts
- dynamic resume building?
- searching dditional job sources


## Getting started:
- Activate pipenv: `pipenv shell`
- Install requirements, if needed.
- Start Flask `flask run`
