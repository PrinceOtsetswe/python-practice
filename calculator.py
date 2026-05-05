print('''Simple calculator

Operations:
* for multiplication
/ for division
+ for addition
- for subtraction
''')

num1 =float(input('input first digit: '))
num2 =float(input('input second digit: '))

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
