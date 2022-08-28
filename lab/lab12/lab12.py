from datetime import datetime

def bai1():
    print("List of names")
    with open("names.txt", 'r') as f:
        for line in f.readlines():
            print(f"- {line}")
        f.close()
        
def bai2():
    file_name = input("Input file name: ")
    try:
        with open(file_name, 'r') as f:
            print("File content:\n")
            for line in f.readlines():
                print(f"{line}")
            f.close()
    except:
        print("File not found.")
        
def bai3():
    print("== Input file content below ==")
    res = ""
    while True:
        line = input()
        if line == '':
            break
        res += line + "\n"
    with open('inputs.txt', 'w') as f:
        f.write(res)
        f.close()
    print("== Input recorded in inputs.txt ==")

def bai4():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("== Input file content below ==")
    res = ""
    while True:
        line = input()
        if line == '':
            break
        res += line + "\n"
    with open('logs.txt', 'a') as f:
        f.write(now)
        f.write('\n'+res + "\n")
        f.close()
    print("== Input recorded in inputs.txt ==")

def bai5():
    score = 0
    print("Give the correct answers to get points.")
    with open("questions.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            l = line.split(',')
            inp = int(input(l[0]))
            if inp == int(l[1]):
                score += 1
        print(f"== You get {score}/{len(lines)} points ==")

