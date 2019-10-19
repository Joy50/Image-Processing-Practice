from PIL import Image,ImageFilter

img = Image.open('Pictures/Superhero.png')
img2 = img.filter(ImageFilter.MedianFilter())

img.show()

img2.show()
