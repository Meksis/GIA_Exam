class CountAndSay:
    def __init__(self, num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Число должно быть натуральным.")
        self.num = num
        self.solution = "1"

    def countAndSay(self):
        for _ in range(self.num - 1):  # Начинаем с 1, поэтому выполняем num-1 итераций
            current = self.solution
            next_sequence = []
            count = 1

            # Проходим по текущей строке и формируем следующую
            for i in range(1, len(current)):
                if current[i] == current[i - 1]:
                    count += 1  # Увеличиваем счетчик, если символ совпадает с предыдущим

                else:
                    next_sequence.append(f"{count}{current[i - 1]}")
                    count = 1

            # Добавляем последний блок (последний символ и его количество)
            next_sequence.append(f"{count}{current[-1]}")

            # Обновляем решение для следующей итерации
            self.solution = ''.join(next_sequence)

    def __str__(self):
        return f"Результат выполнения операции {self.num} раз: {self.solution}"


a = CountAndSay(4)
a.countAndSay()
print(a)  # Результат выполнения операции 4 раз: 1211

b = CountAndSay(7)
b.countAndSay()
print(b)  # Результат выполнения операции 7 раз: 13112221