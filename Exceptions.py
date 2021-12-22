# Errors and Exception
try:
    a =5 / 0
    b = a + 4
except ZeroDivisionError as e:
    print(e)    
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up....')        


class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value
def test_value(x):
    if x> 100:
        raise ValueTooHighError('value is too high')
    if x< 5:
       raise ValueTooSmallError('value is too low', x) 
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)    
    