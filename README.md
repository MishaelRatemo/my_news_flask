# NEWS UPDATER -FLASK APP
## Author

~ Mishael Ratemo
## Description

A Flasl framwork { python } application that keeps up a user with currrent affairs incase one misses news .It provides varous news from techonology, politics, businness,sports among manny others. Also it provides various sources of nes from all over the world that one can choose and read from.This is achiaved by use of [News API](https://newsapi.org/)

## User Story ( BDD ) 
The user would like to.... :
+  to see various news sources on the homepage of the application.
+ select a news source and see all news articles from the selected news source in the application.
+  see the image, description and the time a news article was created.
+ click on an article and read the full article on the source website.

## [Demo](https://newsupdater.herokuapp.com/) click to view



## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3
* flask v2 and above
* gunicorn
* bootstrap

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ``https://github.com/MishaelRatemo/my_news_flask.git``

 + or
 git clone ``git@github.com:MishaelRatemo/my_news_flask.git``

* cd my_news_flask

* Vs code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:
 * #### create flask environnent
        $  python3 -m venv pip virtual -- creates the virtual for runnning your app      
        $ source virtual/bin/env  -- activate  the virtual
        $ chmod +x launcher.py
        $ ./launcher.py
* #### Install Flask and other dependencies/Modules
        $ pip install flask
        $ pip install flask-Bootstrap ( optional)
* #### set up the API KEY
        + create account in [https://newsapi.org] and key will be issued
        + in root fold of your app create  a folder,config file in it and paste you API key and add it to .gitignore
        + alternatively have any python file in root folder and :
            export NEWS_API_KEY='<Your-Api-Key goes here>'
            python3 manage.py server
* #### Run app using vs terminal or main terminal
        $ chmod +x launch.sh
        $ ./launch.sh


## Technologies Used

* python3
* Flask Webframework


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug
* also incase you run it a bug feel free to add or contact

## Contact Information 

If you have any question or contributions, please email me at [ratemomishael@gmail.com](ratemomishael@gmail.com)

LinkedIn - [Mishael Ratemo](www.linkedin.com/in/mishael-mosoti-37b786161/)


Portfolio- [Mishael](https://mishaelratemo.github.io/my_portfolio/)
# Licence

Click to  [MIT License](Licence) view

 Copyright (c) 2022 | Mishael Ratemo