print('''

This is a simple Price Comparison App

Please be sure to use the same unit of measurement for weights.

eg: compare oz to oz, lb to lb, ect

''')

def main():	
	itemA = float(input("Enter price of item A:\n$"))/float(input("Enter weight of item A:\n"))
	
	itemB =float(input("Enter price of item B:\n$"))/float(input("Enter weight of item B:\n"))
	
	unit = input('Enter the unit of measurement you are comparing\neg: oz, g, lb, fl oz:\n')
	
	if itemA == itemB :
		print(f"Both are EQUAL value at ${round(itemA,2)} per/{unit}")
	elif itemA < itemB:
		print(f"Item A is the BETTER DEAL at ${round(itemA,2)} per/{unit}")
		print(f'You saved ${round(itemB -itemA,2)}per/{unit}')
	elif itemB < itemA:
		print(f"Item B is the BETTER DEAL at ${round(itemB,2)} per/{unit}")
		print(f'You saved ${round(itemA -itemB,2)}per/{unit}')
	else:
		print('error')

	x = input('Try again? Type yes or no').lower()
	if x == 'yes':
	  main()
	else:
		print('Done')	

main()