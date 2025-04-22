

def cache_result(method):
    def wrapper(self):
        # Если результат уже вычислен, возвращаем его из кэша
        if self.solution is not None:
            print("Читаем из кэша")
            return self.solution
        # Выполняем метод только при первом вызове
        return method(self)
    return wrapper

class RomanConverter:
    def __init__(self, num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Число должно быть натуральным.")
        self.num = num        # Исходное число
        self.solution = None  # Кэш

    @cache_result
    def intToRoman(self):
        print("Вычисляем число")
        # Список пар (значение, римский символ) в порядке убывания
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = []
        num = self.num
        
        # Проход по всем парам для формирования результата
        for value, symbol in roman_map:
            while num >= value:        # Пока значение подходит
                result.append(symbol)  # Добавляем символ
                num -= value           # Уменьшаем оставшееся число
        
        self.solution = "".join(result)  # Сохраняем результат в кэш
        return self.solution
    
    def __str__(self):
        if self.solution is None:
            return "Число еще не переведено в римскую систему счисления."
        return f"Число {self.num} в римской системе счисления равно {self.solution}"


a = RomanConverter(495)
a.intToRoman()
print(a)
a.intToRoman()
print(a)

b = RomanConverter(1949)
b.intToRoman()
print(b)
b.intToRoman()
print(b)