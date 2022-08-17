numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'VI': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

def bai1():
    inp = input("Nhap so la ma: ")
    try:
        print(numbers[inp])
    except:
        print('Not found')

numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13,'XIV': 14, 'XV': 15,
'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}

def bai2():
    numbers_3 = dict(numbers.items() | numbers_2.items())
    inp = input("Nhap so la ma: ")
    try:
        print(numbers_3[inp])
    except:
        print('Not found')

number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

def bai3():
    number_dict = {}
    for idx, val in enumerate(number_list):
        number_dict[val] = idx + 1
    inp = input("Nhap so la ma: ")
    try:
        print(number_dict[inp])
    except:
        print('Not found')

students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
{'firstName': 'Mervin', 'lastName': 'Friedland'},
{'firstName': 'Aron', 'lastName': 'Wilkins'}]

def bai4():
    print("List of names:")
    for student in students:
        print(f"- {student['firstName']} {student['lastName']}")
        
def bai5():
    for key in names.keys():
        print(f"List of {key}:")
        for student in names[key]:
            print(f"- {student['firstName']} {student['lastName']}")
            
def bai6():
    sequence = input("Input sequence: ")
    result = {}
    for seq in list(sequence):
        result[seq] = result.get(seq, 0) + 1
    print(result)