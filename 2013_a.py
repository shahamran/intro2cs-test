def f1(x, y = ''):
    if len(x) == 0:
        print(y)
    else:
        for k in range(len(x)):
            f1(x[0:k] + x[k + 1:], y + x[k])
def first_gen(n):
    for index in range(n):
        yield 1 if index%2 else 2
def second_gen(n):
    for index in range(n):
        yield sum(first_gen(index))
def third_gen(n):
    if n:
        yield n + next(third_gen(n-1))
    else:
        yield 0
def fourth_gen(my_list):
    first = my_list[0]
    for value in my_list[1:]:
        second = value
        yield first + second
        first = second
