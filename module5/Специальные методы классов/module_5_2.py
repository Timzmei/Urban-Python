class House():
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        
    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(0, new_floor + 1):
                print(i)
        
    

def main():  
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)
    
    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))
        
if __name__ == "__main__":
    main()