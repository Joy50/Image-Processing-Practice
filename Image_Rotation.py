from PIL import Image

im = Image.open('Pictures/Superhero.png')

im = im.rotate(180)

im.show()
