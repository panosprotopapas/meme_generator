## Meme Engine Module

Responsible for manipulating and drawing text onto images. 

The MemeEngine class is responsible for:
1. loading an image using Pillow (PIL)
2. resizing the image so the width is at most 500px and the height is scaled proportionally
3. add a quote body and a quote author to the image
4. saving the manipulated image

The class must implements the instance method `make_meme`  which returns the path to the manipulated image.

```python
make_meme(self, img_path, text, author, width=500) -> str
```