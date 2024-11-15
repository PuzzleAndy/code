import math
import numpy as np

def linear_srgb_to_oklab(RGB):

	l = 0.4122214708 * RGB[0] + 0.5363325363 * RGB[1] + 0.0514459929 * RGB[2]
	m = 0.2119034982 * RGB[0] + 0.6806995451 * RGB[1] + 0.1073969566 * RGB[2]
	s = 0.0883024619 * RGB[0] + 0.2817188376 * RGB[1] + 0.6299787005 * RGB[2]

	l_ = math.cbrt(l)
	m_ = math.cbrt(m)
	s_ = math.cbrt(s)

	return np.array([
		0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
		1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
		0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
	], np.float32)

def oklab_to_linear_srgb(Oklab):

	l_ = Oklab[0] + 0.3963377774 * Oklab[1] + 0.2158037573 * Oklab[2]
	m_ = Oklab[0] - 0.1055613458 * Oklab[1] - 0.0638541728 * Oklab[2]
	s_ = Oklab[0] - 0.0894841775 * Oklab[1] - 1.2914855480 * Oklab[2]

	l = l_ * l_ * l_
	m = m_ * m_ * m_
	s = s_ * s_ * s_

	return np.array([
		+4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
		-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
		-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
	], np.float32)

sRGB = np.array([1, 1, 1], np.float32)
Oklab = linear_srgb_to_oklab(sRGB)
print(Oklab)
sRGB = oklab_to_linear_srgb(Oklab)
print(sRGB)