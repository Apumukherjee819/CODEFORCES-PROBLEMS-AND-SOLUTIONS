import math
def FindMinArea():
	points = [tuple(map(float, input().split())) for _ in range(3)]

	(x1, y1), (x2, y2), (x3, y3) = points

	# Side lengths
	a = math.hypot(x2 - x3, y2 - y3)
	b = math.hypot(x1 - x3, y1 - y3)
	c = math.hypot(x1 - x2, y1 - y2)

	# Triangle area
	area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

	# Circumradius
	try:
		R = a * b * c / (4 * area)
	except ZeroDivisionError:
		print("The area becomes zero can;t find the answer...")
		return 0

	# Central angles
	A = 2 * math.asin(a / (2 * R))
	B = 2 * math.asin(b / (2 * R))
	C = 2 * math.asin(c / (2 * R))

	eps = 1e-6

	def ok(n):
		step = 2 * math.pi / n
		for ang in (A, B, C):
			if abs(ang / step - round(ang / step)) > eps:
				return False
		return True

	for n in range(3, 101):
		if ok(n):
			ans = 0.5 * n * R * R * math.sin(2 * math.pi / n)
			print(f"{ans:.10f}")
			break
	return 0
		
		
FindMinArea()

