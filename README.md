# pleasure_site

Website for the MIT Pleasure group!

## How it works

### So, generally:
1. A user navigates to pleasure.mit.edu/internal/{whatever page}
2. Django looks up that url in the pleasure_internal folder's urls.py, which includes the urls from pleasure_app's urls.py. If the url is there, the way I've defined the urls mean that they all direct to some function in views.py that returns the html for the page that should be displayed.
3. The function in views.py is called. This file queries the database for things like a list of all active educators, events in the next week, etc. It then returns an html file along with all the variables you tell it to (within a dictionary called 'context'). 
4. Django takes the html and variables and serves it using its templating knowledge. 

### Templating
There is a base template for most of the site inside pleasure_app/templates called base_internal.html. This template includes all the relevant css and javascript files, the code for the top navbar and side navbar, and two "content blocks": one for main content, and one for page-specific javascript. 

Each page of the site only defines its own code for those two content blocks; it doesn't have to rewrite the side panel or anything. There are also mini-templates for the trainings, presentations, and events that are included each time one of those needs to be displayed, so that the same code isn't repeated over and over throughout the site. 

### Automated Emails
They are sent. 

## Todos
- Write the above section w/ more detail
- finish dashboard?
- calendar stuff
- see an educator's history of things attended and general stats
- multiple trainings oops
- resources tab (add pubbing email templates)
- figure out booster trainings lol
- show a warning message if people aren't trained to present a module
- fix history breadcrumb
- let people edit how many people came to their event
- backup system!! https://django-dbbackup.readthedocs.io/en/stable/configuration.html
- prettify panels for trainings, presentations, and events (unique color for each?)
- some indicator to show that people's trainings are in the future? or don't show
- extend module 1-week email reminders to 1-day, and also add for trainings
- handle stuff happening today better (on dashboard)
- automate whose pic is on the homepage
- lol don't let the same person sign up multiple times for same event
