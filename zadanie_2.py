numbers = [2,3,7,4,9]

def list_lacks(numbers, n):
    list_1 = []

    for x in range(1, n+1):
        if x not in numbers:
            list_1.append(x)
    
    print(list_1)

list_lacks(numbers, 10)