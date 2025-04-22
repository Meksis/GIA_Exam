# За счет учета вложенности, получается оставить текст вне скобок в исходном виде

def remove_parentheses(text):
    result = []
    depth = 0    # Переменная для отслеживания уровня вложенности скобок

    for char in text:
        if char == '(':
            depth += 1               # Увеличиваем уровень вложенности при открывающей скобке

        elif char == ')':
            if depth > 0:
                depth -= 1           # Уменьшаем уровень вложенности при закрывающей скобке
        else:
            if depth == 0:
                result.append(char)  # Добавляем символ в результат, если он не внутри скобок

    return ''.join(result)


text = "О могильную плиту удар исправит прикус (Velial Squad) ((Великий и ужасный)). Слова из трека моего любимого бенда"
cleaned_text = remove_parentheses(text)
print(cleaned_text)