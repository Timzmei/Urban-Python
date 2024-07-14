def print_params(a = 1, b = 'строка', c = True):
    print(f'a = {a}, b = {b}, c = {c}')
    
    
def main():
    print_params(b = 25)
    print_params(c = [1,2,3])
    
    values_list = [1, 'string', True]
    
    values_dict = {'a': 1, 'b': 'string', 'c': True}
    
    print_params(*values_list)
    print_params(**values_dict)
    
    values_list_2 = [1, 'string']
    print_params(*values_list_2, 42)
        
if __name__ == "__main__":
    main()