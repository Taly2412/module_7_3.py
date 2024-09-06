class WordsFinder:
    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                str_ = file.read().lower()
                for x in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    str_ = str_.replace(x, '')
                all_words[file_name] = str_.split()
                return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        for name, words in dict_.items():
            if word.lower() in words:
                index = words.index(word.lower())
                return {name: index}

    def count(self, word):
        dict_ = self.get_all_words()
        for name, words in dict_.items():
            if word.lower() in words:
                count = words.count(word.lower())
                return {name: count}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
