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
lut = load_cube_file('moto_makusudi_ksouth.cube')
for path in paths(Path('images'), '.jpg'):
	try:
		img = Image.open(str(path))
		img.filter(lut).save(Path('out') / path.name)
	except Exception as e:
		print(e)