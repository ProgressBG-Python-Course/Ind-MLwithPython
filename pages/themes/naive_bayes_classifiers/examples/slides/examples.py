def virus_test():
	# given
	p_virus = 0.01
	p_test_positive_given_virus = 0.9
	p_test_positive_given_non_virus = 0.05

	# calculate from given:
	p_test_positive = p_virus * p_test_positive_given_virus + (1 - p_virus) * p_test_positive_given_non_virus
	# (0.01*0.9) / ( 0.01*0.9  + (1-0.01)*0.05)

	# calculate p(virus|tests_positive):
	p_virus_given_test_positive = (p_virus * p_test_positive_given_virus)/p_test_positive


	print(p_virus_given_test_positive)


def fire_when_smoke():
	# given
	p_fire = 0.01
	p_smoke = 0.1
	p_smoke_fire = 0.9

	# find: p_fire_smoke
	p_fire_smoke = (p_fire * p_smoke_fire) / p_smoke

	print(p_fire_smoke)


def smkoker_cancer():
	# given
	# 5% имат рак
	# 100% от тези, които имат рак са пушачи
	# 20% от тези, които нямат рак са пушачи





