def get_matrix(n: int, m: int, value: int):
    matrix = []
    for i in range(n):
        new_row = []
        matrix.append(new_row)
        for a in range(m):
            new_row.append(value)
    return matrix

def main():
    print(get_matrix(3, 5, 10))
    
    result1 = get_matrix(2, 2, 10)
    result2 = get_matrix(3, 5, 42)
    result3 = get_matrix(4, 2, 13)
    print(result1)
    print(result2)
    print(result3)

if __name__ == "__main__":
    main()
    