# Problem Set 2

## Admin Facing:

    Link For Home Page: https://mydemoapp08.herokuapp.com/

## User Facing:

    Link for Home page: https://mydemoapp08.herokuapp.com/user/home



## Scheduling of Tasks
 
    Used "Advance Python Scheduler(APScheduler)" Module in python to update the catrgory of the app to the database for every 24 hours which is taking from the playstore for that particular Application.

    You can find the files that contain code which schedules the task in pythonscheduler folder.

    we have to create a seperate app to run this scheduler app.
    In my case I have created one app called "testing" and run the scheduler from that app directory.




## Note:
    You can signup for once and use those credentials for both of the admin and the user as well. 
    If you want to have seperate users you can create seperate credentials for both the Admin and the user.






## API Section

    Rest API details: https://mydemoapp08.herokuapp.com/user/api 

    This will expose the api endpoint details to the user who are logged in only, thus making it as a permission based views
    we can enter 1 or 2 in the input field and gives that respective app details to the user
    If there is no endpoint related to that app number it returns None/Null.




## Project Deployment

    Made the project deployed in heroku - https://www.heroku.com/

    Create a new Project and add a python buildpack for that project

    Add requirements.txt, Procfile to our root directory

    Go to the Heroku Cli or Git Bash and navigate to the project directory
    Make sure we must have install the heroku cli in our local machine

    Run these following commands

    - heroku login
    - cd my-project/
    - git init
    - heroku git:remote -a <app name>
    - git add .
    - git commit -am "make it better"
    - git push heroku master

    and the project will be deployed



