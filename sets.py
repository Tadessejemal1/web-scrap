# sets:unordered, mutable ,no duplicates
#myset = set([1,2,3])
#myset = set(['Hello'])
myset =set()

myset.add(1)
myset.add(2)
myset.add(3)

#myset.remove(1)
#myset.discard(2)

for x in myset:
    print(x)
print(myset.pop())

print(myset)


setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
#setA.update(setB)
setA.intersection_update(setB)
setA.symmetric_difference_update(setB)
print(setA)
print(diff)
print(setB.issuperset(setA))