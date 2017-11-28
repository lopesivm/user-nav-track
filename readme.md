# UNT - User Navigation Tracking

Is composed of a server and a javascript plugin used to track user navigation on your own pages. UNT provides you with
an administrative interface to quickly visualize the tracking log of registered users.

This project can be seen running it's server live at [Heroku](https://user-navigation-tracking.herokuapp.com/dashboard)

## Setup

### Requirements

* Python 3.5+
* pip (should already be installed with python)
* virtualenv (not actually required, but really helpful)
* Redis

### Setup

1. Install python requirements by running ```pip install -r server/requirements.txt```
2. On the terminal, export the environment variable with the port number on where to run the server: ```export PORT=5000```
3. Follow the section [UNT Integration](#unt-integration) to learn how to target your local server on the javascript plugin

## Running

### Server

1. Change directory into ```user-nav-track/server/```
2. Run the commando ```uwsgi --ini config/uwsgi.ini```
3. On another terminal run ```python workers/tracking_worker.py```
4. On your browser, access ```http://localhost:<port>/dashboard```
5. Keep in mind nothing is mapped on the root (/) endpoint. This is by design, a little security by obscurity to reduce DOS chance

### Test website

1. On your browser, open ```user-nav-track/website/index.html```
2. Navigate freely through the website
3. Make sure to subscribe an email on the **Contact** page for the user to show on the server's dashboard
4. By default, the test website targets the live server at [https://user-navigation-tracking.herokuapp.com](https://user-navigation-tracking.herokuapp.com)

## UNT Integration

UNT can be used on any website. To do so, one has to simply import the plugin (```user-nav-track/server/js-tracker/unt.js```) to the pages that wish to track, and set it to target the correct server. To do so:

1. Copy the ```unt.js``` file to the static/js/ folder of the website
2. Import the plugin by adding the following line at the end of the <body> tag: ```<script src="static/js/unt.js"></script>``` (the path might be different if running on different settings)
3. Instantiate the plugin passing the target server by adding the following lines below the script import, replacing the *<server_address>* with your own:
```    <script>
        UNT(*<server_address>*);
    </script>```

### Changing default plugin server

Instead of setting the target server on each page, it is possible to change de default server address by editting the unt.js file, and changing the value of the **default_server_addr** variable at line 53.
After that, the plugin can be initialized as ```UNT();```

## Under the hood

### Tracking

Upon executing UNT main function, the user is assigned an **uuid**, and it is stored on the browser's **localstorage**, to persist through sessions.
All tracking is done based on this uuid, and is saved on the database as the user navigates, as an user with a null email.
Upon registering an email, the user entry is updated, allowing it to be identified and addressed on the dashboard.
All previous and future records will be kept under the user, granted the uuid is still preserved on the localstorage.

### Concurrency

To comply with high traffic, queues are in used, through RQ.
All tracking requests are queued for later processing, as it is not time critical.
The email registraton is processed live, as a feedback is required.

### Access times

There are two datetimes being saved for the access logs: **local_time** (the time on the browser of the client) and **server_time** (the time on the server).
They might differ, even on the same timezone, therefore the need to store both.
Currently, only local_time is in use on the dashboard.

