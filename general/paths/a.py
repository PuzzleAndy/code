from pathlib import Path
import os

def paths(path, ext):
	res = []
	for dirpath, dirnames, filenames in path.walk():
		for filename in filenames:
			if ext in Path(filename).suffixes:
				res.append(dirpath / filename)
	return res

print(paths(Path('1'), '.txt'))

