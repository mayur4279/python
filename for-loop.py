#program to print 1 to 10 numbers 

print("this is for loop")
 
for i in range(1,10):
	print(i)
newline() 



#program to print numbers on list 

numbers=[6, 5, 3, 8, 4, 2, 5, 4, 11]

for i in  numbers:
	print (i)


	
	
#program to find sum of all numbers

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

a=0

for i in numbers:
	a=a+i

print("the addition of numbers is", a )



# program to display student's marks from record 

student_name=str(input("enter a student name="))

marks={'mayur': 90, 'Jules': 55, 'Arthur': 77} 

for student in marks:
	if student == student_name:
	  print(marks[student])
	  break
else:
    print("no entry found in dataset.")



