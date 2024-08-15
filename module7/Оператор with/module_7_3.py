class WordsFinder():
    def __init__(self, *files):
        self.file_names = list(files)
        
    def get_all_words(self):
        all_words = {}
        delete_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                data = f.read().lower()
                for char in delete_chars:
                    data = data.replace(char, '')
                words = data.split()
                all_words.update({file: words})
                
        return all_words
                
    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file, words in all_words.items():
            for index, w in enumerate(words):
                if w == word:
                    result.update({file: index+1})
        return result
    
    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file, words in all_words.items():
            count = 0
            for w in words:
                if w == word:
                    count += 1
            result.update({file: count})
        return result



def main():
    finder2 = WordsFinder('module7\Оператор with\Mother Goose - Monday’s Child.txt', 'module7\Оператор with\Rudyard Kipling - If.txt', 'module7\Оператор with\Walt Whitman - O Captain! My Captain!.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('for')) # 3 слово по счёту
    print(finder2.count('for')) # 4 слова teXT в тексте всего


if __name__ == "__main__":
    main()
