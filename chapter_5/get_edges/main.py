class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):

        x1 = min(self.__x1, self.__x2)
        return x1

    def get_right_x(self):

        x2 = max(self.__x1, self.__x2)
        return x2 

    def get_top_y(self):

        y2 = max(self.__y1, self.__y2)
        return y2
    
    def get_bottom_y(self):

        y1 = min(self.__y1, self.__y2)
        return y1

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
