from PIL import Image, ImageDraw, ImageFont
from random import randint

class MemeEngine():
    def __init__(self, output_dir):
            self.output_dir = output_dir
            
    
    def make_meme(self, img_path, text, author, width=500):

        img = Image.open(img_path)
        
        # Resize image
        if width > 500:
            width = 500
        multiplier = width/img.width
        new_width = int(img.width*multiplier)
        new_height = int(img.height*multiplier)
        img = img.resize((new_width,new_height))
        
        # Add message
        message = text + "\n - "+author
        draw = ImageDraw.ImageDraw(img)
        random_width = randint(0, new_width)
        random_height = randint(0, new_height)
        draw.text((random_width, random_height), message)

        # Save
        img.save(self.output_dir)
        return(self.output_dir)
    