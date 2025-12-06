# [Heritage Tomato Club](https://tomatoes.cassiterite.digital)

Developer: ([runwiththerhythm](https://www.github.com/runwiththerhythm))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://tomatoes.cassiterite.digital)

## Table of Contents

   * [Introduction](#introduction)
   * [UX](#ux)
      * [The 5 Planes of UX](#the-5-planes-of-ux)
         * [1. Strategy](#1-strategy)
         * [2. Scope](#2-scope)
         * [3. Structure](#3-structure)
         * [4. Skeleton](#4-skeleton)
         * [5. Surface](#5-surface)
      * [Colour Scheme](#colour-scheme)
      * [Typography](#typography)
   * [Wireframes](#wireframes)
   * [User Stories](#user-stories)
   * [Features](#features)
      * [Existing Features](#existing-features)
      * [Future Features](#future-features)
   * [Tools &amp; Technologies](#tools--technologies)
   * [Database Design](#database-design)
      * [Data Model](#data-model)
   * [Agile Development Process](#agile-development-process)
      * [GitHub Projects](#github-projects)
      * [GitHub Issues](#github-issues)
   * [Testing](#testing)
   * [Deployment](#deployment)
      * [Heroku Deployment](#heroku-deployment)
      * [Cloudinary API](#cloudinary-api)
      * [PostgreSQL](#postgresql)
      * [WhiteNoise](#whitenoise)
      * [Local Development](#local-development)
         * [Cloning](#cloning)
         * [Forking](#forking)
      * [Local VS Deployment](#local-vs-deployment)
   * [Credits](#credits)
      * [Content](#content)
      * [Media](#media)
      * [Acknowledgements](#acknowledgements)

**Site Mockup**
![screenshot](documentation/mockup.png)

source: [tomato-club amiresponsive](https://ui.dev/amiresponsive?url=https://tomatoes.cassiterite.digital)


## Introduction

Heritage Tomato Club is an online digital membership and subscription service. The site provides information and resources about cultivating heritage tomatoes and offers a yearly subscription service with three tiers including options for basic(free), standard, and premium subscriptions with secure recurring payments using Stripe.
Subscribed member also get access to the Grow Diary tomato growing tracking app.

The site is designed to appeal to home gardeners interested in growing heritage tomatoes from seed and furthering education in the importance of heritage seed saving and cultivation.

## [View deployed version](https://tomatoes.cassiterite.digital)


## UX

### The 5 Planes of UX

#### 1. Strategy


**Purpose**

- Provide home growers and heritage tomato enthusiasts with a central hub to explore tomato varieties, learn cultivation skills, and engage with a friendly community.
- Offer users clear, accessible information about the club’s membership tiers, benefits, and resources.
- Support members with a seed library they can browse, filter, and explore, including detailed variety profiles and images.
- Deliver a warm, vintage-inspired, mobile-first experience that reflects the heritage gardening theme.

**Primary User Needs**

- Users need an easy way to understand what the club offers and which membership tier suits them.
- Users need intuitive navigation from informational pages to actionable steps (e.g., joining, contacting, or browsing seed varieties).
- Users need a visually appealing, readable interface with reliable performance on all devices.
- Members need the ability to explore tomato varieties with clear cultivar information, images, and filters (colour, growth habit, etc.).
- Prospective members need confidence that the site is trustworthy and secure when making payments.

**Business Goals**

- Provide a polished, user-centered Django application aligned with academic requirements and portfolio standards.
- Create a foundation for future expansion into community features, events, or seed-sharing tools.
- Build a strong brand identity for the Heritage Tomato Club using consistent design, storytelling, and accessible UI components.
- Encourage engagement through high-quality resources, membership benefits, and a pleasant browsing experience that invites users to return.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**

- Informational pages for Home, About, Resources, Contact, and Membership.
- Membership tier display with Stripe-powered checkout for paid plans.
- Seed Library: list, filter, and detail views for tomato varieties.
- Tomato variety profiles with images, descriptions, traits, and cultivation info.
- Image uploading for varieties (via Cloudinary).
- Filtering and sorting options (e.g., colour, growth habit, alphabetical).
- Newsletter signup system with admin export functionality.
- User authentication (signup, login, logout) using Django Allauth.
- Customised, vintage-inspired UI using Tailwind CSS and DaisyUI.
- Error handling pages (e.g., 404 and 500) matching the site’s aesthetic.

#### 3. Structure

**Information Architecture**

- **Navigation Menu**:
  - Links to Home, Seed Library, Resources, About, Membership, Join, Contact, Login/Logout.
- **Hierarchy**:
  - Home introduces the club and guides users toward key areas (Seed Library, Membership, Resources).
  - Membership pages clearly explain tier benefits and link to Stripe checkout.
  - Seed Library list and detail views provide structured, easy-to-browse cultivar information.
  - Resource pages present learning materials in a clean, accessible format.

**User Flow**

1. Guest user arrives on the Home Page → learns about the Heritage Tomato Club, browses varieties, and sees prompts to join.
2. User visits the Membership page → selects a tier and begins checkout.
3. User completes Stripe checkout → is redirected to a success page confirming membership.
4. User browses the Seed Library → filters varieties by traits, views detailed profiles, and explores cultivation notes.
5. User returns over time to access new resources, explore more varieties, or manage additional features as the club expands.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used [coolors.co](https://coolors.co) to finalise my color palette.

![screenshot](documentation/coolors.png)

#### Colour Palette Rationale

The Heritage Tomato Club palette was chosen to reflect the warmth, charm, and vintage character of traditional seed packets and heritage gardening culture. The colours are inspired by tomato varieties themselves, paired with earthy tones that evoke allotments, potting sheds, and parchment labels.

**Pomodoro Reds (#C73F34 – #E8594F)**  
Inspired by the deep, rich tones of heritage tomato skins — from beefsteaks to oxhearts. These reds provide warmth and familiarity, making key elements such as headings, accents, and buttons feel inviting rather than harsh.

**Vine Greens (#4E6B41 – #7FA66A)**  
Drawn from tomato foliage and garden twine, these greens introduce balance and calm. They ground the interface and support accessibility by offering contrast when paired with cream backgrounds.

**Golden Seed Yellow (#E6C77A)**  
Echoing heirloom seed packets and dried tomato seeds, this muted yellow adds a nostalgic touch without becoming overly bright. It works well for highlights, badges, and subtle decorative elements.

**Light Mode Foundations (#FAF6EC background, #1A1A1A text)**  
A parchment-like cream background provides excellent readability and a heritage feel. Paired with dark text, it achieves strong contrast while keeping the site warm and organic.

**Dark Mode Foundations (#1B1A18 deep soil brown, #F2EDE5 text)**  
Inspired by soil, hessian sacks, and old greenhouse shelving. This dark palette supports low-light browsing while maintaining the rustic tone of the brand.

By combining warm reds, earthy greens, and vintage cream foundations, the Heritage Tomato Club presents a friendly, accessible, and distinctly horticultural aesthetic that aligns closely with its theme — all while maintaining WCAG AA contrast throughout.


### Typography

- [Modern Thrash](https://thebrandedquotes.sellfy.store/p/modern-thrash-font/) 
The typography choices for the Heritage Tomato Club were selected to evoke the feel of vintage seed packets, traditional gardening guides, and classic printed ephemera — all while maintaining clear readability across devices.

**Headings — Bitter (Serif)**  
Bitter provides a strong, traditional serif style that feels rooted in heritage print design. Its sturdy letterforms pair well with the gardening theme while remaining highly readable on screens.  
Used for: all headings (H1–H6), key section titles, and feature highlights.

**Body Text — Lora (Serif)**  
Lora offers a warm, humanist serif that complements Bitter without competing with it. It is softer and more fluid, making longer paragraphs comfortable to read.  
Used for: paragraphs, descriptions, seed profile text, and general content areas.

**Why These Fonts Work Together**  
- Both typefaces reflect the tone of vintage horticultural publications.  
- Bitter establishes hierarchy and presence, giving pages a confident, editorial feel.  
- Lora supports readability, offering a gentle contrast that prevents the site from feeling overly formal or dense.  
- Together, they reinforce the club’s identity: friendly, traditional, and inspired by classic gardening design.

**Accessibility Considerations**  
- Typography sizes are increased slightly for comfortable reading on mobile.  
- Line heights and spacing are chosen to reduce visual strain.  
- Both fonts maintain high clarity at small sizes due to their modern web-optimized design.

The final result is a cohesive type system that feels authentic to the heritage gardening theme while providing a clean and accessible reading experience.

## Wireframes

![screenshot](documentation/wireframes.png) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a first time visitor,|  I can view detailed information about the app without having to register, | so that I can decide if I want to use it. |
| As a first time visitor, | I would like to be able to navigate the site easily | so that I can find relevant information quickly. |
| As a new user | I can sign up easily using a registration form | so that I can create an account and start using the app. |
| As a registered user | I can log in securely | so that I can access my private dashboard and saved gigs.|
| As a user who forgot my password | I can reset it via email | so that I can regain access to my account.
| As a logged in user,| I can log out, | so that I can end my session securely.|
| As a user,| I can view a friendly error page if I hit a dead link | so that I’m not confused or lost. |
| As a logged in user,| I want to add a gig I attended | so that I can manage user engagement effectively. |
| As a logged in user, | I want the band field to autocomplete when typing| so I don’t create duplicate entries. |
| As a logged in user, | I want to view the full details of a specific gig, | so I can revisit memories and see all the information I entered.|
| As a logged in user, | I want to edit an existing gig,  | so I can fix mistakes or update information like venue, date, or notes.|
| As a logged in user, |  I want to delete a gig, | so I can remove any accidental or unwanted entries.|
| As a logged in user, | I want to view a list of all gigs I’ve entered,| so I can browse my gig history easily.|
| As a logged in user, | I want to upload and manage images for a gig,| so I can visually document the concert experience.|
| As a logged in user, |I want to record a festival as a gig that contains multiple band performances, | so I can document the full experience in one place.|
| As a logged in user, | I want to add other artists who performed at the same gig,  | sso I can log the full lineup. |
| As a logged in user,| I want to see relevant YouTube videos from a gig,| so I can relive the performance without having to manually search. |
| As a logged in user, | I want to quickly see the setlist from the gig,| so I can remember what songs were played. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register / Login / Logout | Handled by django-allauth, allowing users to create secure accounts, log in, and log out. | ![screenshot](documentation/features/register.png) |
| Dashboard | The central hub showing upcoming gigs, attended gigs, and quick stats. | ![screenshot](documentation/features/dashboard.png) |
| My Gigs | Full list view of all a user’s gigs with filtering for upcoming vs past gigs. Entries are displayed as cards with cover images and details. | ![screenshot](documentation/features/my-gigs.png) |
|Add Gig | Users can log a gig they attended or are planning to attend. The form supports band autocomplete, venue search (Mapbox), gig date, status, and genre.| ![screenshot](documentation/features/add-new-gig1.png) |
| Edit / Delete Gig | Existing gig entries can be updated or removed, giving users full control over their vault. | ![screenshot](documentation/features/edit-gig.png) |
| Band Autocomplete | Powered by django-autocomplete-light, users can quickly search and select existing bands or add new ones via modal. | ![screenshot](documentation/features/band-autocomplete.png) |
| Venue Search | Uses Mapbox Search JS to autocomplete venue details. Venue name, city, and country are stored without needing coordinates. | ![screenshot](documentation/features/venue.png) |
| Image Uploads | Users can upload multiple gig images (via Cloudinary). One image can be marked as the cover, and previews are shown before saving. | ![screenshot](documentation/features/image-uploads.png) |
| YouTube Integration | Users can auto-search YouTube for videos of their gig and link them directly into the entry. | ![screenshot](documentation/features/youtube.png) |
| About Page | Introduces the Gig Vault project and its purpose.| ![screenshot](documentation/features/about.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |
| Messages / Feedback | Django messages framework provides clear feedback for actions (e.g., gig created, updated, deleted). | ![screenshot](documentation/features/django-messages.png) |
| Heroku Deployment | Fully deployed to Heroku with Postgres, Cloudinary, and Whitenoise. | ![screenshot](documentation/features/deployed-heroku.png) |

### Future Features

- **Festival Child Gigs**: Ability to create a “parent” festival entry that contains multiple band performances as child gigs. Helps users track festival weekends in detail.
- **Social Sharing**: Quick-share options for individual gig entries to platforms like Instagram, Facebook, and X (Twitter). Lets users show off their vault highlights.
- **Dark Mode Toggle**:A built-in dark theme for night-time browsing, fitting the live music aesthetic and reducing eye strain.
- **Advanced Stats**: A calendar-based view for upcoming gigs, making it easier to see what’s coming up at a glance.
- **Calendar View**: Enable users to reply to comments, creating nested comment threads for better discussions.
- **Notifications / Reminders**: Email or dashboard notifications reminding users about upcoming gigs or anniversaries of past ones.
- **Export / Import**: IAbility to export a user’s gig history to CSV/JSON or import past gig data from external services.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new features, updates, and newsletter.
- **Analytics**: For better understanding of how the user uses the site to better future improvements.
- **Multilingual Support**: Add the ability to write and view in multiple languages, broadening the audience.
- **Mobile PWA**: Progressive Web App mode for offline access and quick “Add to Home Screen” installs on iOS/Android.
- **SEO Optimization**: Implement features for SEO, such as meta tags, custom URLs, and keywords for better search engine ranking.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, research, code logic and pair program. |

## Database Design

### Data Model

Gig Vault uses a relational schema built in PostgreSQL with models representing users, gigs, bands, venues, images, videos and genres.

![screenshot](documentation/erd.png)

 [`Mermaid flowchart`](https://mermaid.live). 
I have used `Mermaid` to generate an ERD of my project.

erDiagram
    direction TB
    User {
        int id PK
        string username
        string email
    }

    Band {
        int id PK
        string name
    }

    Venue {
        int id PK
        string venue_name
        string venue_city
        string venue_country
        string address_text "optional"
    }

    Genre {
        int id PK
        string name
    }

    GigImage {
        int id PK
        string image "Cloudinary"
        string caption "optional"
        boolean is_cover "max one per gig"
        int gig_id FK
    }

    GigVideo {
        int id PK
        string url
        datetime added_at
        int gig_id FK
        int added_by_id FK "nullable → User"
    }

    Gig {
        int id PK
        date date
        boolean is_festival
        string tour_title
        string status "upcoming / attended"
        text notes "rich text (Summernote)"
        int user_id FK
        int band_id FK "headliner"
        int venue_id FK
    }

    User ||--o{ Gig : "owns"
    Band ||--o{ Gig : "headliner"
    Venue ||--o{ Gig : "hosted at"
    Gig }o--o{ Band : "other_artists (supports)"
    Genre ||--o{ Gig : "genres"
    Gig ||--o{ GigImage : "images"
    Gig ||--o{ GigVideo : "videos"
    User ||--o{ GigVideo : "added_by (optional)"

source: [Mermaid](https://www.mermaidchart.com/app/projects/9d020117-8aa3-4abc-879e-0ce435a4ec55/diagrams/74682d3b-637b-42e9-ae1d-65b4f302a37f/version/v0.1/edit)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/runwiththerhythm/gig_vault/projects) served as an Agile management tool for this project. Through it, User Stories, issues/bugs and tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/runwiththerhythm/gig_vault/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/runwiththerhythm/gig_vault)](https://www.github.com/runwiththerhythm/gig_vault/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/runwiththerhythm/gig_vault)](https://www.github.com/runwiththerhythm/gig_vault/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://gig-vault-2fe6800a7bea.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/runwiththerhythm/gig_vault).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/runwiththerhythm/gig_vault.git`
7. Press "Enter" to create your local clone.

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/runwiththerhythm/gig_vault).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Markdown Table of Contents generator](<!-- https://github.com/ekalinin/github-markdown-toc -->) | Generate TOC for README |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

- Images
    - [Canva](https://www.canva.com)

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |

### Acknowledgements

- I would like to thank;
The [Code Institute](https://codeinstitute.net) for their learning materials and project assignment.
My Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for their support throughout development of this project.





## 🚀 Deployment

The Heritage Tomato Club is deployed to a live VPS environment using **Nginx**, **Gunicorn**, **PostgreSQL**, and **Let’s Encrypt SSL**.

### 🔗 Live Site

**[https://tomatoes.cassiterite.digital](https://tomatoes.cassiterite.digital)**

### ⚙️ Deployment Summary

The project was deployed using the following steps:

1. SSH into the VPS.
2. Clone the GitHub repository into the project directory.
3. Create and activate a Python virtual environment.
4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
6. Build Tailwind CSS and collect static files:

   ```bash
   python manage.py tailwind build
   python manage.py collectstatic --noinput
   ```
7. Configure **Gunicorn** as the application server using a systemd service.
8. Configure **Nginx** as a reverse proxy to Gunicorn and enable HTTPS via Let’s Encrypt.
9. Reload all services to complete deployment.

### 🔄 Updating the Live Server

To deploy updates:

```bash
git pull
python manage.py migrate
python manage.py tailwind build
python manage.py collectstatic --noinput
sudo systemctl restart <app-service>
```
