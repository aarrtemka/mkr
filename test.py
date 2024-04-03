import os
import pytest
from my_module import count_words_and_sentences


@pytest.fixture
def text_file():
    # Створюємо тимчасовий файл з різним вмістом для кожного тесту
    text = """
    Git — розподілена система керування версіями файлів та спільної роботи.
    Проєкт створив Лінус Торвальдс для керування розробкою ядра Linux.
    Git є однією з найефективніших, надійних і високопродуктивних систем керування версіями.
    Для забезпечення цілісності історії та стійкості до змін заднім числом використовуються криптографічні методи.
    """
    with open("test_file.txt", "w", encoding="utf-8") as file:
        file.write(text)
    
    yield "test_file.txt"
    
    # Після виконання тесту видаляємо тимчасовий файл
    os.remove("test_file.txt")


@pytest.mark.parametrize("input_text, expected_words, expected_sentences", [
    ("This is a sample sentence.", 5, 1),
    ("Another sample sentence.", 3, 1),
    ("One more sample sentence.", 4, 1),
])
def test_count_words_and_sentences(input_text, expected_words, expected_sentences, text_file):
    # Перевіряємо роботу функції на різних вхідних текстах
    count_words_and_sentences(text_file)
    assert count_words_and_sentences(input_text) == (expected_words, expected_sentences)


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
