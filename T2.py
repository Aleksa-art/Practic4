def countSum():
    num = float(input("Уведіть Ваше число:"))
    sum = 0
    for i in range(num+1):
        if i != num+1:
            sum += i
    print(sum)
    return sum

countSum()
