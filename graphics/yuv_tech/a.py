# License: CC0
# https://puzzleandy.com

def rgb_to_yuv(R, G, B):
	Y = 0.299 * R + 0.587 * G + 0.114 * B
	U = 0.492 * (B - Y)
	V = 0.877 * (R - Y)
	return Y, U, V

def yuv_to_rgb(Y, U, V):
	R = Y + 1.14 * V
	G = Y - 0.395 * U - 0.581 * V
	B = Y + 2.033 * U
	return (R, G, B)

R, G, B = 1, 0, 0
Y, U, V = rgb_to_yuv(R, G, B)
print(Y, U, V)
R, G, B = yuv_to_rgb(Y, U, V)
print(R, G, B)