score_lst = [78, 56, 67]

# bai 2 
print("High scores: ")
# for index, value in enumerate(score_lst):
#     print(f"{index}. {value}")
    
# bai 3
inp = int(input("Input new score: "))
score_lst.append(inp)
for index, value in enumerate(score_lst):
    print(f"{index}. {value}")