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



# print('''
#      What operation would you like to perform?
#        1.union
#        2.intersection
#        3.intersection_update
#        4.difference
#        5.difference_update
#        *.Exit
#      ''') 
# set1 = {}
# set2 = {}
# user = input('Option: ')   

# element1 = input("Please enter an element of set 1: ")
# set1.update(element1)

# element2 = input("Please enter an element of set 2: ")
# set2.append(element2)
                                                                                    
# if input == "1":
# result = set1.union(set2)
# print("The union of set 1 and set 2 is: ",result)
# print(result) 
# elif input == "2":
#      result = set1.intersection(set2)
#      print("The intersection of set 1 and set 2 is: ")
#      print(set1 & set2)
# elif user == '*':
#     exit()
# else:
#     print('Invalid command')   


# print('''
#     What operation would you like to perform?
#     1.Addition
#     2.Subtraction
#     3.Multiplication
#     4.Division
#     5.Modulus
#     *.Exit
# #     ''') 

# user = input('Option: ')   



# def addition():
#     value1 = float(input('Enter the first number: '))
#     value2 = float(input('Enter the first number: '))
#     result = value1 + value2
#     print(result)

# def subtraction():
#         value1 = float(input('Enter the first number: '))
#         value2 = float(input('Enter the first number: '))
#         result = value1 - value2
#         print(result)

# def multiplication():
#         value1 = float(input('Enter the first number: '))
#         value2 = float(input('Enter the first number: '))
#         result = value1 * value2
#         print(result)

# def division():
#         value1 = float(input('Enter the first number: '))
#         value2 = float(input('Enter the first number: '))
#         result = value1 / value2
#         print(result)

# def modulus():
#         value1 = float(input('Enter the first number: '))
#         value2 = float(input('Enter the first number: '))
#         result = value1 % value2
#         print(result)


# if user == '1':
#     addition() 
# elif user == '2':
#     subtraction()
# elif user == '3':
#     multiplication()
# elif user == '4': 
#      division()
# elif user == '5':
#     modulus()
# else:
#     exit()



    # MULTIPLICATION TABLE

user = int(input('Input the number you want to be supplied with the multiplication table: '))
table = range(1,13)
for x in table:
    result = user * x
    print(user , '*', x , '=', result  )

# class Calculator:
#     def __init__(self) -> None:
#         self.name = 'Casio'
         
#         self.home()

#     def home(self):
#         print('Welcome to',self.name)
#         self.val1 = float(input('First value: '))
#         self.val2 = float(input('Second value: '))
#         user = input ('''
#            What operation would you like to perform?
#            1.Addition
#            2.Subtraction
#            3.Multiplication
#            4.Division
#            *.Exit
#         Option: ''') 
        
        # if user == '1':
        #     self.addition()
        # elif user == '2':
        #     self.subtraction()
        # elif user == '3':
        #     self.multiplication()
        # elif user == '4': 
        #     self.division()    
#         elif user == '#':
#             exit()
#         else:
#             print('Invalid option,Try again')
#             self.home()

#     def addition(self):
#         print(f"Ans:{self.val1 + self.val2}")
#         self.decide()
#     def subtraction(self):
#         print(f"Ans:{self.val1 - self.val2}")
#         self.decide()
#     def multiplication(self):
#         print(f"Ans:{self.val1 * self.val2}")
#         self.decide()
#     def division(self):
#         print(f"Ans:{self.val1 / self.val2}")
#         self.decide()
#     def decide(self):
#         user = input('Press 1 to go back to home or # to exit: ')
#         if user == '1':
#             self.home()
#         else:
#             exit()
# casio = Calculator()

# .....
# casio.home()
# print(casio.name)
# print(type(casio))