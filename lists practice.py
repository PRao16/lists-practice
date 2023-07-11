#]LISTS stores a series of items in a particular order. You can access them using an index or within a loop.
#items in list are stored within square brackets.

bikes = ['red', 'blue', 'black', 'white']
print(bikes)

first_bike = bikes[0]
print('first_bike is  '+first_bike)

second_bike = bikes[1]
print('second bike is ' + second_bike)

last_bike = bikes[-1]
print('last bike is ' + last_bike)
#adding items to a list

boxes = ['white', 'black', 'brown']

#append is inbuilt function to add items to lists.
boxes.append('blue')
print(boxes)

#Making numerical lists
squares =[]
#created an empty list called squares.
#you can add items to the empty list by command squares.append

for x in range(1,11):
    squares.append(x**2)

print(squares)
#FOR I IN LIS

list = [1,2, 3]
for i in list:
    print(list, end="")


#List comprehensions:

squares = [x**2 for x in range(1,11)]
print(x)

#scaling a list:

finishers =['Sam', 'bob', 'ada', 'bea']
#first_two = finishers[:2]
#print(first_two)

#copyig a list
finishers =['Sam', 'bob', 'ada', 'bea']
copy_of_finishers = finishers[:]

print()
print()# lines to sperate the code. more list practice


colorlist =['red', 'white', 'blue', 'orange']
print(colorlist)
colorlist.append('gray')
print(colorlist)

colorlist.insert(0,'yellow')
print(colorlist)
colorlist.remove('white')

print(colorlist)

print(colorlist)
colorlist.pop(4)

print(colorlist)
colorlist.index('orange')

colorlist.count('blue')

colorlist.sort()
print(colorlist)

colorlist.reverse()
print(colorlist)

colorlist.copy()


#Looping through a list

user=['john', 'joseph', 'Matthew', 'David']
print(user)
for user in user:
    print(user)

Grades=[]
Grades.append(30)
print(Grades)
Grades.append(80)
print(Grades)

Grades.append(90)
print(Grades)
for i in Grades:
    print(Grades)

print()

for i in Grades:
    print(Grades)

for u in user:
    print(user)

for user in user:
    print(user)

for s in user:
    print(user)
for i in user:
    print(user)


user=['john', 'joseph', 'Matthew', 'David']
user.append('Joshua')
user.append('Steven')
user.remove('joseph')
num_users=len(user)


print(user)
user.pop()
print(user)
user.pop(1)
print(user)
user.append('Mark')
user.append('Joe')
print(user)

#sorting

user.sort()

print(user)
user.sort(reverse=True)
print(user)
for x in user:

    print('Welcome to this celebration!  ', user)
#print one by one
print() #for space
print()#for space
for x in user:
    print('Welcome to this celebration!  ' + x)
    print('Welcome to this celebration!  ' , x)

for loop in user:
    print('Thank you ' + loop +'!')

for numbers in range(10):
    print (numbers)
#print number 1-10

for numbers in range(1,11):
    print(numbers)

#printing the numbers 1 t0 1000
for numbers in range(1,1001):
    print(numbers)

print()#seperator

#Making a list of numbers from 1 to a million

#Simple statistics using lists:
print("Finding the minimum in a alist using min of list")

ages = [93, 45,67, 65, 90 , 9, 87, 100]
youngest = min(ages)
print(youngest)

print("Finding the maxiumum in a alist using max of list")
oldest=max(ages)
print(oldest)

#print('finding the sum of all ages. using sum

Total_age=sum(ages)
print('Total age of all people in this list is ',Total_age)
print('Total age of all people in this list is ' + str(Total_age))

#SLICING A LISTS
finishers=['kai','abe','kevin','kim','Martin']
first_3_finishers=finishers[:3]
print(first_3_finishers)
print("GETTING THE LAST 3 FINISHERS:")
last_3_finishers=finishers[-3:]
print(last_3_finishers)

print('get the 3-5 finishers')
_3_5_finishers=finishers[1:4]
print(_3_5_finishers)

print('to copy a list use [:]')
copy_of_finishers=finishers[:]

print(copy_of_finishers)
