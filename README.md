# PyLadies Elections Website Source 

The PyLadies Election page is a Python 3 pelican powered website. This repository includes the pelican theme and code to generate the static files that are served via the pyladies.github.io/elections GitHub project page.

## Organization

This repository includes the following submodules:

- `/pelican-plugins`: points to the main pelican-plugins repo
- `/pelican-fh5co-marble`: points to a fork of the theme fetched from [pelican-themes](http://www.pelicanthemes.com/)

Additionally the repository includes the following:

- `/output`: content that is served on the `elections.pyladies.com` via GitHub actions on the `gh-pages` branch (see `.github/workflows/build_deploy.yml`)

## Installation

To start you'll need to:

1. Clone the repo:

   - If you have git 2.11+:
     ```bash
     git clone --recurse-submodules https://github.com/pyladies/pyladies-elections-website
     ```
   - Otherwise run:
     ```bash
     git clone --recursive https://github.com/pyladies/pyladies-elections-website
     ```

2. Setup and activate a virtual environment:
   ```bash
   python3 -m venv .ENV
   source .ENV/bin/activate
   ```

3. Install `pip install -r requirements.txt`.

4. Generate pelican content and serve locally with:

   ```bash
   pelican content
   pelican --listen
   ```

   Alternatively, you can use `make` instead of Pelican commands:

   ```bash
   make html
   make serve
   ```

## Updating elections.pyladies.com

Whenever a push action is issued again `main` GitHub Actions will run the `build_deploy.yml` workflow to:

- Checkout the submodules with the pelican theme (`/pelican-fh5co-marble`) and plugin (`/pelican-fh5co-marble`)
- Install the `requirements.txt`
- Run `pelican content` to repopulate `/output`
- Push `/ouput` to `gh-pages` to host the content via GitHub pages

Navigate to elections.pyladies.com to confirm the changes are live. 

## Working with submodules: Syncing the theme and plugin submodules with elections.pyladies.com

### Confirm the submodules

```bash
$ git submodule
$ 700eb3b435f18ef0ca9b7bdf7f8ca0a3d59f2e46 pelican-fh5co-marble (v1.0.1-25-g700eb3b)
$ f191788fe0bf3cae54f22b5b447dd23b8d32364e pelican-plugins (heads/master)
```

This confirms the latest commit the repository has checked out for each of the submodules: the theme (`pelican-fh5co-marble`) as well as the plugins (`pelican-plugins`).

### Init the submodules if missing

Example of initializing the `/pelican-fh5co-marble` submodule:

1. `cd /pelican-fh5co-marble`
2. Confirm `git remote -v` points to proper repo
  
  ```bash
  git remote -v 
  origin	https://github.com/pyladies/pelican-fh5co-marble (fetch)
  origin	https://github.com/pyladies/pelican-fh5co-marble (push)
  ```

  If the submodule remote doesn't exist:

  ```bash
  git submodule update  --init 
  ```

### Update the submodule after changes made

The workflow is the same as working in a standard repository, if updating the `pelican-fh5co-marble` submodule:

```bash
$ cd /pelican-fh5co-marble
$ git status
$ git add <FILES_CHANGED>
$ git commit -m "Meaningful message"
$ git push origin main
$ cd ../
$ git add pelican-fh5co-marble
$ git commit -m "Updated submodule"
$ git push origin feature_branch
```

## Localizing the website

To add additional languages in the website the following changes are required:

1. `pelicanconf.py`

- `I18N_SUBSITES` dict with a key representing the 2 character language code (e.g. `es` for espanol) and specify:
  - `PAGE_PATHS` this is the route that will be generated for the content pages e.g. `localhost:8000/pages/es`
  - `ARTICLE_PATHS` this is the route that will be generated for the articles e.g. `localhost:8000/blog/es`
  - `LOCALE` with the two language character code and country e.g. `es_ES` 
- `HERO` list of image dicts:
  - `title` of each image with the same 2 character language code e.g. `es` for espanol
  - `links` list of each `text` key with the same 2 character language code e.g. `es` for espanol

2. Add your markdown pages into `content/pages/<LANGUAGE CHARACTER CODE>`. 

3. Each page should include the following metadata, `Title`, `Order`, `Date`, `Icon`, `Summary`, `Lang`, `Slug`. Here is an example the Aplica page in Spanish:

```
Title: Aplica
Order: 5
Date: 2020-04-09 10:30
Icon: icon-link2
Summary: Cómo convertirse en miembro del Consejo Global de PyLadies
Lang: es
Slug: aplica
```
