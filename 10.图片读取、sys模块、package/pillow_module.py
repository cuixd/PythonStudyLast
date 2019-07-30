from PIL import Image

im = Image.open("/PycharmProjects/PythonStudy/10.图片读取、sys模块、package/cuixd.jpg")  # type: Image.Image
print(im.format, im.size, im.mode)

im.thumbnail((240, 320))

im.save("cuixd_1.jpg", "JPEG")
