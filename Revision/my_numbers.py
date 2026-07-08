def square(num):
    sq = num * 2
    return sq

def cube(num):
    cu = num**3
    return cu

def add(n1,n2):
    sum = n1+n2
    return sum


class Calci:
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2

    def sum(self):
        return self.num1+self.num2
    
    def sub(self):
        return self.num1-self.num2
    
    def mul(self):
        return self.num1*self.num2
    
    def div(self):
        return self.num1/self.num2