first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


def main():
    first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))
    print(list(first_result))

    second_result = (len(f) == len(s) for f, s in [(first[i], second[i]) for i in range(len(first))])
    print(list(second_result))
    
    
if __name__ == "__main__":
    main()
