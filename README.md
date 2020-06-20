# pyladies.github.io-src

This repository includes three submodules:

- `/output`: content that builds `pyladies.github.io`
- `/pelican-plugins`: points to the main pelican-plugins repo
- `/pelican-fh5co-marble`: points to a fork of the theme fetched from [pelican-themes](http://www.pelicanthemes.com/)

## Installation

To start you'll need to:

1. Clone the repo

	- If you have git 2.11+: `git clone --recurse-submodules https://github.com/pyladies/pyladies.github.io-src  `
	- Otherwise use this: `git clone --recursive https://github.com/pyladies/pyladies.github.io-src   `

2. Setup a `virtualenv`

3. Install `pip -r requirements.txt`