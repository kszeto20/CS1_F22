from check2_helper import make_square
from PIL import Image

im = Image.new('RGB', (512,512), 'white')

im1 = Image.open('ca.jpg')
im2 = Image.open('im.jpg')
im3 = Image.open('hk.jpg')
im4 = Image.open('bw.jpg')

im1 = make_square(im1)
im2 = make_square(im2)
im3 = make_square(im3)
im4 = make_square(im4)

im1 = im1.resize((256,256))
im2 = im2.resize((256,256))
im3 = im3.resize((256,256))
im4 = im4.resize((256,256))

im.paste(im1, (0, 0))
im.paste(im2, (im1.width, 0))
im.paste(im3, (0, im1.width))
im.paste(im4, (im1.width, im1.height))

im.show()
