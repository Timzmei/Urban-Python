class House():
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(0, new_floor + 1):
                print(i)
        
    

def main():  
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)
        
if __name__ == "__main__":
    main()