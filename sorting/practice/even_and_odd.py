# partition problem
def segregate(numbers):

    even = 0

    for odd in range(len(numbers)):
        if numbers[odd]%2 ==0:
            #swap
            numbers[even], numbers[odd] = numbers[odd], numbers[even]
            even += 1
        print(numbers)

    return numbers


a = [14, 2, 8, 3, 5]
result = segregate(a)
print(result)
