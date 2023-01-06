# Test Algorithm, time checks
import random

class AlgoTest:
	def __init__(self):
		print("TEST_ALGO LOADED")

	def get_move(self):
		x = 0
		loop_size = [1,50,1000,50000]
		for _ in range(random.choice(loop_size)):
			x += 1
		print(x)
		print("RETURN GRID")
		return self.grid

