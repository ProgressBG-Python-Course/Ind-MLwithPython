# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Print only the positive (i.e. > 0) even numbers from a given list
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# given
numbers = [2, -4, -3, 13, 8, -6, 4] 

# your code goes below:
for n in numbers:
	if n>0 and n%2==0:
		print(n)

# expected output:
# 2 
# 8 
# 4