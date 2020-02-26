import random
import os
import requests
from flask import Flask, render_template, abort, request

from meme import generate_meme

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    
    quotes = []
    for file in quote_files:
        for quote in Ingestor.parse(file):
            quotes.append(quote)
    
    images_path = "./_data/photos/dog/"
    imgs = os.listdir(images_path)
    imgs = [images_path + item for item in imgs]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = generate_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)



@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form['image_url']
    r = requests.get(img_url)
    with open("./temp.jpg", 'wb') as f:
        f.write(r.content)
    img = "./temp.jpg"
    body = request.form['body']
    author = request.form['author']
    path = generate_meme(img, body, author)
    os.remove("./temp.jpg")
    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run()
