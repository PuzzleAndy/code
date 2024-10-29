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

paths = paths(Path('luts'), '.cube')
Path('out').mkdir(exist_ok=True)
for path in paths:
	try:
		lut = load_cube_file(str(path))
	except Exception as e:
		print('Invalid LUT:', path)
	im = Image.open('woman.jpg')
	im.filter(lut).save(Path('out') / path.with_suffix('.png').name)