# class MedianCalculator:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         nums = sorted(self.nums)
#         n = len(nums)
#         if n % 2 == 1:
#             median = nums[n // 2]
#         else:
#             median = (nums[n // 2 - 1] + nums[n // 2]) / 2
#         return median


def median_decorator(func):
    def wrapper(self, *args, **kwargs):
        return func(self, *args, **kwargs)

    return wrapper


class Class:
    def __init__(self, nums):
        self.nums = nums
        self.solution = []

    def permute(self):
        self._generate_permutations(self.nums, [])
        

        # The simpliest method
        # from itertools import permutations

        # self.solution = [list(p) for p in permutations(self.nums)]


    def _generate_permutations(self, remaining, current):
        # print(remaining, current)
        if not remaining:
            self.solution.append(current)
            # print('!!!', current)
            return
        
                                            # [1,2,3]
        for i in range(len(remaining)):     # 0-2, 0
            # remaining[0] = 1 => new_remaining = [] + [2,3] = [2,3]
            new_remaining = remaining[:i] + remaining[i + 1:]           # All except fixed number
            # current = [], remaining[0] = 1, new_current = [] + [1] = [1]
            new_current = current + [remaining[i]]                      # Filling sequence
            # print("-" * 4 + '\n', new_remaining, new_current, '\n\n') 
            # new_remaining = [2, 3], new_current = [1]  
            self._generate_permutations(new_remaining, new_current)     # Recursive call



    # @MedianCalculator
    @median_decorator
    def mediana(self):
        arr = sorted(self.nums)
        n = len(arr)
        if n == 0:
            return None

        # Если длина массива нечетная – возвращаем средний элемент
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n // 2 - 1] + arr[n // 2]) / 2

    def __str__(self):
        return f"For gained sequence {self.nums} possible permutes is {self.solution}"


a = Class([1, 2, 3])
a.permute()
print(a)  
print(a.mediana())  # 2

b = Class([1,2,3,4])
b.permute()
print(b)  
print(b.mediana())  # 2.5