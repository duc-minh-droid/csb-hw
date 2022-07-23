score_lst = [78, 56, 67, 0, 12]

def desc_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

inp = int(input("Input new score: "))
score_lst.append(inp)
desc_sort(score_lst)
for index, value in enumerate(score_lst):
    if index >= 5: 
        break
    print(f"{index+1}. {value}")