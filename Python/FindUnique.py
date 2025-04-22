# Временная сложность зависит от использованных методов и структур данных. Влияет на количество операций, необходимых для выполнения алгоритма.

# Пространственная сложность также зависит от используемых методов и структур данных и отображает количество памяти,
# необходимое для хранения промежуточных результатов и окончательного результата.

def sum_decorator(method):
    def wrapper(self):
        if self.solution:
            return sum(self.solution[:self.solution.index('_')])
        
        else:
            return f"Массив еще не отсортирован, сумма исходных элементов - {sum(self.nums)}"
    return wrapper

class UniqueArrayProcessor:
    def __init__(self, nums):
        self.nums = sorted(nums)
        self.solution = []

    def process(self):
        seen = set()    # Множество для отслеживания уникальных элементов                       # O(1) в худшем случае
        self.solution = [num for num in self.nums if not (num in seen or seen.add(num))]        # O(n)
        self.solution += ['_'] * (len(self.nums) - len(self.solution))

    @sum_decorator
    def array_sum(self):
        pass

    def __str__(self):
        return f"Исходный массив: {self.nums}\nИтоговый массив: {self.solution}"

nums = [4, 2, 2, 3, 1, 4, 1]
processor = UniqueArrayProcessor(nums)
processor.process()
print(processor)
print(f"Сумма элементов: {processor.array_sum()}")