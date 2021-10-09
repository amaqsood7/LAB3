#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: amaqsood7

def operate(number1, number2, operator):
    # Place logic in this function
	if operator == 'add':
		number3 = number1 + number2
		return number3
	elif operator == 'subtract':
		number4 = number1 - number2
		return number4
	elif operator == 'multiply':
		number5 = number1 * number2
		return number5
	
	else:	
		return 'Error: function operator can be "add", "subtract", or "multiply"'	

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
