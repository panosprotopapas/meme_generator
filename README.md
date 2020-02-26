# Motivational Puppy Meme Generator

## Udacity - Intermediate Python Nanodegree

A multimedia application to dynamically generate memes, including an image with an overlaid quote. There are two ways to use this app.

### 1. Command Line Interface tool

The utility can be run from the terminal by invoking `python3 meme.py`. The script must take three _optional_ CLI arguments:

- `--body` a string quote body
- `--author` a string quote author
- `--path` an image path

The script returns a the path to the generated image.

If any argument is not defined, a random selection is used.

### 2. Flask app

To run the utility first enter in terminal: `export FLASK_APP=app.py` then after having navigated to the folder containing `app.py` enter in terminal `flask run`.Finally, open a web-browser and navigate to http://127.0.0.1:5000/

To quit the flask app, hit Ctrl + C in the terminal.