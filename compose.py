# Реализуйте функцию compose, которая принимает на вход две
# других одноаргументных функции и возвращает новую функцию.
# Эта новая функция также должна принимать один аргумент и
# применять к нему исходные функции в нужном порядке: для
# функций f и g порядок применения должен выглядеть,
# как f(g(x)).
#
# Примеры
# Примеры ниже помогут понять, как должна работать функция:
#
# >>> def add5(x):
# ...     return x + 5
# ... def mul3(x):
# ...     return x * 3
# ...
# >>> compose(mul3, add5)(1)
# 18
# >>> compose(add5, mul3)(1)
# 8
# >>> compose(mul3, str)(1)
# '111'
# >>> compose(str, mul3)(1)
# '3'
def compose(func1, func2):
    return lambda arg: func1(func2(arg))


if __name__ == '__main__':
    def add5(x):
        return x + 5


    def mul3(x):
        return x * 3


    print(compose(mul3, add5)(1))
    print(compose(mul3, str)(1))
    assert compose(mul3, add5)(1) == 18
    assert compose(add5, mul3)(1) == 8
    assert compose(mul3, str)(1) == '111'
    assert compose(str, mul3)(1) == '3'
