def fibonacci(n):
    first, second, temp = 1, 2, 0
    n_fibonacci = [1, 2]

    while temp < n:
        temp = first + second
        if temp > n:
            break
        else:
            n_fibonacci.append(temp)
        first = second
        second = temp

    return n_fibonacci


def is_even_sum(n_fibonacci):
    total_sum = 0

    for num in n_fibonacci:
        if num % 2 == 0:
            total_sum += num

    return total_sum


if __name__ == '__main__':
    t = int(input().strip())  # number of test cases

    results = []
    for t_itr in range(t):  # amount of numbers
        n = int(input().strip())

        n_fibonacci = fibonacci(n)

        result = is_even_sum(n_fibonacci)
        results.append(result)

    for result in results:
        print(result)