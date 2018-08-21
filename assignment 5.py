
#Q.1- Take an input year from user and decide whether it is a leap year or not.
#Answer
year=int(input('Enter Year:'))
if year%4==0:
    if year%100==0:
         if year%400==0:
             print(year,'is a leap year ')
         else:
             print(year,'is not a leap year ')
    else:
         print(year,'is a leap year ')
else:
     print(year,'is not a leap year ')

#Q.2-Take length and breadth input from user and check whether the dimensions are of square or rectangle.
#Answer
length=int(input('Enter Length:'))
breadth=int(input('Enter Breadth:'))
if(length>0 and breadth>0):
    if(length==breadth):
         print("Dimensions are of Square")
    else:
        print("Dimensions are of Rectangle")
else:
   print("Wrong Input")

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
#Answer
a1=int(input("Enter age 1:"))
a2=int(input("Enter age 2:"))
a3=int(input("Enter age 3:"))
if(a1>=a2 and a1>=a3):
    print("Oldest age is:",a1)
    if(a2>=a3):
      print("Youngest age is:",a3)
    else:
      print("Youngest age is:",a2)
      
elif(a2>=a1 and a2>=a3):
    print("Oldest is:",a2)
    if(a1>=a3):
      print("Youngest age is:",a3)
    else:
      print("Youngest age is:",a1)
      
else:
    print("Oldest age is:",a3)
    if(a1>=a2):
      print("Youngest age is:",a2)
    else:
      print("Youngest age is:",a1)
    
#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#Answer
'''
1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR".
'''
age=int(input("Enter age:"))
sex=input("Enter Sex( M or F):")
status=input("Enter Marital Status (Y or N):")
if(sex=='F' or sex=='f'):
    print("Place of Service: URBAN AREA ONLY ")
elif(sex=='M' or sex=='m'):
    if(age>=20 and age<=40):
        print("Place of Service: ANYWHERE ")
    elif(age>40 and age<=60):
        print("Place of Service: URBAN AREA ONLY")
    else:
        print("ERROR")
else:
   print("ERROR")
   

'''
Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
'''
#Answer
unit=int(input("Enter units:"))
cost=int(input("Enter cost:"))
amount=unit*cost
print('Amount:',amount)
if(amount>=1000):
    print('Amount after discount:',amount-(amount*(1/10)))
else:
    print("NO DISCOUNT")

#Q.6- Take 10 integers from user and print it on screen.
#Answer
integers=[]
for i in range(10):
    value=int(input('Enter value:'))
    integers.append(value)
print('List:',integers)


#Q.7- Write an infinite loop.An infinite loop never ends. Condition is always true.

#x=1
#while x>0:
 #   print(x)
  #  x+=1


#Q.8- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list
#Answer
l1=[]
l2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digits:'))
    l1.append(b)
print('List:',l1)
for i in range(a):
    sq=l1[i]*l1[i]
    l2.append(sq)
print('List of Squared element:',l2)

#Q.9- From a list containing ints, strings and floats, make three lists to store them separately
#Answer
list1=[]
list2=[]
list3=[]
list4=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    d=input('Enter values:')
    list1.append(d)
print('List:',list1)
for i in range(a):
    if str(list1[i]).isdigit():
        list2.append(list1[i])
    elif str(list1[i]).isalpha():
        list3.append(list1[i])
    else:
        list4.append(list1[i])
print('Int List:',list2)
print('String List:',list3)
print('Float List:',list4)


#Q.10- Using range(1,101), make a list containing only prime numbers. 
#Answer
print("Prime numbers are:")

for i in range(1,101):
   if i > 1:
       for x in range(2,i):
           if (i % x) == 0:
               break
       else:
           print(i)


'''
Q.11- Print the following patterns:
* 
** 
*** 
****
'''
#Answer
print('Pattern')
for i in range(0, 5,1):
    print("* "*i)

    
#Q.12- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
#Iterate over list using for loop.
#Answer
print()
list1=[]
list2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digit:'))
    list1.append(b)
print(list1)
search=int(input("Enter value to search:"))
list1.remove(search)
print(list1)      
         
         
             
         
