import math

def deg2rad(theta):
	return theta * math.pi / 180

def rad2deg(theta):
	return theta * 180 / math.pi

def norm_angle(theta):
	return theta - math.tau * math.floor(theta / math.tau)

print(deg2rad(-90))
print(rad2deg(-math.pi / 2))
print(norm_angle(-math.pi / 2))