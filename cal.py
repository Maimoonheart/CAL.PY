# VERSION 1.0

# print('''
#       What operation would you like to perform?
#       1.Addition
#       2.Subtraction
#       3.Multiplication
#       4.Division
#       *.Exit
#       ''') 
# user = input('Option: ')
# num1 = float(input('Enter  the first number:'))
# num2 = float(input('Enter  the second number:'))
# if user == '1':
#     result = num1 + num2
#     print('Answer:',result)
# elif user == '2':
#     result = num1 - num2 
#     print('Answer:',result)
# elif user == '3':
#     result = num1 * num2
#     print('Answer:',result)
# elif user == '4':
#     result = num1 / num2    
#     print('Answer:',result)
# elif user == '*':
#     exit()
# else:
#     print('Invalid command')


# VERSION 2.0
    
print('''
      What operation would you like to perform?
      1.Addition
      2.Subtraction
      3.Multiplication
      4.Division
      *.Exit
      ''') 
user = input('Option: ')
num1 = float(input('Enter  the first number:'))
num2 = float(input('Enter  the second number:'))
if user == '1':
    result = num1 + num2
    print('Answer:',result)
elif user == '2':
    result = num1 - num2 
    print('Answer:',result)
elif user == '3':
    result = num1 * num2
    print('Answer:',result)
elif user == '4':
    result = num1 / num2    
    print('Answer:',result)
elif user == '*':
    exit()
else:
    print('Invalid command')



    
