print('''Simple calculator

Operations:
* for multiplication
/ for division
+ for addition
- for subtraction
''')

num1 =float(input('enter first number: '))
num2 =float(input('enter second number: '))

operation = input("enter operation: ")

if operation =='*':
 result = num1 * num2
 print(result)
elif operation =='/':
 result = num1 / num2
 print(result)
elif operation =='+':
 result = num1 + num2
 print(result)
elif operation =='-':
  result = num1 - num2
  print(result)
else:
 print('Invalid operation')
