from PIL import Image
from pillow_lut import load_cube_file

lut = load_cube_file('pop_it.cube')
img = Image.open('woman.jpg')
img.filter(lut).save('out.jpg')