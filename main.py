from random import randint

basic_list = [randint(-100, 100) for i in range(15)]
sum_of_negative_num = 0
sum_of_even_num = 0
sum_of_odd_num = 0
multiplication_of_3 = 1
multiplication_between_min_max = 1
sum_of_elements_between_first_and_last_positive = 0

index_of_max = basic_list.index(max(basic_list))
index_of_min = basic_list.index(min(basic_list))

index_of_first_positive_num = 0
index_of_last_positive_num = 0

if index_of_min > index_of_max:
    index_of_min, index_of_max = index_of_max, index_of_min

for i in range(len(basic_list)):
    if basic_list[i] < 0:
        sum_of_negative_num += basic_list[i]
    if basic_list[i] % 2 == 0:
        sum_of_even_num += basic_list[i]
    if basic_list[i] % 2 != 0:
        sum_of_odd_num += basic_list[i]
    if i % 3 == 0:
        multiplication_of_3 *= basic_list[i]

for i in range(index_of_min, index_of_max + 1):
    multiplication_between_min_max *= basic_list[i]

for i in range(len(basic_list)):
    if basic_list[i] > 0:
        index_of_first_positive_num = i
        break

for i in range(len(basic_list) - 1, 0, - 1):
    if basic_list[i] > 0:
        print(basic_list[i])
        index_of_last_positive_num = i
        break

for i in range(index_of_first_positive_num, index_of_last_positive_num + 1):
    sum_of_elements_between_first_and_last_positive += basic_list[i]


print("Сумма негативных чисел ", sum_of_negative_num)
print("Сумма парных чисел ", sum_of_even_num)
print("Сумма непарных чисел ", sum_of_odd_num)
print("Произведение элементов с индексом кратным 3 ", multiplication_of_3)
print("произведение элементов между минимальным и максимальным числом ", multiplication_between_min_max)
print("Сумма элементов между первы и последним позитивным числом ", sum_of_elements_between_first_and_last_positive)