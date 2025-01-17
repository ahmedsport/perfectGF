import glob
import imagehash
from PIL import Image

my_img_url = './boys/me.jpg'
my_hash = imagehash.average_hash(Image.open(my_img_url))

girls = glob.glob('./girls/*.jpg')
selected = girls[0]
accepted_diff = 50

print(girls)
for girl in girls:
    girl_hash = imagehash.average_hash(Image.open(girl))
    diff = girl_hash - my_hash
    if diff < accepted_diff:
        selected = girl
        accepted_diff = diff


bf_img = Image.open(my_img_url)
gf_img = Image.open(selected)
couple_img = Image.new('RGB', (bf_img.width + gf_img.width, bf_img.height))
couple_img.paste(bf_img, (0, 0))
couple_img.paste(gf_img, (bf_img.width, 0))
couple_img.show()
