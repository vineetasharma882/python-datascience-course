class Calculator:

    #constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #Instance method
    def add(self):
        return self.x+self.y

    def subtract(self):
        return self.x-self.y

    def multyply(self):
        return self.x*self.y

    def divide(self):
        return self.x/self.y