# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Testing Overview

This document records the testing carried out for the Heritage Tomato Club Django project.

Testing covered:

- Code validation
- Manual feature testing
- User authentication
- Membership and Stripe checkout
- Seed Library browsing and filtering
- Grow diary CRUD functionality
- Recipes
- Newsletter signup
- Contact form
- Responsiveness
- Browser compatibility
- Deployment checks
- Bug fixes and known issues

Where possible, testing was carried out on the deployed site as this represents the final submitted version.

Deployed site:

- https://tomatoes.cassiterite.digital

---

## Code Validation

### HTML

HTML was checked using the [W3C Nu HTML Validator](https://validator.w3.org/nu/). The validator was used on rendered deployed pages rather than raw Django templates, because Django template tags are processed server-side before reaching the browser.

| Page / Area         | URL Tested                                                | Result | Notes                                                                      |
| ------------------- | --------------------------------------------------------- | ------ | -------------------------------------------------------------------------- |
| Home                | `https://tomatoes.cassiterite.digital/`                   | Pass   | Main landing page rendered correctly.                                      |
| About               | `https://tomatoes.cassiterite.digital/about/`             | Pass   | Informational content displayed correctly.                                 |
| Membership          | `https://tomatoes.cassiterite.digital/membership/`        | Pass   | Membership tier cards and checkout forms rendered correctly.               |
| Join                | `https://tomatoes.cassiterite.digital/join/`              | Pass   | Join page content and links rendered correctly.                            |
| Resources           | `https://tomatoes.cassiterite.digital/resources/`         | Pass   | Resource page and newsletter form rendered correctly.                      |
| Contact             | `https://tomatoes.cassiterite.digital/contact/`           | Pass   | Contact form rendered correctly.                                           |
| Seed Library        | `https://tomatoes.cassiterite.digital/seeds/`             | Pass   | Filter form, sort buttons and variety cards rendered correctly.            |
| Seed Variety Detail | `https://tomatoes.cassiterite.digital/seeds/ailsa-craig/` | Pass   | Individual tomato variety page rendered correctly.                         |
| Login               | `https://tomatoes.cassiterite.digital/accounts/login/`    | Pass   | Login form rendered correctly.                                             |
| Signup              | `https://tomatoes.cassiterite.digital/accounts/signup/`   | Pass   | Signup form rendered correctly after removing unused social login section. |
| 404 Page            | Invalid URL tested manually                               | Pass   | Custom 404 page displayed correctly.                                       |

A validation issue was found in the redirect page meta refresh syntax:

```html
<meta
  http-equiv="refresh"
  content="0;url=https://tomatoes.cassiterite.digital"
/>
```

This was corrected to:

```html
<meta
  http-equiv="refresh"
  content="0; url=https://tomatoes.cassiterite.digital"
/>
```

After correction, the page validated successfully.

### CSS

CSS was checked using the [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) where applicable. The project uses Tailwind CSS and daisyUI, so most styling is generated from the Tailwind build process rather than written as large custom CSS files.

| CSS Area / File               | Validation Method                                     | Result | Notes                                                              |
| ----------------------------- | ----------------------------------------------------- | ------ | ------------------------------------------------------------------ |
| Main Tailwind/daisyUI output  | Browser rendering check and deployed stylesheet check | Pass   | Generated stylesheet loaded correctly on deployed pages.           |
| `assets/css/styles.css`       | Source file reviewed                                  | Pass   | Contains Tailwind/daisyUI source directives for the build process. |
| `assets/css/tailwind.css`     | Generated CSS output checked                          | Pass   | Built CSS output was present and loaded by the site.               |
| `static/css/admin-custom.css` | CSS validator / manual check                          | Pass   | Admin custom styles were limited and did not cause display issues. |
| Responsive styling            | Manual responsive testing                             | Pass   | Layout worked across mobile, tablet and desktop widths.            |

Tailwind and daisyUI generate utility CSS and framework-specific output. Because this CSS is generated by the build tool rather than manually authored page-by-page, final testing focused on confirming that the compiled stylesheet loaded correctly and that the rendered pages displayed as expected.

### JavaScript

Custom JavaScript was checked manually in the browser and reviewed for syntax issues.

| JavaScript File             | Feature                  | Result | Notes                                                                                         |
| --------------------------- | ------------------------ | ------ | --------------------------------------------------------------------------------------------- |
| `static/js/membership.js`   | Paid membership checkout | Pass   | Paid tier buttons submit a POST request and redirect to Stripe Checkout.                      |
| `static/js/seed-filters.js` | Seed Library filters     | Pass   | Sort, fruit colour and growth habit controls update the query parameters and refresh results. |

A JavaScript issue was found in `seed-filters.js` where stray backticks caused the file to fail. These were removed and the Seed Library filters were retested successfully.

### Python / Django

The Django system check was run:

```bash
python3 manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

### Automated Testing

Focused Django tests were added for the membership and seed library functionality.

The tests cover:

- Membership page loading
- Free membership signup link
- Checkout rejecting direct GET requests
- Checkout requiring login
- Checkout returning JSON for AJAX POST requests
- Seed Library listing active varieties
- Seed Library colour filtering
- Seed Library growth habit filtering
- Seed Library search
- Tomato variety detail page loading

Tests were run with:

```bash
python3 manage.py test club seeds

### Result:

System check identified no issues (0 silenced).
.....

---

Ran 16 tests in 7.357s

OK

## Manual Testing

Manual testing was carried out across the main features of the site.

### Navigation

| Test                 | Expected Result                      | Actual Result             | Status |
| -------------------- | ------------------------------------ | ------------------------- | ------ |
| Open home page       | Home page loads successfully         | Home page loaded          | Pass   |
| Use navbar links     | User can navigate between main pages | Navigation worked         | Pass   |
| Open About page      | About page displays                  | Page loaded               | Pass   |
| Open Resources page  | Resources page displays              | Page loaded               | Pass   |
| Open Contact page    | Contact page displays                | Contact form shown        | Pass   |
| Open Membership page | Membership tiers display             | Tiers displayed correctly | Pass   |
| Open Seed Library    | Seed Library displays varieties      | Varieties displayed       | Pass   |

### User Accounts

| Test                                        | Expected Result                       | Actual Result                           | Status |
| ------------------------------------------- | ------------------------------------- | --------------------------------------- | ------ |
| Open signup page while logged out           | Signup form displays                  | Signup page loaded                      | Pass   |
| Create an account                           | New user account is created           | Account creation worked                 | Pass   |
| Open login page                             | Login form displays                   | Login page loaded                       | Pass   |
| Login with valid account                    | User is logged in                     | Login worked                            | Pass   |
| Logout                                      | User is logged out                    | Logout worked                           | Pass   |
| Open signup page after social login removal | No empty social login section appears | Empty “or sign up with” section removed | Pass   |

### Membership

| Test                             | Expected Result                            | Actual Result                                      | Status |
| -------------------------------- | ------------------------------------------ | -------------------------------------------------- | ------ |
| Open membership page             | Free and paid tiers display                | Membership tiers displayed                         | Pass   |
| Click free tier while logged out | User goes to signup page                   | Signup page opened                                 | Pass   |
| Click paid tier while logged in  | User is redirected to Stripe Checkout      | Stripe Checkout opened                             | Pass   |
| Direct checkout URL using GET    | Request should be rejected                 | `405 Method Not Allowed` returned as expected      | Pass   |
| Paid checkout button             | Button submits POST request                | Checkout session created                           | Pass   |
| Complete Stripe test checkout    | User returns to success page               | Success page loaded                                | Pass   |
| Cancel Stripe checkout           | User returns to cancel page                | Cancel page loaded                                 | Pass   |
| Membership status display        | Logged-in user can see current tier/status | Tier/status shown on membership page/success state | Pass   |

### Stripe Checkout

| Test                               | Expected Result                          | Actual Result                     | Status |
| ---------------------------------- | ---------------------------------------- | --------------------------------- | ------ |
| Stripe public key configured       | Checkout can initialise                  | Checkout initialised              | Pass   |
| Stripe secret key configured       | Server can create checkout session       | Session created                   | Pass   |
| Stripe success route               | Success page loads after payment         | Page loaded                       | Pass   |
| Stripe cancel route                | Cancel page loads after cancellation     | Page loaded                       | Pass   |
| Missing/invalid direct GET request | Checkout endpoint rejects invalid method | `405 Method Not Allowed` returned | Pass   |

### Seed Library

| Test                  | Expected Result                                         | Actual Result               | Status |
| --------------------- | ------------------------------------------------------- | --------------------------- | ------ |
| Seed Library loads    | Active tomato varieties display                         | Varieties displayed         | Pass   |
| Fixture data loaded   | Deployed site contains tomato variety data              | Seed Library populated      | Pass   |
| Placeholder images    | Varieties without images use default tomato placeholder | Placeholder image displayed | Pass   |
| Variety detail page   | Individual variety detail opens                         | Detail page loaded          | Pass   |
| Search by name/origin | Matching varieties display                              | Search worked               | Pass   |
| Fruit colour filter   | Matching colour varieties display                       | Filter worked               | Pass   |
| Growth habit filter   | Matching habit varieties display                        | Filter worked               | Pass   |
| Sort by name          | Varieties sort alphabetically                           | Sorting worked              | Pass   |
| Sort by maturity      | Varieties sort by days to maturity                      | Sorting worked              | Pass   |
| Clear filters         | Filters reset                                           | Clear filters worked        | Pass   |

### Grow Diary

| Test                            | Expected Result               | Actual Result         | Status |
| ------------------------------- | ----------------------------- | --------------------- | ------ |
| Open grow diary while logged in | Diary page loads              | Page loaded           | Pass   |
| Create diary entry              | New entry is saved            | Entry created         | Pass   |
| View diary entry                | Entry detail page opens       | Detail page loaded    | Pass   |
| Edit diary entry                | Existing entry can be updated | Entry updated         | Pass   |
| Delete diary entry              | Entry can be removed          | Entry deleted         | Pass   |
| Unauthenticated access          | User is redirected or blocked | Access control worked | Pass   |

### Recipes

| Test                    | Expected Result                | Actual Result      | Status |
| ----------------------- | ------------------------------ | ------------------ | ------ |
| Open recipe list        | Recipe page loads              | Page loaded        | Pass   |
| Open recipe detail      | Recipe detail displays         | Detail page loaded | Pass   |
| Recipe content displays | Recipe information is readable | Content displayed  | Pass   |

### Newsletter Signup

| Test                   | Expected Result                               | Actual Result          | Status |
| ---------------------- | --------------------------------------------- | ---------------------- | ------ |
| Submit valid email     | Subscriber is saved and success message shown | Signup worked          | Pass   |
| Submit duplicate email | Duplicate is handled gracefully               | Error/feedback shown   | Pass   |
| Submit invalid email   | Validation error shown                        | Invalid email rejected | Pass   |

### Contact Form

| Test                   | Expected Result                        | Actual Result | Status |
| ---------------------- | -------------------------------------- | ------------- | ------ |
| Open contact page      | Contact form displays                  | Form loaded   | Pass   |
| Submit valid message   | Message is accepted and feedback shown | Form worked   | Pass   |
| Submit incomplete form | Validation errors display              | Errors shown  | Pass   |

### Error Pages

| Test                     | Expected Result             | Actual Result   | Status |
| ------------------------ | --------------------------- | --------------- | ------ |
| Visit invalid URL        | Custom 404 page displays    | 404 page loaded | Pass   |
| Use 404 navigation links | User can return to the site | Links worked    | Pass   |

---

## Responsiveness

The deployed site was checked using browser developer tools at mobile, tablet and desktop widths.

| Page           | Mobile | Tablet | Desktop | Notes                                      |
| -------------- | ------ | ------ | ------- | ------------------------------------------ |
| Home           | Pass   | Pass   | Pass    | Hero and cards remained readable.          |
| About          | Pass   | Pass   | Pass    | Text layout remained readable.             |
| Membership     | Pass   | Pass   | Pass    | Tier cards stacked on smaller screens.     |
| Seed Library   | Pass   | Pass   | Pass    | Cards and filters adapted to screen width. |
| Variety Detail | Pass   | Pass   | Pass    | Details remained readable.                 |
| Login / Signup | Pass   | Pass   | Pass    | Forms remained usable.                     |
| Grow Diary     | Pass   | Pass   | Pass    | CRUD pages remained usable.                |
| Contact        | Pass   | Pass   | Pass    | Form remained usable.                      |

---

## Browser Compatibility

The deployed site was checked in the following browsers.

| Browser                   | Result | Notes                                           |
| ------------------------- | ------ | ----------------------------------------------- |
| Chrome                    | Pass   | Main user flows worked.                         |
| Firefox Developer Edition | Pass   | Pages and forms displayed correctly.            |
| Brave                     | Pass   | Navigation, membership and Seed Library worked. |

---

## Lighthouse

Lighthouse was used as a general quality check during final testing.

| Area           | Result  | Notes                                                                   |
| -------------- | ------- | ----------------------------------------------------------------------- |
| Performance    | Checked | Site loaded successfully and remained usable.                           |
| Accessibility  | Checked | Pages used semantic headings, readable text and accessible form labels. |
| Best Practices | Checked | HTTPS restored and production settings corrected.                       |
| SEO            | Checked | Main pages had useful titles and readable content.                      |

---

## Deployment Testing

The deployed VPS version was tested after final fixes.

| Test             | Expected Result                      | Actual Result                        | Status |
| ---------------- | ------------------------------------ | ------------------------------------ | ------ |
| Live URL loads   | Site loads at deployed domain        | Site loaded successfully             | Pass   |
| HTTPS works      | Browser accepts SSL certificate      | SSL restored                         | Pass   |
| Gunicorn service | Service is active                    | `heritagetomato.service` running     | Pass   |
| Nginx proxy      | Nginx proxies to Gunicorn            | Proxy corrected to port `8000`       | Pass   |
| Static files     | CSS and JavaScript load              | Static files loaded after collection | Pass   |
| Django check     | No configuration errors              | `python3 manage.py check` passed     | Pass   |
| Seed fixture     | Seed data available on deployed site | Fixture loaded                       | Pass   |

---

## Security / Production Configuration Testing

| Test                 | Expected Result                     | Actual Result                 | Status |
| -------------------- | ----------------------------------- | ----------------------------- | ------ |
| `SECRET_KEY`         | No hardcoded fallback in repository | Environment variable required | Pass   |
| Missing `SECRET_KEY` | App fails clearly if missing        | Runtime error configured      | Pass   |
| `DEBUG` default      | Defaults to `False`                 | Default set to `False`        | Pass   |
| Deployed `DEBUG`     | Production uses `DEBUG=False`       | Confirmed in VPS environment  | Pass   |
| Checkout response    | Checkout can return JSON            | `JsonResponse` imported       | Pass   |
| `.env` file          | Not committed to GitHub             | `.env` ignored by Git         | Pass   |

---

## Fixed Bugs

| Bug                                                                        | Fix                                                                   | Status |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------ |
| Paid checkout endpoint used `JsonResponse` without importing it            | Imported `JsonResponse` in `club/views.py`                            | Fixed  |
| Checkout links could fall back to GET and produce `405 Method Not Allowed` | Paid tier buttons were changed to use POST form behaviour             | Fixed  |
| Hardcoded fallback `SECRET_KEY` existed in settings                        | Removed fallback and required environment variable                    | Fixed  |
| `DEBUG` defaulted to true                                                  | Changed default to `False`                                            | Fixed  |
| Deployed site returned 502                                                 | Repaired Gunicorn/Nginx proxy configuration                           | Fixed  |
| SSL certificate/config issue affected deployed site                        | Restored Hestia SSL setup and confirmed HTTPS                         | Fixed  |
| Signup page showed “or sign up with” with no social providers              | Removed unused social login block                                     | Fixed  |
| Seed Library was sparse/empty on deployment                                | Added and loaded tomato variety fixture data                          | Fixed  |
| Seed Library filters did not respond                                       | Fixed JavaScript syntax issue and corrected growth habit values       | Fixed  |
| Some old tomato records had missing detail/image issues                    | Updated variety data and cleared broken image fields                  | Fixed  |
| Broken screenshot references existed in testing evidence                   | Removed screenshot references that were not present in the repository | Fixed  |

---

## Known Issues

There are no known blocking issues at the time of final testing.

Automated test coverage is limited and focused on selected high-risk areas. The wider project functionality has also been verified through manual testing.
```
