list1 = ['a','e','i','o','u']
list2 = list1
list3 = ['a','e','i','o','u']
list1.append('y')
print(str(list1) + " list 1 after line 4")
print(str(list2) + " list 2 after line 4")
print(str(list3) + " list 3 after line 4")
del list2[2]
print(str(list1) + " list 1 after line 5")
print(str(list2) + " list 2 after line 5")
print(str(list3) + " list 3 after line 5")
list3.remove('i')
print(str(list1) + " list 1 after line 6")
print(str(list2) + " list 2 after line 6")
print(str(list3) + " list 3 after line 6")
list1 = [0,1,2,3,4,5,6,7]
print(str(list1) + " list 1 after line 7")
print(str(list2) + " list 2 after line 7")
print(str(list3) + " list 3 after line 7")
list1[4:] = [0,0]
print(str(list1) + " list 1 after line 8")
print(str(list2) + " list 2 after line 8")
print(str(list3) + " list 3 after line 8")
list2.clear()
print(str(list1) + " list 1 after line 9")
print(str(list2) + " list 2 after line 9")
print(str(list3) + " list 3 after line 9")
