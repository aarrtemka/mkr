import re

def count_words_and_sentences(file_path):
    # Відкриваємо файл для читання
    with open(file_path, 'r', encoding='utf-8') as file:
        # Зчитуємо вміст файлу у змінну text
        text = file.read()

    # Підрахунок слів за допомогою регулярних виразів
    words = re.findall(r'\w+', text)
    word_count = len(words)

    # Підрахунок речень за допомогою регулярних виразів
    # Розділяємо текст на речення за символами кінця речення (".", "!", "?", "...")
    sentences = re.split(r'[.!?…]', text)
    # Фільтруємо порожні рядки, які можуть виникнути після розділення
    sentences = [sentence for sentence in sentences if sentence.strip()]
    # Підраховуємо кількість речень
    sentence_count = len(sentences)

    # Виведення результатів
    print("Кількість слів: ", word_count)
    print("Кількість речень: ", sentence_count)


# Виклик функції з вказанням шляху до файлу
file_path = "/Users/artem/Desktop/mkr/mkrtext.txt"
count_words_and_sentences(file_path)







