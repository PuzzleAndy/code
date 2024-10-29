from PIL import Image
from pillow_lut import load_cube_file
from pathlib import Path
import os

def paths(path, ext):
	res = []
	for dirpath, dirnames, filenames in path.walk():
		for filename in filenames:
			if ext in Path(filename).suffixes:
				res.append(dirpath / filename)
	return res

Path('out').mkdir(exist_ok=True)
img = Image.open('woman.jpg')
for path in paths(Path('luts'), '.cube'):
	try:
		lut = load_cube_file(str(path))
		img.filter(lut).save(Path('out') / path.with_suffix('.png').name)
	except Exception as e:
		print(e)