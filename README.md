# [Heritage Tomato Club](https://tomatoes.cassiterite.digital)

Developer: ([runwiththerhythm](https://www.github.com/runwiththerhythm))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club)
[![badge](https://img.shields.io/badge/deployment-VPS-purple)](https://tomatoes.cassiterite.digital)

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

#### Colour Palette

The Heritage Tomato Club colour palette takes inspiration from vintage seed packets, garden twine, soil, and the natural colours found in tomato plants.  
Each hue contributes to a warm, earthy, accessible aesthetic that supports the brand identity.

⬛ **Dark Soil — `#1D1D1B`**  
The deepest tone in the palette, inspired by rich garden soil and vintage ink.  
Used for headings, body text, and strong contrast elements.

🟩 **Vine Green — `#355E3B`**  
A classic tomato-vine green offering balance and an organic feel.  
Used for accents, badges, and supportive UI components.

⬜ **Seed Packet Cream — `#F6F1E8`**  
A warm, parchment-like neutral echoing traditional seed envelopes.  
Used for page backgrounds and high-readability surfaces.

🟥 **Pomodoro Red — `#C3423F`**  
A ripe tomato red used for buttons, calls-to-action, and key highlights.  
Warm and inviting without overwhelming the interface.

🟧 **Heirloom Orange — `#D96F3B`**  
Reflecting the colour of heritage varieties such as *Orange Banana* and *Valencia*.  
Used for warm accents and secondary emphasis elements.

🟨 **Golden Seed Yellow — `#D6A84B`**  
Inspired by dried tomato seeds and aged paper.  
Used for highlights, decorative touches, and gentle emphasis.

Together, these colours create a vintage-inspired, horticulturally grounded palette that enhances readability, brand warmth, and accessibility.

### Typography

- The typography choices for the Heritage Tomato Club were selected to evoke the feel of vintage seed packets, traditional gardening guides, and classic printed ephemera — all while maintaining clear readability across devices.

**<span style="color:#C3423F;font-weight:700;">Headings — [Bitter](https://fonts.google.com/specimen/Bitter/) (Serif)</span>**  
Bitter provides a strong, traditional serif style that feels rooted in heritage print design. Its sturdy letterforms pair well with the gardening theme while remaining highly readable on screens.  
Used for: all headings (H1–H6), key section titles, and feature highlights.

**<span style="color:#355E3B;font-weight:700;">Body Text — [Lora](https://fonts.google.com/specimen/Lora/) (Serif)</span>**  
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
| As a first-time visitor, | I can view information about the Heritage Tomato Club without registering, | so that I can decide whether I want to join. |
| As a first-time visitor, | I can easily navigate the site, | so that I can find seed varieties, resources, and membership information quickly. |
| As a new user, | I can register for an account, | so that I can access member features. |
| As a registered user, | I can log in securely, | so that I can access my profile and member-only content. |
| As a logged-in user, | I can log out of my account, | so that my session ends securely. |
| As a user who forgot my password, | I can reset my password via email, | so that I can regain access to my account. |
| As a visitor or member, | I can view a friendly error page if I reach a broken link, | so that I am not confused or lost. |
| As a visitor, | I can browse the Seed Library, | so that I can learn about different heritage tomato varieties. |
| As a user, | I can view detailed information about a tomato variety, | so that I can understand its growth habit, origin, and characteristics. |
| As a logged-in user, | I can purchase a membership tier, | so that I can support the club and access additional features. |
| As a logged-in member, | I can manage my membership status, | so that I know whether my membership is active. |
| As a logged-in user, | I can create a grow diary entry, | so that I can record the progress of my tomato plants. |
| As a logged-in user, | I can edit a grow diary entry, | so that I can update notes or growth stages. |
| As a logged-in user, | I can delete a grow diary entry, | so that I can remove incorrect or unwanted records. |
| As a logged-in user, | I can upload photos to my grow diary entries, | so that I can visually document plant development. |
| As a user, | I can browse tomato recipes, | so that I can find ideas for using harvested tomatoes. |
| As a visitor, | I can sign up to the newsletter, | so that I can receive club updates and news. |
## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register / Login / Logout | Handled by Django Allauth, allowing users to create secure accounts, log in, and log out. | ![screenshot](documentation/features/auth.png) |
| Membership Tiers | Users can view available membership tiers, including free and paid options, with clear descriptions and pricing. | ![screenshot](documentation/features/membership-tiers.png) |
| Stripe Checkout | Paid memberships are processed securely using Stripe Checkout. Users are redirected to a confirmation page on success. | ![screenshot](documentation/features/stripe-checkout.png) |
| Membership Status | Logged-in users can see whether their membership is active and which tier they belong to. | ![screenshot](documentation/features/membership-status.png) |
| Seed Library | Publicly accessible list of heritage tomato varieties with clean, card-based layout. | ![screenshot](documentation/features/seed-library.png) |
| Variety Detail Pages | Each tomato variety has a dedicated page showing images, origin, growth habit, and descriptive notes. | ![screenshot](documentation/features/variety-detail.png) |
| Filtering & Sorting | Users can filter tomato varieties by traits such as growth habit and colour, and sort alphabetically. | ![screenshot](documentation/features/filters.png) |
| Grow Diary | Logged-in users can record the progress of their tomato plants through diary entries. | ![screenshot](documentation/features/grow-diary.png) |
| Add Diary Entry | Users can create diary entries with growth stage, date, notes, and optional photo upload (Cloudinary). | ![screenshot](documentation/features/add-diary.png) |
| Edit / Delete Diary Entries | Users have full control to update or remove their own grow diary entries. | ![screenshot](documentation/features/edit-diary.png) |
| Recipes | Users can browse tomato-based recipes, including prep time, difficulty, and suitability for gluts. | ![screenshot](documentation/features/recipes.png) |
| Newsletter Signup | Visitors can subscribe to the newsletter to receive updates from the club. | ![screenshot](documentation/features/newsletter.png) |
| Feedback Messages | Django messages framework provides clear feedback for actions such as form submissions and membership changes. | ![screenshot](documentation/features/messages.png) |
| Custom Error Pages | Friendly 404 and 500 error pages are provided to maintain a consistent user experience. | ![screenshot](documentation/features/404.png) |
| Responsive Design | The site is fully responsive and optimised for mobile, tablet, and desktop devices. | ![screenshot](documentation/features/responsive.png) |

### Future Features

- **Seed Swapping**: Allow members to request and exchange seeds with other club members.
- **Advanced Grow Diary Insights**: Visual timelines and summaries showing plant progress over time.
- **Member-Only Recipes**: Restrict certain premium recipes to paid membership tiers.
- **Events & Meetups**: Promote seed swaps, talks, and local gardening events.
- **Notifications**: Email reminders for diary updates, seasonal tips, or membership renewal.
- **Search**: Full-text search across seed varieties, diary entries, and recipes.
- **Admin Analytics**: Insights into popular varieties, active members, and site usage.
- **Accessibility Enhancements**: Continued improvements toward WCAG AAA compliance.

## Tools & Technologies

### Technologies Used

| Tool / Tech | Use |
| --- | --- |
| ![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000) | Generate README and TESTING templates. |
| ![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717) | Version control and remote code storage. |
| ![badge](https://img.shields.io/badge/HTML5-grey?logo=html5&logoColor=E34F26) | Structure and semantic layout of the site. |
| ![badge](https://img.shields.io/badge/CSS3-grey?logo=css3&logoColor=1572B6) | Basic styling before Tailwind processing. |
| ![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E) | Interactive front-end behaviour (filters, form enhancement). |
| ![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB) | Core back-end programming for Django. |
| ![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20) | The main web framework powering the application. |
| ![badge](https://img.shields.io/badge/Django_Allauth-grey?logo=django&logoColor=092E20) | User authentication (signup, login, logout). |
| ![badge](https://img.shields.io/badge/Tailwind_CSS-grey?logo=tailwindcss&logoColor=06B6D4) | Utility-first CSS framework for styling, integrated via Tailwind CLI. |
| ![badge](https://img.shields.io/badge/DaisyUI-grey?logo=daisyui&logoColor=FF9900) | Tailwind component library providing accessible UI components and theming. |
| ![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=626CD9) | Secure payment processing for membership tiers. |
| ![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5) | Media storage for tomato variety images. |
| ![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF) | Serving static files in production (with Django). |
| ![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1) | Relational database used for production deployments. |
| ![badge](https://img.shields.io/badge/VPS-grey?logo=linux&logoColor=FCC624) | Production hosting environment (Hostinger VPS). |
| ![badge](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC) | Wireframing and visual planning. |
| ![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7) | Iconography across the site. |
| ![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C) | Assistance with debugging, research, content drafting, and pair programming. |


## Database Design

### Data Model

Heritage Tomato Club uses a relational schema built in PostgreSQL with models representing users, membership, profile, tomato variety, recipe, grow diary and newsletter.

![screenshot](documentation/erd.png)

 [`Mermaid flowchart`](https://mermaid.live). 
I have used `Mermaid` to generate an ERD of my project.

---
config:
  theme: forest
---
erDiagram
    User {
      int id PK
      string username
      string email
    }

    Profile {
      int id PK
      int user_id FK
      string display_name
      string location
      string favourite_tomato
      string avatar        "Cloudinary"
    }

    MembershipTier {
      int id PK
      string slug          "unique"
      string name
      decimal price_per_year
      boolean is_active
      int sort_order
      string short_tagline
      text feature_list    "one feature per line"
      string stripe_price_id  "Stripe Price (price_...)"
    }

    Membership {
      int id PK
      int user_id FK       "OneToOne -> User"
      int tier_id FK       "MembershipTier"
      string stripe_subscription_id "sub_... (optional)"
      boolean active
      datetime started_at
    }

    NewsletterSubscriber {
      int id PK
      string email         "unique"
      datetime date_joined
    }

    TomatoVariety {
      int id PK
      string name          "unique"
      string slug          "unique"
      string image         "ImageField (Cloudinary storage)"
      string origin        "optional"
      string growth_habit  "choice"
      smallint days_to_maturity "optional"
      string fruit_color   "optional"
      text description     "optional"
      boolean is_featured
      boolean is_active
      datetime created_at
      datetime updated_at
    }

    GrowDiaryEntry {
      int id PK
      int user_id FK
      int variety_id FK    "TomatoVariety"
      date date
      string stage         "choice (sown/harvest/etc.)"
      string title         "optional"
      text notes           "optional"
      string photo         "Cloudinary (optional)"
      datetime created_at
      datetime updated_at
    }

    Recipe {
      int id PK
      string title
      string slug          "unique"
      text intro
      text ingredients     "one per line"
      text instructions
      int prep_time_minutes    "optional"
      int cook_time_minutes    "optional"
      int serves              "optional"
      string difficulty        "easy/medium/advanced"
      boolean is_freezer_friendly
      boolean is_good_for_gluts
      string image             "ImageField (optional)"
      datetime created
      datetime updated
    }
    User ||--|| Profile : "has profile"
    User ||--|| Membership : "has membership"
    MembershipTier ||--o{ Membership : "tiers"
    User ||--o{ GrowDiaryEntry : "logs entries"
    TomatoVariety ||--o{ GrowDiaryEntry : "diary entries"

source: [Mermaid](https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=toggle#pako:eNqlVktz0zAQ_iuanNpD0nsOXIAyDAN0aOGUGY9ire0FWWukdYpp-99ZOfUjzqPpkIMjr77Vvr5d-WGWkoHZcjafz1cuJZdhvlw5pbiAEpYqIw-BV67dBv8Ode51GQFKfQ_g1cN2rRQ6VmjUzadOENijy1UtKKdLmIih1Gi3sqeV2y5uPGVo4cSZURAPTER6PbVkMFRWN8kBa5ZSzUhuIs70hmqPDAlTqZkm23qjWXv1_FvN3lqqDTrtm9Vs4vpnKNfgQ4HVHZ6TlWDrXKnh6Nrh7xq6Y3vYOBQDKZbaqspjCkklSWhA-253TWRBO4Uh0SnjBsYeBPKckDfgp24UcYd1btH1Ggx_WGWgufaQWAy8dZEcdFIl1lWrMnU4_lXiXeujBC56t61IiisidbHdWSwWlydyeDYD-vx9dXBH8lDzNy0vB8eiAuOewm7BjsUR6nVIZRW5Ew9YzUQSvVcX1Aq1vRx0uxrsFsBoBsYS5EztGUyieRL4F7gPFpjB327trc-hUNtBJyjU242L5CdJuczE8F3L-h_aI3DzssXIxjNIeya3hcw5jGAf4_s1gjXqYug0QZOXjcs9ffKYoxv0u4LsAXNP91wkhV4jR2BakHBwBJOusjFmo5sgkyApI8lRMnLi0MzXyElKlvwR620bGej5c9TNUes-95d5sav74qZeVEakGm3VldEH-fZBEiKT3DfvHfvm1eM2SjdbzgxNtZrtkGmXhu1jr8N2y7-tiroIdO-uCu03cu9cAaeL_cozsh2rHsm9I4aglDqDIlVBTOrQpD_Y6P-V_W8yxyt4udvaKF_ZWm3ccqCniSQXUiE4DmoY5vtD_Bksxuo0Bh3GPlYeqiSGlpTo6ufUHsppBKdEv84GC8M2O5U6XSyDWYZpbaVBezDo0FyVEmNdXmmz0S6VJjrYYR7grzA6E5o6Y5sDkJzIJPLhk-S25nByau1PrjPYcowqPU_6j6vHx_n88bH_LlqKrUIHqUT73lkYQ0d3aIcue1GnMPlYiar0MFWNd2bYMyG4yfSIWEt5UMIuyWmvsnu3HNc18XVQnj39A_kyV8s)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/runwiththerhythm/tomato-club/projects) served as an Agile management tool for this project. Through it, User Stories, issues/bugs and tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/runwiththerhythm/tomato-club/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/runwiththerhythm/tomato-club)](https://www.github.com/runwiththerhythm/tomato-club/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [VPS](https://tomatoes.cassiterite.digital).

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a PostgreSQLfor the Relational Database with Django.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live site.

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

1. Go to the [GitHub repository](https://www.github.com/runwiththerhythm/tomato-club).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/runwiththerhythm/tomato-club.git`
7. Press "Enter" to create your local clone.

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/runwiththerhythm/tomato-club).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content


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
