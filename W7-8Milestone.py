from PIL import Image

photo = Image.open("beach.jpg")
photo2 = Image.open("cactus.jpg")

print(photo.format)

combine_image = Image.new('RGB',photo.size)
(width, height) = photo.size
print(f'Photo Width: {width}')
print(f'Photo Height: {height}')

(width, height) = photo2.size
print(f'Photo2 Width: {width}')
print(f'Photo2 Height: {height}')

combine_image = Image.new('RGB', photo2.size)
combine_pixels = combine_image.load()

pixels_photo = photo.load()
pixels_photo2 = photo2.load()

r_p2, g_p2, b_p2 = pixels_photo2[10, 10]

for x in range(0, 800):
    for y in range(0, 600):
        r, g, b = pixels_photo2[x, y]
        r_p, g_p, b_p = pixels_photo[x, y]
        if r < r_p2 + 60 and g > g_p2 - 60 and b < b_p2 + 60:
            combine_pixels[x, y] = (r_p, g_p, b_p)
        else:
            combine_pixels[x,y] = (r, g, b)

combine_image.show()
#combine_image.save('cactus_on_beach.jpg')