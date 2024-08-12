import math

class Figure():
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = list(sides) if sides == self.sides_count else [1] * self.sides_count
        self.__color = list(color)
        self.filled = False
    
    def get_color(self):
        return self.__color
    
    def __is_valid_color(self, *color):
        if all(0 <= x <= 255 for x in color):
            return True
        else: False 
    
    def set_color(self, *color):
        if self.__is_valid_color(*color):
            self.__color = list(color)
    
    def __is_valid_sides(self, *sides):
        if (x > 0 and len(sides) == self.sides_count for x in sides):
            return True
        else: False
        
    def get_sides(self):
        return self.__sides
    
    def __len__(self):
        return sum(self.__sides)
        
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        

class Circle(Figure):
    sides_count = 1
    
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = list(sides)[0]/(2*math.pi)
        
    def get_square(self):
        return math.pi * self.__radius**2
    

class Triangle(Figure):
    sides_count = 3
    
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = 2*self.get_square()/list(self.sides)[0]
        
    def get_square(self):
        half_perimeter = sum(list(self.__sides)) / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.__sides[0]) * (half_perimeter - self.__sides[1]) * (half_perimeter - self.__sides[2]))

class Cube(Figure): 
    sides_count = 12
    
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
    
    def get_sides(self):
        return self.__sides
    
    def get_volume(self):
        return self.__sides[0]*self.__sides[0]*self.__sides[0]
        

def main():

    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())


if __name__ == "__main__":
    main()
