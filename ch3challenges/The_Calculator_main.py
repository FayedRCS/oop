class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__a = a
        self.__result += self.__a

    def subtract(self, a):
        self.__a = a
        self.__result -= self.__a

    def multiply(self, a):
        self.__a = a
        self.__result *= self.__a

    def divide(self, a):
        self.__a = a
        if self.__a == 0:
            raise ValueError("Cannot divide by zero")
        
        self.__result /= self.__a

    def modulo(self, a):
        self.__a = a

        if self.__a == 0:
            raise ValueError("Cannot divide by zero")
        
        while self.__result > 0:

            self.__result -= self.__a
            if self.__a > self.__result:
                return self.__result
        
        return self.__result
        
        #^Proud note: I really did that by myself 
        #sidenote, i realized later on I could've just done self.__result %= self.__a ... this is cuter though

    def power(self, a):
        self.__a = a
        self.__result **= self.__a
        return self.__result

    def square_root(self):

        self.__result = self.__result ** 0.5

    def clear(self):
        
        self.__result = 0

    def get_result(self):
        return self.__result

