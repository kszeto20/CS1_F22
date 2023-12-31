from PIL import Image
im = Image.new('RGB', (512,512), 'white')

im1 = Image.open('ca.jpg')
im2 = Image.open('im.jpg')
im3 = Image.open('hk.jpg')
im4 = Image.open('bw.jpg')

im1 = im1.resize((256,256))
im2 = im2.resize((256,256))
im3 = im3.resize((256,256))
im4 = im4.resize((256,256))

im.paste(im1, (0,0))
im.paste(im2, (256, 0))
im.paste(im3, (0, 256))
im.paste(im4, (256, 256))

im.show()
