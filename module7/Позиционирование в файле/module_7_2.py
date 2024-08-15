
def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string  in enumerate(strings):
            strings_positions.update({(index+1, f.tell()): string})
            f.write(string + '\n')
    return strings_positions



def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('module7\Позиционирование в файле\\test.txt', info)
    for elem in result.items():
        print(elem)


if __name__ == "__main__":
    main()
