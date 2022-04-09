def generation(n):
    for number in range(1, n + 1, 2):
        yield number


gen = generation(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
