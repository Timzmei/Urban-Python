from os import name


class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
        
class Shop():
    def __init__(self):
        self.__file_name = 'module7\Режимы открытия файлов\products.txt'
        open(self.__file_name, 'a').close()
        
    def get_products(self):
        content = ''
        with open(self.__file_name, 'r') as file:
            content = file.read()
        return content
    
    def add(self, *products):
        content = self.get_products().split('\n')

        with open(self.__file_name, 'a') as file:
            for product in products:
                if any(p.startswith(product.name) for p in content):
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    content.append(str(product))
                    file.write(str(product) + '\n')
        
    

def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2) # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())


if __name__ == "__main__":
    main()
