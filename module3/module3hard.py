def calculate_structure_sum(data):
    sum = 0
    if isinstance(data, list):
        for i in data:
            sum += calculate_structure_sum(i)
    elif isinstance(data, tuple):
        for i in data:
            sum += calculate_structure_sum(i)
    elif isinstance(data, set):
        for i in data:
            sum += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for i in data.items():
            sum += calculate_structure_sum(i)
    elif isinstance(data, int):
        sum += data
    elif isinstance(data, float):
        sum += data
    elif isinstance(data, str):
        sum += len(data)
    return sum


def main():  
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
        ]
        
    result = calculate_structure_sum(data_structure)
    print(result)
        
if __name__ == "__main__":
    main()