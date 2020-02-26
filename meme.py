import os
import random
import argparse
from random import randint

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, Quote

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given a path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = Quote(body, author)

    meme = MemeEngine(f'./static/{random.randint(0,100000000)}.png')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse. ArgumentParser(description= "Meme creation tool. If not image is provided a random one will be used. If not (text) body & author are provided, random ones will be used. Notice that if body is provided then an author is required as well, and vice-versa.")
    parser.add_argument('--body', type=str, default=None, help="The quote to be used")
    parser.add_argument('--author', type=str, default=None, help="The quote's author")       
    parser.add_argument('--path', type=str, default=None, help="The path to the image that is to be used")    
    
    args = parser.parse_args()
    
    parser = argparse.ArgumentParser(description='Process some integers.') 
    print(generate_meme(args.path, args.body, args.author))
