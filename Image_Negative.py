from PIL import Image
import PIL.ImageOps as ops

img = Image.open('Pictures/Superhero.png')

inv_img = ops.invert(img)

inv_img.show()
