set(itertools.permutations([7, 3, 0, 0]))

cards = list(itertools.product(suits, runs))

list(itertools.combinations(cards, 5))

# define a function that returns factorials
def factorial(n):
    product = 1
    while n != 0:
        product *= n
        n -= 1
    return product