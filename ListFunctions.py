import os
import sys
import random


print("Hello Youtube!!")
quote = "Mess up with the best and die like a rest .";
print("The quote is : " + quote )

''' Lists '''

def list_printer(): #Prints the elements of a list1 containig animal names 
	list1 = ['Cat','Dog','Giraffe','Cow']
	#Prints the first elemnt in the list1 
	print("First animal : " + list1[0])
	#prints the length of the list1
	print("The length of the list1 is : %d" %(len(list1)))
	#Insert function 
	list1.insert(0 , 'Buffalo')
	#Prtint the last added elemtnt
	print("The last added element is " + list1[0])
	#Append function
	list1.append('Donkey')
	#Print the appended element
	print("The appended element is : " + list1[5])
	#Remove function
	list1.remove('Dog')
	#Print the list1 
	print("The list1 is %s" % (list1))
	#Add another elemnt with ame value
	list1.append('Buffalo')
	#Count and diplay the number of times "Buffalo" is added to the list1
	print("Number of buffaloes : %d" % (list1.count('Buffalo')))
	#Print the current list1 order
	print("The current list1 order : %s" % (list1))
	#Reverse the list and print it
	list1.reverse()
	print("The reversed list is : %s" % (list1))
	#Search for the index of "Cat" and display it
	print("The word \"Cat\" is located at : %dth position" %(list1.index('Cat')))
	#Print a particular range of elements in a list
	print("The range from 2 to 4 elements: %s" % (list1[2:5]))
	
 
list_printer()
