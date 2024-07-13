def encryption(number: int):
    if number < 3 or number > 20:
        return 'число из первой вставки не соответствует условию задачи'
    first_digit = number
    result = ''
    if number > 10:
        first_digit = 9
    for i in range(1, first_digit + 1):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                # print(f'{i} : {j}')
                result += str(i) + str(j)
    return result

def main():
    print(encryption(20))
    

if __name__ == "__main__":
    main()