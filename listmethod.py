numbers = [1,2,4,5,3,6]

#append method to add item to end of the list
numbers.append(20)
print(numbers)

#insert method to add item in the middle or anywhere in the list insert(index,object to add)
numbers.insert(0,10)
print(numbers)

#remove method ,to remove an item  from a list
numbers.remove(5)
print(numbers)

#clear method ,to clear te whole items in a list
#numbers.clear()
#print(numbers)

#pop method to remove the last item in a list
numbers.pop()
print(numbers)

#index method to check for the existence of an item in a list
numbers.index(2)
print(numbers)

#count method to check number of times a particular item appears in a list
numbers = [1,4,6,3,3,7]
print(numbers.count(3))

#sort method - to arrange th items ina list in ascending order or from the smallest number to the largest
numbers = [5,2,4,6,8,9,1]
numbers.sort()
print(numbers)

#reverse method - does te opposite of sort,rearrange in descending order
numbers2= [5,2,4,6,8,9,1]
numbers2.reverse()
print(numbers2)

#copy method copies a whole list 
numbers3 = numbers2.copy()
print(numbers3)


#Exercise write a program to remove duplicates in a list.
newno = [2 , 3 , 3, 4 , 6, 6, 7 , 3 , 8, 6]
uniqueno = []
for no in newno:
    if no not in uniqueno:
        uniqueno.append(no)
print(uniqueno)