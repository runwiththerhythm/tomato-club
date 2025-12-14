# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

- https://validator.w3.org/nu/?doc=https://runwiththerhythm.github.io/tomato-club/index.html

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [checkout.css](https://github.com/runwiththerhythm/tomato-club/blob/main/checkout/static/checkout/css/checkout.css) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/css-checkout-checkout.png) | ⚠️ Notes (if applicable) |
| profiles | [profile.css](https://github.com/runwiththerhythm/tomato-club/blob/main/profiles/static/profiles/css/profile.css) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/css-profiles-profile.png) | ⚠️ Notes (if applicable) |
| static | [base.css](https://github.com/runwiththerhythm/tomato-club/blob/main/static/css/base.css) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/css-static-base.png) | ⚠️ Notes (if applicable) |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [stripe_elements.js](https://github.com/runwiththerhythm/tomato-club/blob/main/checkout/static/checkout/js/stripe_elements.js) |  | ![screenshot](documentation/validation/js-checkout-stripe_elements.png) | ⚠️ Notes (if applicable) |
| profiles | [countryfield.js](https://github.com/runwiththerhythm/tomato-club/blob/main/profiles/static/profiles/js/countryfield.js) |  | ![screenshot](documentation/validation/js-profiles-countryfield.png) | ⚠️ Notes (if applicable) |
| static | [base.js](https://github.com/runwiththerhythm/tomato-club/blob/main/static/js/base.js) |  | ![screenshot](documentation/validation/js-static-base.png) | ⚠️ Notes (if applicable) |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

## Responsiveness

The site has been tested across modals of display

- Mobile
- Tablet
- Desktop

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Brave](https://brave.com/download)

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues and ensure everything passes above 80%. 

## Automated Testing

I have conducted a series of automated tests on my application.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)


## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/runwiththerhythm/tomato-club?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/runwiththerhythm/tomato-club/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/runwiththerhythm/tomato-club/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/runwiththerhythm/tomato-club/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/runwiththerhythm/tomato-club?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/runwiththerhythm/tomato-club/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/runwiththerhythm/tomato-club/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

