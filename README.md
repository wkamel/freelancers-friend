# Freelancer's Friend
### List of Python offers from sites like freelancer.com, guru.com and others

## How it works?

### 1. Downloader/scraper
The script written in Python.
It downloads *Python* offers from many sources in many formats, i.e.:
* **freelancer.com** - *JSON* data are used 
* **guru.com** - *RSS*(in fact *Atom*) - XML parsing is used 
* **others** ... in progress

### 2. Viewer 
Simple application for showing list of offers.
It is written in Python with *Flask* framework and Jinja2 templates engine.
Frontend is based on *Bootstrap*.

## Demo

This script was hosted on heroku, but now it's inactive.
If you would like to test it find me [on my webpage](https://softarm.pl).

## Testing

For now:
python -m unittest discover -s tests -p "*_test.py"
