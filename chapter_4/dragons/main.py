class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        x = self.pos_x
        y = self.pos_y

        if (x_1 <= x <= x_2) and (y_1 <= y <= y_2):
            return True
        
        return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        shmoked = []
        x_1 = x - self.__fire_range
        x_2 = x + self.__fire_range
        y_1 = y - self.__fire_range
        y_2 = y + self.__fire_range

        print(f"Dragon: ({x},{y})")
        print(f"Fire Range: {self.__fire_range}")

        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                shmoked.append(unit)

        return shmoked