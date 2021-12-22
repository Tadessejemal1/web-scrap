my_list = ['banana','apple','pig']
print(my_list)

for x in my_list:
    print(x)
if 'banana' in my_list:
    print('yes')
else:
    ('no')        
my_list.append('lemon')
print(my_list)

item = my_list.remove ("apple")
print(item)


my_list2 = [5,True,'orange']
print(my_list2)

mylist = [4,3,1,-1,-5,10]
print(mylist)

item = mylist.sort()
print(mylist)

# slice
mylist2 =[1,2,3,4,5,6,7,8,9]

a= mylist2[1:5]
b = mylist2[::2]
print(a)
print(b)


list_org = ['banana', 'cherry', 'apple']

list_cpy = list_org

list_cpy.append('lemon')

print(list_cpy)
print(list_org )

mylist3 = [1,2,3,4,5]
b= [i*i for i in mylist3]

print(mylist3)
print(b)