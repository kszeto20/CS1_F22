from PIL import Image

def make_square(ima):
    w = ima.width
    h = ima.height
    
    if (w > h):
        return ima.crop((0, 0, h, h))
    elif (h > w):
        return ima.crop((0, 0, w, w))
    else:
        return ima.crop((0, 0, 256, 256))

im = Image.open('1.jpg')

imsquare = make_square(im)
imsquare.show()