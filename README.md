# pyladies.github.io-src

This repository includes submodules:

- `/output`: content that builds `pyladies.github.io`
- `/pelican-plugins`: points to the main pelican-plugins repo
- `/pelican-fh5co-marble`: points to a fork of the theme fetched from [pelican-themes](http://www.pelicanthemes.com/)

## Installation

To start you'll need to:

1. Clone the repo

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

3. Install `pip -r requirements.txt`

4. Generate pelican content and serve locally with:
   ```bash
   pelican content
   pelican --listen
   ```
