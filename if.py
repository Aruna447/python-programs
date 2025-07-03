# #"if"
# """
# if condition:
#     statements
# """
""" Write a python program to find whether a number is positive or not
"""

# num = int(input("enter a number.."))
# if num>0:
#      print("the number is positive ",num)

 
"""write a program to find biggest of two numbers

"""

# a = int(input("enter a number: "))
# b = int(input("enter anumber: "))
# if a>b:
#     print("A is greater:",a)
# else:
#     print("B is greater:",b)

# Accept the percentage from the user and display the 
# grade according to the following criteria 
#  """
# # Below D-25
# # 25 to 45--C
# # 45 to 50--B
# # 50 to 60--B+
# # 60 to 80--A
# # above 80+--A+
# # """
#  percentage = int(input("enter a number"))
#  pr = int (input ("enter your percentage.."))
#  if pr<25:
#       print("The grade is D..")
#  elif pr>=25 and pr<=45:
#      print("The grade is c..")
#  elif pr>45 and pr<=50:
#      print("The grade is B..")
#  elif pr>50 and pr<=60:
#     print("The grade is B++")
#  elif pr>60 and pr<=8
#          print("The grade is A..")
#  elif pr>80:
#          print("The grade is A++")
#  else:
#          print("Your failed")


""" write a program to accept two numbers from the user and an operator from the user and perform an operation accordingly 
num1 : 5
mum2 : 10
opr : +
answer : 15
"""

# num1 = int(input("enter a number.."))
# num2 = int(input("enter a number.."))
# opr = input("enter a operator : ")
# if opr=="+" :
#     print("The answer : ",num1+num2)
# elif opr=="-" :
#      print("The answer : ",num1-num2)
# elif opr=="*" :
#      print("The answer : ",num1*num2)
# elif opr=="/" :
#      print("The answer : ",num1/num2)
# else:
#      print("Wrong operator selected")


"""
write a program to accept a number from 1 to 12 then display  name of the month and days in that month 
like 1 for january and the no of days 31 and so on

"""

"""slicing in used to retrieve the elements from one particular range to another particular range 
the synatx: s^3(start:stop:skip)
"""
mylist =  [1,2,13,15,16,17,18,19]
print(mylist)
print(mylist[0:6:2])


mylist1=[2,5,6,7,8,9,10]
print(mylist1[0:7:3])


mylist3=[45,46,78,90,56,34,78,90,34,65,89]
print(mylist3[0:8:4])


mylist4=[2,5,6,7,8,9,10]
print(mylist4[2:6:2])
