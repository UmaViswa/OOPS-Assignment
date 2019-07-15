from Class_example import math_operations
class Advance_Calculator(object):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.M = math_operations(self.num1,self.num2)

    def test_math_operation(self):
        A = self.M.addition()
        return (A)

if __name__ == '__main__':
    nb1 = 5
    nb2 = 7
    Adv=Advance_Calculator(nb1,nb2)
    x= Adv.test_math_operation()
    print (x)