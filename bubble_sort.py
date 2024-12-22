

def bubblesort(num: list):

    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(num)-1):
            if num[i] > num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]
                intercambio = True


nums = [10,3,2,6,8,9,0]
bubblesort(nums)
print(nums)
