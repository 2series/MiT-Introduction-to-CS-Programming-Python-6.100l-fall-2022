def part_c(initial_deposit):
	house_cost = 800000
	down_payment = house_cost * 0.25
	months = 36

	def calculate_savings(r):
		return initial_deposit * (1 + r/12)**months

	if initial_deposit >= down_payment - 100:
		r = 0.0
		steps = 0
	elif calculate_savings(1.0) < down_payment - 100:
		r = None
		steps = 0
	else:
		low = 0.0
		high = 1.0
		steps = 0
		while True:
			steps += 1
			r = (low + high) / 2
			savings = calculate_savings(r)
			if down_payment - 100 < savings < down_payment + 100:
				break
			elif savings < down_payment:
				low = r
			else:
				high = r

	return r, steps