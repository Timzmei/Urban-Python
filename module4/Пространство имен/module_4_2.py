def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
        
    inner_function()
        
        
def main():  
    test_function()
    # inner_function()
        
if __name__ == "__main__":
    main()