# License: CC0
# https://puzzleandy.com

def convert(old_val, old_min, old_max, new_min, new_max):
	return new_min + (new_max - new_min) * ((old_val - old_min) / (old_max - old_min))

print(convert(8, 0, 10, 0, 1))