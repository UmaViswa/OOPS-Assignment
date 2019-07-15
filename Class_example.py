class math_operations(object):
    class_attribute_example="Something"
    def __init__(self,a,b):
        #print ("Called constructor of math operations")
        self.a=a
        self.b=b


    def addition(self):
        sumof = self.a + self.b
        #print(sumof)
        return sumof

    def subtraction(self):
        subof = self.a - self.b
        #print(subof)
        return subof

    def multiplication(self):
        mulof = self.a * self.b
        #print(mulof)
        return mulof

    def division(self):
        divof = self.a / self.b
        #print(divof)
        return divof

if __name__ == '__main__':
    n1 = 3
    n2 = 5
    M = math_operations(a=1,b=2)
    print (M.class_attribute_example)
    A = M.addition()
    print (A)
    S = M.subtraction()
    print (S)
    MU = M.multiplication()
    print(MU)
    D = M.division()
    print(D)
