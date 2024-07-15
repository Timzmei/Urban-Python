def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
    
def main():
    result = get_multiplied_digits(40203)
    print(result)
        
        
if __name__ == "__main__":
    main()