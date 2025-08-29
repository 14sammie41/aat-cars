![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# AAT Cars

This page is the brain child of observing numerous sites for clubs and groups I am a part of. The idea of the page is to allow car enthusiasts to post articles about there cars where other enthusiasts can browse and enjoy looking at them. There will be the ability to comment and 'like' other people's posts too.

The long term goal of the page will be for clubs and groups to be able to sell their merchandise and group members to order on there too but i did not have time to be able to add these abilities.

## User interactions

The base idea will be to have pre published articles from owners with their car and details of who they are etc. The home page will be a short overview of the individual posts with a preview of the image of the car and a blurb of the article itself. Then there will be a click to open option for each of the posts to be able to see and read more. The final page will only be viewable to permitted users, to allow for admins to do site maintenance.

## Wireframes of all three pages of the site:

I have sketched up 

+ ![]()

## How to:

### Dependencies and Credits

This will be for dependencies as I go through this project - complete as they come through.
+ [Bootstrap](https://getbootstrap.com/) has been used throughout the project to add items like a navbar, a carousel, and a footer. I have annotated throughout the project, the key areas this has been used.
+ [Microsoft Create](https://create.microsoft.com/en-us/features/ai-image-generator) was used to create AI images to utilize for the Home page and some content in other areas.
+ [Canva](https://www.canva.com/colors/color-palette-generator/) was used to choose a colour pallette for the page that aligns with the bright and aggressive nature of some of the cars on the page.
+ [Google Fonts](https://fonts.google.com/) used to import two font styles into the style.css file. Both fonts were attributed to the Root in CSS making the styles uniform across the site.
+ [Font Awesome](https://fontawesome.com/) used to import icons for social links in the footer section. Will most likely be used elsewhere too.
+ [Favicon.io](https://favicon.io/#google_vignette) used to create a simple favicon with the correct colors and fonts as used throughout the site. Then link to each page.
+ [IloveIMG.com](https://www.iloveimg.com/) was used to compress all of my images to optimize page load up.
+ [Grammarly](https://app.grammarly.com/ddocs/2742182934) was used to check and correct all of the grammar on this README file.

## Bug problems and solutions

These bugs were found as I was writing the code, not whilst testing, hence being at this point in the README file.

+ When deploying my initial commit to Heroku I was having issues with it having a server error. It turns out this was caused by having a comma in my `ALLOWED_HOSTS = []` segment in `settings.py`. I solved this by finding the error in the Heroku CLI log.
+ For the sake of proving that I both know how to and ensuring that they work, I created the `posts.json` file to enable the use of a `json` file. This will also facilitate a 'backup' function to allow me to put some posts as permanent fixtures even if the page crashes for any reason, so there will never be a blank page loaded.
+ When auto setting up for users to have a log in to enable commenting etc. I found that the `allauth` download had automatically put those templates into a sub folder called `allauth` meaning that it was not extending `base.html` to allow for consistent formatting. When I moved the `account` folder out of the `allauth` folder all links then worked.
+ When testing deployment to Heroku after adding authentication onto my project i found that my CSS was not being carried over to my Heroku deployed project. After checking my `settings.py` file incase I had missed a path, i found that i had forgotten to run `collectstatic` before saving my files for deployment. This corrected the issue.


## Source for images and text

All images below have been compressed using iloveimg.com to help with load speed on the website.

+ ![2003 Focus RS](static\images\2003-focus-rs.jpg) alt, 2003 Ford Focus RS, image courtesy of Millie Harris - Owner.



## Deployment process

For security reasons I have not put the instructions for deploying my project through Django and Heroku on here as this is a public document. Should you wish to replicate the deployment process through Django and Heroku please follow all of the below and use the documentation on the relevant website.

For tutors and examiners please find the keys required for marking purposes in: 

Running the project locally:
1. Ensure you have a GitHub account [Create one here](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
2. Use Google Chrome as the best browser for this deployment.
3. Install VSCode to your computer or open the browser version [here](https://vscode.dev/).
4. Click the 'Open Remote Repository' button on the home page to clone and or edit as you wish.

To do the above you may need to follow these steps also:
1. Open the repository in GitHub [here](https://github.com/14sammie41/samantha-spencer)
2. Under the name, click 'clone or download'.
3. Once in the clone section copy the HTTP clone URL for the repository.
4. In the local IDE of your choice, open the terminal.
5. Change the current working directory to wherever you want it to be made.
6. Type `git clone`, and then paste the URL you copied in step 3.

Deployment, step-by-step guide:
+ In GitHub, first, ensure all work is committed and pushed, then go to the settings tab on GitHub, then the Pages section on the left-hand navigation.
+ Once in the Pages section on GitHub change the branch drop down to 'Main' and then click the save option.
+ Now go back to the code section of GitHub and click the deployment link on the right-hand side. (You may need to refresh the page to see the deployment link)
+ Once on the deployment page on GitHub click on the provided link and it will open up the deployed project.

## Testing

As I have been testing most aspects as I write the code for the site, I am hoping this is not going to be too much.

### Testing as a user for navigation purposes:
+ 

### Testing with validators:
+ First validator used was [W3Schools HMTL validator](https://validator.w3.org/#validate_by_input). Expecting possibly some missed slashes, but that should be all. 
    + 
+ Second validator used was [W3Schools CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). Expecting some syntax errors as I haven't dived as deep on my CSS as I did on my HTML.
    + style.css shows no errors
+ Checked page using Chrome DevTools. Unsure what to expect, I think I have been pretty thorough with writing my code.
    + Lighthouse shows a performance score of 
    + See below for a screenshot of my DevTools testing:
    + ![]()

+ For all bugs I encountered whilst writing my initial code please refer to the 'bugs section' further up this page.