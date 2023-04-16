# boejaker.github.io [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/BoeJaker/boejaker.github.io.git/master)
### A portfolio of programming examples, website templates &amp; more!      

***
</br>

## Problem Statement
Employers and collaborators do not have an easy way to view or experience my work. Github is good for version control but lacks substance.  

I post my work to multiple platforms, social media and blogs, this makes it hard to see all my content without lots of searching.  

Maintianing multiple websites over sveral platforms makes keeping track of broken links, key information, domain renewals  and other such issues is time consuming and prone to error or inconsistency.  

***
</br>  

## Solution
A single webpage that aggregates all of my content and posts automatically.   
List and summarize my most notable repos automatically with javascript API calls to github.  

Interactive sections that run deployed code.  

A section that contains my contact details and a dynamic CV element that updates as I update the google doc.  

Website CI/CD Script  
A script that scans each website for broken links, missing images, broken interactive elements incorrect contact info, domain name renewal. It will also measure response times and pageload speeds. To keep me up to speed i will intergrate a notification API such as pushbullet.

With these features i will be able to keep posting to my other platforms as i was with all new content automatically displaying on the portfolio. I wont have to keep checking if everything is up to date and working as the website scanner will notify me of any issues.

***
</br>  

## Design Specification
Must be easy to use on both PC and Mobile (responsive).  

Must provide my contact details in several places - uses animation to draw the eye to at least one.  

A distinct, clashing, color pallette.  

A modular extensible design

This should create an easy to use, memorable, experience that easy easy to upkeep and extend the features of.

***
</br>  

## Implementation
Minimal use of libraries, use my own code wherever feasible.  

Minimal HTML for quick upkeep.

</br>  

## Development Workflow
![software development workflow](assets/SoftwareDevelopmentWorkflow.png)
***
</br>

## Testing & Deployment

### JavaScript Unit Test
Files / Folders:
jest.config.js
babel.config.js

This website has JavaScript unit test that have been designed for it.
To run the unit tests open a terminal in the base directory and type the following:  

    yarn install

    yarn test

These test check that the website renders correctly and the javaScript behaves as intended. It is designed as a pre pull/push check, ensuring you have not changed the layout accidentally whilst editing the source.

</br>

### Test Server
Included is a local python server. to run the server, from the text/Server directory execute either of the following in a terminal:

    python test/Sever/test_server.py

or

    docker build -t test_server -f ./test/Server/Dockerfile .

    docker run -ti -p 8000:8000 test_server

This will allow you to connect to the website on a local network - this can be useful for testing on mobile devices before pulling or pushing to git.

</br>

### CI/CD Test
Files / Folders:
website_test.py
dockerfile

The deployment tests run as a scheduled docker container on a server. They check that my websites in production are operating as expected.

From the test/Remote directory execute

    python website_test.py

or

    docker build website_test -f ./test/Remote/Dockerfile .

    docker run -ti -p 80:80 website_test

This will create a service that checks the website for error at a set cadence

</br>  

### Test Suite

From the base directory execute the following in a terminal.

    docker-compose build
    docker-compose run
    
This will build both parts of the test suite mentioned above the local test server and a CI/CD tester.

***
</br>

## Conclusion

***
</br>

## To Do
Condense all tests into one containerized workflow that hosts the local server and also schedules CI/CD checks.


