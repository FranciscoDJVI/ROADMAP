def selecctionsort(num: list):

    for i in range(len(num)):

        lowest_value_index = i

        for j in range(i + 1, len(num)):
            if num[j] < num[lowest_value_index]:
                lowest_value_index = j

        num[i], num[lowest_value_index] = num[lowest_value_index], num[i]


num = [5,2,1,8,4]
selecctionsort(num)
print(str(selecctionsort))