# Tuples: ordered, immutable, allows duplicate element

mytuple = ('max',28, 'boston')
#or
#mytuple = tuple(['max', 28 ,'Boston'])
print(mytuple)

item = mytuple[-1]
print(item)


x = 5

if x > 2 :
    print('Bigger than 2')
    print('still bigger')
print('Done with with 2')    


hrs = input("Enter Hours:")
h = float(hrs)
xx = input("Enter the Rate:")
x = float(xx)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)




score = input("Enter Score: ")
xx = float(score)

try: 
    if xx >=0.9:
       print('A')
    elif xx >=0.8:
        print ('B')
    elif xx >=0.7:
        print ('c') 
    elif xx >=0.6:
        print ('D')
    elif xx <0.6:
        print ('F')
except:
    print('an error')