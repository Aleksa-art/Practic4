def countNum():
    num = int(input())
    evenList = [(i, "Число ділиться на три" if i%3 == 0  else("Число не ділиться на три")) for i in range(num) if i%2 == 0]
    primeList = [i for i in range(2, num+1) if all(i % j != 0 for j in range(2, i))]
    print(f"Усі парні числа, які було перевірено на подільність на три: {evenList}")
    print(f"Прості числа в діапазоні до заданого числа: {primeList}")
    
countNum()