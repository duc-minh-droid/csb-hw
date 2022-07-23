lst = [5, 1, 8, 92, 7, 30]
# bai 1
def getEvenList(lst):
    even_lst = []
    even_str = ""
    for x in lst:
        if x % 2 == 0:
            even_lst.append(x)
    for x in even_lst:
        even_str += str(x) + ' '
    return even_str
print(f'Even numbers: {getEvenList(lst)}')

# bai 2
print("Input the list of numbers.\nEnter 0 to finish.")
user_list = []
user_inp = ""
while user_inp != 0:
    user_inp = int(input())
    user_list.append(user_inp)
user_list.pop()
print(f"Even numbers in list: {getEvenList(user_list)}")
