from typing import Generator

def generate_squares(n):
    for i in range(n):
        yield i ** 2



for i in generate_squares(10):
    print(i)


print(list(generate_squares(10)))