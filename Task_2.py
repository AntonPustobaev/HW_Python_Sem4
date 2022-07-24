#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Find_prime_numbers(n):
    i = 2
    prime_numbers = []
    while n > 1:
        if n % i == 0:
            n /= i
            prime_numbers.append(i)
        else:
            i += 1
    return prime_numbers


N = int(input('Введите натуральное число: '))
print(Find_prime_numbers(N))