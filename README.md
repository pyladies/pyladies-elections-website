# PyLadies Elections Website Source 

The PyLadies Election page is a Python 3 pelican powered website. This repository includes the pelican theme and code to generate the static files that are served via the pyladies.github.io/elections GitHub project page.

## Organization

This repository includes the following submodules:

- `/output`: content that builds `pyladies.github.io` and serves on custom subdomain `elections.pyladies.com`
- `/pelican-plugins`: points to the main pelican-plugins repo
- `/pelican-fh5co-marble`: points to a fork of the theme fetched from [pelican-themes](http://www.pelicanthemes.com/)

## Installation

To start you'll need to:

1. Clone the repo:

   - If you have git 2.11+:
     ```bash
     git clone --recurse-submodules https://github.com/pyladies/pyladies.github.io-src
     ```
   - Otherwise run:
     ```bash
     git clone --recursive https://github.com/pyladies/pyladies.github.io-src
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

## Working with submodules: Syncing the `content` submodule with elections.pyladies.com

After generating the static files with either `pelican content` or `make html` you will need to push changes to the Election GitHub page repo:

1. `cd /output`
2. Confirm remote -v points to Election GitHub page repo:
  
  ```bash
  git remote -v 
  origin  https://github.com/pyladies/pyladies.github.io.git (fetch)
  origin  https://github.com/pyladies/pyladies.github.io.git (push)
  ```

  If the submodule remote doesn't exist:

  ```bash
  git submodule update  --init 
  ```

  Confirm that the remote is properly set, if so recreate the static files with either `pelican content` or `make html`. Confirm the `CNAME` file exists in `/output` with `elections.pyladies.com`  as well.
3. Push content to the  Election GitHub page :
   ```bash
   git status
   git add <files>
   git  commit -m "Meaningful message"
   git push origin master
   ```

   Navigate to elections.pyladies.com to confirm pages are live. 
