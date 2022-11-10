operator = input(''' Please select operator :
+
-
*
/
''')

number1 = int(input('Please enter your first number: '))
number2 = int(input('Please enter your last number: '))

# Function

if operator == '+':
    print('{} + {} = '.format(number1,number2))
    print(number1 + number2)

elif operator == '-':
    print('{} - {} = '.format(number1,number2))
    print(number1 - number2)

elif operator == '*':
    print('{} * {} = '.format(number1*number2))
    print(number1*number2)

elif operator == '/':
    print('{} / {} = '.format(number1/number2))
    print(number1/number2)

else:
    print('Your operator is not provide')