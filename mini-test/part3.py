lst = [5, 1, 8, 92, -1, 30]

# bai 1
# inp = int(input('Input a number: '))
# if inp not in lst:
#     print('Number not found')
# else:
#     print(f'Number found at position {lst.index(inp)}')
    
# bai 2
# sum = 0
# for i in lst:
#     sum += i
# print(sum)

# bai 3
print("Input the list of numbers.\nEnter 0 to finish.")
user_list = []
user_inp = ""
while user_inp != 0:
    user_inp = int(input())
    user_list.append(user_inp)
    
user_sum = 0
for i in user_list:
    user_sum += i
    
print(f"Sum of numbers in list: {user_sum}")