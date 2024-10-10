def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	
	current_savings = 0
	r = 0.05
	monthly_salary = yearly_salary / 12
	months = 0
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	
	while current_savings < down_payment:
	    current_savings += monthly_salary * portion_saved
	    current_savings += current_savings * r / 12
	    months += 1
	    if months % 6 == 0:
	        monthly_salary += monthly_salary * semi_annual_raise
	
	print("Number of months:", months)
	return months