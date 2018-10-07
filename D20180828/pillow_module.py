from PIL import Image

im = Image.open("/Users/cuixiaodong/Pictures/图片/IMG_0575.JPG") # type: Image.Image
print(im.format, im.size, im.mode)

im.thumbnail((240,320))

im.save("cuixd.jpg","JPEG")