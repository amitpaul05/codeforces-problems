from PIL import Image

im = Image.open('shoe.jpg')

print(im.height)
# im.resize((500, 600)).show()

new_width = 500

new_height = int((new_width / im.height) * im.width)
# print(type(new_width), type(new_height))
im = im.resize((new_width, new_height))

temp = new_height - 600

im.crop((0, temp//2, 500, new_height - temp//2)).show()
