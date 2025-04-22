import re

def remove_parentheses(text):
    while '(' in text:
        text = re.sub(r'\([^()]*\)', '', text)  # Удаление скобок и вложенного в них текста
    return ' '.join(text.split()) # Удаление лишних пробелов

text = "О могильную плиту удар исправит прикус (Velial Squad) ((Великий и ужасный)). Слова из трека моего любимого бенда"
cleaned_text = remove_parentheses(text)
print(cleaned_text)