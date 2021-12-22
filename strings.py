my_string = "Hello \n world"
print(my_string)

greeting = 'Hello'
name = 'tad'
sentences = greeting + " " + name
print(sentences)

for x in greeting:
    print(x)

my_string = "Hello world"
print(my_string.upper())
print(my_string.count('o'))
print(my_string.replace('world' , 'universe'))
print(my_string.split())

def stuff():
    print('Hello')
    return
    print('World')

stuff()

score = input('Enter Score between 0.0 and 1.0:')
s = float(score)
try:
    if s<=1.0 :
        if s>=0 :
            if s>=0.9 :
                print('A')
            elif s>=0.8 :
                print('B')
            elif s>=0.7 :
                print('C')
            elif s>=0.6 :
                print('D')
            elif s<0.6 :
                print('F')
    else :
        print('error')
except:
    print('Enter a valid score')


#or
score = input("Enter Score: ")
try:
   score = float (score)
except:
   print("Error! Please enter numeric input.")

if 0.9 <= score <= 1.0:
  print("A")
if 0.8 <= score < 0.9:
  print("B")
if 0.7 <= score < 0.8:
  print("C")
if 0.6 <= score < 0.7:
  print("D")
if score < 0.6:
  print("F")
elif score < 0.0 or score > 1.0:
  print("Error! Please enter a valid number.")    
  
def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p
    
hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr,rphr)
print("Pay", p)