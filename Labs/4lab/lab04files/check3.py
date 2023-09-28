from PIL import Image

def resizer(ima):
    w = ima.width
    h = ima.height
    rat = w/h
    print(rat * 256)
    return ima.resize((int(rat * 256), 256))

im = Image.new('RGB', (1082, 360), 'white')

im1 = Image.open('ca.jpg')
print('image width', str(im1.width), 'image size', str(im1.size))
im2 = Image.open('im.jpg')
im3 = Image.open('hk.jpg')
im4 = Image.open('bw.jpg')
im5 = Image.open('hw.jpg')
im6 = Image.open('tr.jpg')


im1 = resizer(im1)
im2 = resizer(im2)
im3 = resizer(im3)
im4 = resizer(im4)
im5 = resizer(im5)
im6 = resizer(im6)

orig = 31
im.paste(im1, (orig, 20))
im.paste(im2, (orig + 10 + im1.width, 60))
im.paste(im3, (orig + 20 + im2.width + im1.width, 20))
im.paste(im4, (orig + 30 + im3.width + im2.width + im1.width, 60))
im.paste(im5, (orig + 40 + im4.width + im3.width + im2.width + im1.width, 20))
im.paste(im6, (orig + 50 + im5.width + im4.width + im3.width + im2.width + im1.width, 60))

im.show()
