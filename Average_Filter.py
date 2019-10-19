from PIL import Image,ImageFilter

img = Image.open('Pictures/Superhero.png')
img2 = img.filter(ImageFilter.ModeFilter())

img.show()

img2.show()
