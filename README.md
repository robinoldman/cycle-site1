# Cycle Alpine

Cycle Alpine is a site that allows users to view and record their times on specific Austrian cycle routes.

## Table of Contents

- [User Experience (UX)](#user-experience-ux)
- [Features](#features)
- [Design](#design)
- [Planning](#planning)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)

### User Stories

1. **US01: Illustrate Purpose of the Application through UI**
    - As a Site User, I can view the landing page to determine the purpose of the application.
2. **US02: Navigate Site**
    - As a Site User, I can navigate through the application using the menu to easily access application functionality.
3. **US03: View Cycle Routes**
    - As a Site User, I can view a list of hikes/excursions to select one and access more details.
4. **US04: View Route Information**
    - As a Site User, I can click on a hike to view its full details.
5. **US05: View Previous Times**
    - As a Site User, I can view previous times from other users for a specific route.
6. **US06: View Booked Hikes**
    - As a Site User, I can access a list of hikes I have booked to see an itinerary of my hikes.
7. **US08: View a Map**
    - As a Site User, I can view an interactive map of my route using Google Maps.
8. **US10: Add a New Route**
    - As a Site User, I can add a new route for other users to see.
9. **US11: View Comments**
    - As a Site User, I can view comments on individual hikes to record feedback and identify areas for improvement.
10. **US12: Approve Comments**
    - As a Site Admin, I can review and approve or disapprove comments to filter out unsuitable or objectionable content.
11. **US13: Account Registration and Login**
    - As a Site User, I can register an account to log in and then book a hike, leave comments on hikes, and like hikes.
12. **US14: Manage Routes**
    - As a Site Admin, I can create, read, update, and delete routes to manage site content.
13. **US15: Comment Delete**
    - As a Site User, I can delete the comment I have made.
14. **US16: Comment Edit**
    - As a Site User, I can edit the comment I have made.


**User Story 1:**
"As a cyclist planning a trip to the Austrian Alps, I want to be able to track my progress on specific bike routes and see the most beautiful scenic spots along the way, so that I can have an enjoyable and memorable experience.

When I visit the website, I want to be able to sign up for an account using my email and password, or by using a third-party authentication service. Once I'm signed up, I want to be able to browse a map of the Austrian Alps that shows all available bike routes, and select a route that suits my interests and skill level.

After selecting a route, I want to be able to see a detailed map that highlights the most scenic spots along the way, such as mountain peaks, lakes, and historical landmarks. I also want to be able to track my progress on the route by starting and stopping a timer that records my time and distance, and see my progress displayed in real-time on the website.

Finally, I want to be able to compare my progress with other users who have completed the same route, and see how I stack up against other cyclists. I want to be able to view leaderboards and rankings for each route, and filter the results by age group or other criteria."

 

**User Story 2**
: "As a cycling enthusiast living in the Austrian Alps, I want to be able to track my progress on specific bike routes and compete with other local cyclists, so that I can improve my skills and have fun.

When I visit the website, I want to be able to sign in to my account using my email and password, or by using a third-party authentication service. Once I'm signed in, I want to be able to see a map of all available bike routes in the Austrian Alps, and select a route that I want to track my progress on.

After selecting a route, I want to be able to start and stop a timer that tracks my time on that route, and see my progress displayed in real-time on the website. I also want to be able to save my progress data to my account, so that I can come back later and see how I've improved over time.

Finally, I want to be able to compare my progress with other local cyclists who have completed the same route, and see how I stack up against the competition. I want to be able to view leaderboards and rankings for each route, and filter the results by age group or other criteria. I also want to be able to connect with other local cyclists through the website and arrange group rides and events."

**User Story 3 Austrian tourist board**

"As the Austrian Tourist Board, we want to encourage tourists to visit the Austrian Alps and experience the beauty of the region through cycling. We plan to partner with a website that allows users to track their progress on specific bike routes and share their experiences with others.

When we visit the website, we want to see a visually appealing and easy-to-use interface that showcases the most popular bike routes in the region. We want to be able to see detailed maps of each route, highlighting the most scenic spots and points of interest along the way.

We also want to be able to see user-generated content, such as photos and reviews, to get an idea of what it's like to cycle in the Austrian Alps. We want to be able to filter the content by location, skill level, or other criteria, so that we can tailor our marketing efforts to different types of cyclists.

Finally, we want to be able to collaborate with the website owners to promote cycling in the Austrian Alps to a wider audience. We want to be able to share user-generated content on our social media channels, and offer incentives to users who complete certain routes or achieve certain milestones.

By partnering with this website, we hope to encourage more tourists to visit the Austrian Alps and experience the natural beauty of the region through cycling."

## Features

### Existing Features



• **F01 Navigation Bar**
   - The navigation bar ensures consistent appearance and placement across all pages, facilitating easy and intuitive navigation. It comprises a logo and links to the Home page, new routes, and set routes. For non-signed-in users, there are additional links to the Register and Sign In pages. Once signed in, users can access the Home page along with links to new routes and set routes. The navigation bar also displays the active username and a user icon. It adapts responsively to different screen sizes, transforming into a "burger" menu style on smaller screens.
• **F02 Landing Page Image and Text**
   - Located at the top of the landing page (home page), there is a visually appealing section featuring a captivating photograph accompanied by text overlay. This combination effectively communicates the purpose of the website as a platform for discovering new and exciting cycle routes.
   ![home](static/readmeimages%20/homepageheronav.png)
• 

•**F03 Set Routes**
   - Further down on the landing/home page, a list of cycle routes is shown. Each summary gives an image of the hike and a title,  At a glance, the user can quickly decide if this is a hike that might appeal to them. Each route picture expands when clicked with the buttons then becoming active. The user can then decide to view extra detail on the route and log a time or view previous times.

    ![set](static/readmeimages%20/setroutes1.png)

• **F04 Routes Detail Page**
   - When a user clicks on a cycle summary title on the home page, they are brought to the Cycle Detail page for the clicked cycle. Here the user is shown a full description of the cycle route, the location for the route, the difficulty rating, a map, and estimated duration. Only users who are signed in can comment on a route.

     ![setroute](static/readmeimages%20/setroutewithmap.png)

• **F05 Comment on a set Route**
   - In order to comment on a route, a user must be signed in. A comment can be added on any time that users have recorded or new cycle route that users have logged. The user enters their comment in a text box under the cycle description and clicks on Submit. The comment must be approved by the admin user before it will be visible. To approve comments, the admin user logs in to the admin pages, opens the Comments table, selects the comment(s) to be approved, chooses the 'Approve Comments' action from the drop-down menu, and clicks 'Go'.

    ![publise](/static/readmeimages%20/publisedownroute1.png)
• **F08 My Routes Page**
   - In order to access the My Routes page, a user must be signed in. The My Routes page provides a convenient place for the user to write down their own route to share with the community. Users are then able to comment on one another's routes by clicking on the post.

    ![postroute](/static/readmeimages%20/postownroute1.png)

• **F09 User Authentication**
   - The application provides the following user authentication-related functions:
     - User Registration: The application provides user authentication features, including user registration. To sign in, users need to register first. The "Register" option is available on the navigation bar when no user is currently signed in. During registration, users are required to provide a username, an optional email address (which must be unique), and a password (entered twice for confirmation). Once registered, users can log in to the application and access its features.
     - User Sign-in: Once registered, a user can sign in and will have access to extra functionality, namely:
       - Comment on a route
       - Create a new route
       - Time their routes on the routes set by the website
       - To sign in, the user must provide a) a registered username and b) the password for the username.
     - User Sign-out: A user who is currently signed in can easily sign out by clicking on the "Sign out" link available on the navigation bar. To complete the sign-out process, the user simply needs to confirm the action by clicking on the "Sign out" button displayed on the page.


• **F11 Add and Publish a Route**
   - The admin user, who has special privileges, is responsible for adding and publishing routes using the admin pages. These pages can be accessed either by appending '/admin' to the application URL or by signing in to the application and clicking on the "Admin" link, which is only visible when the admin user is signed in. To add a new route, the admin user can click on the "+ Add" link located next to the route table name form where the admin user can enter the necessary data for the route. It's important to note that route titles must be unique, and as the admin user starts typing the title, a slug (a URL-friendly version of the title) will be automatically generated. A rich editor called Summernote is provided for the hike description content field, allowing the admin user to easily add formatting to the text.

• **F12 Visual Route Maps**
   - There is a visual route map for each set route. This map shows a start and end point with a route between these points.

    ![map](static/readmeimages%20/setroutewithmap.png)

• **F13 On-screen Messages**
   - An on-screen message appears whenever a user has written a comment to tell the user their comment is waiting for approval.



## Wireframes

The wireframe diagrams below describe the Home, Site  Wireframes are available for desktop, tablet, and smartphone views. 

![wireframe](static/readmeimages%20/wireframe1.png)
![wireframe](static/readmeimages%20/wireframe%202.png)




## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project. The acceptance criteria were tested as each story moved to 'Done' and were also included in the final pre-submission manual testing documented in the Testing section of this README. I have attached a image of the agile and moved the stories around for ease of reading rather than all done

Agile tool can be found here: [Aglie](https://github.com/robinoldman/cycle-site1/blob/main/agile.png)



### Languages Used

- HTML5
- CSS3
- Python

### Frameworks, Libraries & Programs Used

1. Django: Utilized as the framework to facilitate rapid and secure development of the application.
2. Google Fonts: Incorporated to implement the Lato font in the project.
3. Font Awesome: Employed to enhance aesthetics and user experience by adding icons.
4. Bootstrap: Utilized to create responsive web pages.
5. Git and GitHub: Employed for version control, using the Gitpod terminal to commit changes to Git and push them to GitHub. Additionally, GitHub was used for agile development by utilizing User Stories (GitHub Issues) and tracking progress on a Kanban board.
6. Gunicorn: Used as the web server to run Django on Heroku.
7. psycopg2: A database adapter used to support the connection to the PostgreSQL database.
8. Cloudinary: Utilized as a storage solution for the application's images.
9. Summernote: Incorporated to provide a WYSIWYG (What You See Is What You Get) editing experience on the Hike editing screen.
10. Django allauth: Employed for account registration and authentication functionality.
11. Django Crispy Forms: Used to simplify the rendering of forms in the application.



### Validator Testing

- HTML Validator: As this project uses Django templates, the HTML has been validated by manually clicking through the application pages, copying the source of the rendered pages, and then validating this version of the HTML using the W3C Validator. HTML for the Django admin site pages was not edited, so it has not been validated here. The Signup, Login, and Logout pages from Django allauth were customized and have been validated, with results below.
  - Results for Home: Pass
  - Results for Millstatt, Bad Kleinkirchheim, Villach, and Wörthersee HTML: Pass
  - Results for Base, Main, Own Route, Post, Comments, and Route HTML: Pass
  - Results for Signup: Pass
  - Results for Login: Pass

- CSS Validator: Pass
- JavaScript Validator: Pass

![validator](static/readmeimages%20/validator.png)
![validator](static/readmeimages%20/validator1.png)
![validator](static/readmeimages%20/validator2.png)

### Browser Compatibility

To ensure the application's compatibility across different browsers, the following approach was taken:
- Chrome DevTools: Used to test the application's responsiveness on various screen sizes during development.

### Manual Testing Test Cases and Results

The application underwent manual testing to validate its functionality and adherence to user story acceptance criteria. The test cases and results are documented in a PDF, which includes cross-references to the corresponding Feature IDs. The test cases were designed based on the acceptance criteria of user stories, enabling thorough testing throughout the development iterations.

[Manual test](https://github.com/robinoldman/cycle-site1/blob/main/test.pdf)

### Known bugs

Currently, there are no known bugs.

## Deployment

Deployment Instructions:

To deploy this project, follow the detailed steps outlined below. Code Institute also provides a summary of similar processes, which can be found here: [Link to Code Institute deployment summary]

1. Cloning the Repository:
   - Visit the project repository on GitHub: [Link to GitHub Repository]
   - Click the "Code" button on the right side of the screen, select "HTTPs," and copy the provided link.
   - Open a GitBash terminal and navigate to the desired directory for the clone.
   - In the terminal, enter "git clone" followed by the copied URL, then press Enter to initiate the cloning process.
   - Install the required packages by running the command: "pip install -r requirements.txt."
   - When developing and running the application locally, set DEBUG=True in the settings.py file.
   - Push any changes made to the local clone back to the repository using the commands: "git add filenames" (or "." to add all changed files), "git commit -m 'text message describing changes'," and "git push."
   - Note: Changes pushed to the master branch will take effect on the live project once the application is redeployed from Heroku.

2. Creating the Application and Postgres DB on Heroku:
   - Log in to Heroku at https://heroku.com (create an account if necessary).
   - From the Heroku dashboard, click the "Create new app" button. If you have a new account, an icon will be visible on the screen; otherwise, access this function under the "New" dropdown menu.
   - On the "Create New App" page, provide a unique name for the application, select a region, and click "Create app."
   - In the Application Configuration page for the new app, navigate to the "Resources" tab.
   - Search for "Postgres" in the Add-ons search bar and select "Heroku Postgres" from the list. Follow the prompts to submit the order form.
   - Next, go to the "Settings" tab on the Application Configuration page and click the "Reveal Config Vars" button. Ensure that the DATABASE_URL has been automatically set up.
   - Add two new Config Vars: DISABLE_COLLECTSTATIC (set value as 1) and SECRET_KEY (assign a random string of letters, digits, and symbols).
   - Update the settings.py file to use the DATABASE_URL and SECRET_KEY environment variable values as follows:
     - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
     - SECRET_KEY = os.environ.get('SECRET_KEY')
   - In Gitpod, in the project terminal window, run the command "python3 manage.py migrate" to initialize the data model in the Postgres database.
   - Ensure that the project's requirements.txt file is up to date with all necessary supporting files by entering the command "pip3 freeze --local > requirements.txt."
   - Commit and push any local changes to GitHub.
   - To run the application on localhost, add SECRET_KEY and DATABASE_URL with their respective values to env.py.

3. Configuring Cloudinary for Hosting Images:
   - Log in to Cloudinary (create an account if needed) and access the dashboard.
   - Copy the "API Environment variable" value from the dashboard.
   - Log in to Heroku, go to the Application Configuration page, and click "Settings." Then click "Reveal Config Vars."
   - Add a new Config Var named CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, excluding the "CLOUDINARY_URL=" prefix.
   - To run the application on localhost, add the CLOUDINARY_URL environment variable and its value to env.py.

Connecting the Heroku App to the GitHub Repository:

To establish the connection between your Heroku app and the GitHub repository, follow these steps:

1. Go to the Application Configuration page of your Heroku app and navigate to the "Deploy" tab.
2. Choose "GitHub" as the Deployment Method. If prompted, confirm your intention to connect to GitHub.
3. Enter the name of your GitHub repository (the one used for this project) and click "Connect" to establish the link between your Heroku app and the GitHub repository code.
4. Scroll down the page and select either "Automatically Deploy" (triggering deployment whenever changes are pushed to GitHub) or "Manually Deploy" (allowing manual control over deployment). For this project, "Manual Deploy" was selected.
5. To run the application, you can access it directly from the Application Configuration page by clicking the "Open App" button.
6. The live link for this project can be found at [insert live link here].

Final Deployment Steps:

After completing and testing the code changes on localhost, follow these steps to prepare the application for deployment on Heroku:

1. Set the DEBUG flag to False in the settings.py file.
2. Make sure the following line exists in the settings.py file to enable summernote functionality on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'.
3. Ensure that the requirements.txt file is up to date by executing the command: "pip3 freeze --local > requirements.txt".
4. Push all files to the GitHub repository.
5. In the Heroku Config Vars for your application, delete the DISABLE_COLLECTSTATIC environment variable.
6. On the Heroku dashboard, go to the "Deploy" tab for your application and click "Deploy Branch."
7. The final deployed version of the application can be accessed through the live link provided here: [insert live link here].

Please note that the above instructions are a general guideline for deploying a Django project on Heroku. You may need to adapt the steps according to your specific project configuration and requirements.




### Credits

#### Code

- A lot of the coding and testing relies on information in the "Hello Django" and "I Think Therefore I Blog" walkthroughs in the Code Institute course.
- Information on how to use a foreign key: [Django Documentation - Many-to-One Relationships](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/)
- Information on how to order models: [Django Documentation - Model Meta options](https://docs.djangoproject.com/en/4.2/ref/models/options/)
- Google Maps API: [Google Maps API Documentation](https://developers.google.com/maps)
- Code to make sliding panels: [Udemy Course - Sliding Panels](https://www.udemy.com/home/my-courses/learning/)
- Code to help me with understanding slugs: [Learn Django - Django Slug Tutorial](https://learndjango.com/tutorials/django-slug-tutorial)

#### Media

- The Lato font used was imported from [Google Fonts](https://fonts.google.com/).
- Font Awesome was used for social icons and bike icon: [Font Awesome](https://fontawesome.com/).

#### Mountain Images

- [Pexels - Empty road along the mountain](https://www.pexels.com/photo/empty-road-along-the-mountain-2739013/)
- [Pexels - Brown logs on grass field](https://www.pexels.com/photo/brown-logs-on-grass-field-358532/)
- [Pexels - Alps](https://www.pexels.com/search/alps/)
- [Pexels - Bird's-eye view photography of mountains](https://www.pexels.com/photo/bird-s-eye-view-photography-of-mountains-552785/)
- [Pexels - Person walking on hill](https://www.pexels.com/photo/person-walking-on-hill-554609/)

### Acknowledgments

- Thank you to my mentor Brian Macharia for his continuing help and feedback.

...
import os

os.environ["DATABASE_URL"]="postgres://cyxcrowj:OLYR4ToxmyyqgO7nnrXbVFlSEq0CZ8G4@rogue.db.elephantsql.com/cyxcrowj"
os.environ["SECRET_KEY"]="RobinOldman"
os.environ["CLOUDINARY_URL"] = 'cloudinary://962444711949455:IEF70dVolBgsnC0nr_HzBPQZYuA@dwpdkpzlx'

env.py

The error message suggests that the URL pattern post/None/edit/ is being matched, but it should not be the case. It appears that the comment_slug value is not being passed correctly to the URL or the view.

pip install -r requirements.txt

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **March 3rd, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

