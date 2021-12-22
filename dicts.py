# Dictionary: key_value pairs, unordered, Mutable
mydict = {'name': 'Max', 'age':28,'city':'new york'}
print(mydict)

value = mydict['name']
print(value)

mydict['email'] = 'max@.com'
print(mydict)

del mydict['name']
#mydict.popitem()
print(mydict)

if 'name' in mydict:
    print(mydict['name'])

try:
    print(mydict['name'])
except:
    print('error')    

for key, value in mydict.items():
    print(key, value)

mydict = {'name': 'Max', 'age':28,'email':'max@xyz.com'}
mydicy2 = dict(name = 'marry' ,age =27, city = 'boston')

mydict.update(mydicy2)
print(mydict)


my_dict = {3:9, 6:36 , 9:81}
print(my_dict)

value = my_dict[3]
print(value)