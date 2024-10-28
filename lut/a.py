from PIL import Image
from pillow_lut import load_cube_file

lut = load_cube_file('pop_it.cube')
im = Image.open('woman.jpg')
im.filter(lut).save('out.jpg')