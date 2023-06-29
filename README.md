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

## Features

### Existing Features



• **F01 Navigation Bar**
   - The navigation bar ensures consistent appearance and placement across all pages, facilitating easy and intuitive navigation. It comprises a logo and links to the Home page, new routes, and set routes. For non-signed-in users, there are additional links to the Register and Sign In pages. Once signed in, users can access the Home page along with links to new routes and set routes. The navigation bar also displays the active username and a user icon. It adapts responsively to different screen sizes, transforming into a "burger" menu style on smaller screens.
• **F02 Landing Page Image and Text**
   - Located at the top of the landing page (home page), there is a visually appealing section featuring a captivating photograph accompanied by text overlay. This combination effectively communicates the purpose of the website as a platform for discovering new and exciting cycle routes.
• **F03 Set Routes**
• **F03 Set Routes**
   - Further down on the landing/home page, a list of cycle routes is shown. Each summary gives an image of the hike, a title, details on distance and estimated duration, and an image rating the difficulty of the route - easy/moderate/hard. At a glance, the user can quickly decide if this is a hike that might appeal to them. Each route picture expands when clicked with the buttons then becoming active. The user can then decide to view extra detail on the route and log a time or view previous times.
• **F04 Routes Detail Page**
   - When a user clicks on a cycle summary title on the home page, they are brought to the Cycle Detail page for the clicked cycle. Here the user is shown a full description of the cycle route, the location for the route, the difficulty rating, a map, and estimated duration. Only users who are signed in can comment on a route.
• **F05 Comment on a Route**
   - In order to comment on a route, a user must be signed in. A comment can be added on any time that users have recorded or new cycle route that users have logged. The user enters their comment in a text box under the hike description and clicks on Submit. The comment must be approved by the admin user before it will be visible on the Hike Detail page. To approve comments, the admin user logs in to the admin pages, opens the Comments table, selects the comment(s) to be approved, chooses the 'Approve Comments' action from the drop-down menu, and clicks 'Go'.
• **F08 My Routes Page**
   - In order to access the My Routes page, a user must be signed in. The My Routes page provides a convenient place for the user to write down their own route to share with the community. Users are then able to comment on one another's routes by clicking on the post.
• **F10 User Authentication**
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

• **F13 On-screen Messages**
   - An on-screen message appears whenever a user has written a comment to tell the user their comment is waiting for approval.


## Design

...

## Planning

...

## Technologies Used

...

## Testing

...

## Deployment

...

## Credits

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

Happy coding!
