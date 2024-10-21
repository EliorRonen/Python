setA = {'Elior','cyan'}
setB = {'Blue','Elior'}
print("The original sets are:")
print(setA)
print(setB)
setE = setA.intersection(setB)
print("The intersection of both of the sets are:",setE)



import array as arr

array_num = arr.array('i',[1,3,5,3,7,9,3])
print("Original array: "+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items")
print(str(array_num))