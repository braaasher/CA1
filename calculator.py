class Calculator(object):
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
            
    def subtract(self):
        return self.a - self.b 
    
    def multiply(self):
        return self.a*self.b
    
    def divide(self):
        return self.a/self.b
    
    def square(self):
        return self.a*self.a

    def cube(self):
        return (self.a)*(self.a)*(self.a)
    
    def expon(self):
        return self.a**self.b
    
    def sqrt(self):
        return self.a**(0.5)

    def pi(self):
        return (self.a)*(3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745)

    def factorial(self):
        self.b = 1
        while self.a >= 1:
            self.b = self.b * self.a
            self.a = self.a - 1
        return self.b