import random
from numpy.random import choice

score = 0

def generate_question(score):
    calc = choice(['+','-','x',':'], p=[0.3,0.3,0.2,0.2])
    a = random.randint(0, 100)
    b = random.randint(0, 50)
    true_ans = 0

    if calc == '+':
        true_ans = int(a + b)
    elif calc == '-':
        true_ans = int(a - b)
    elif calc == '*':
        # hơi bug :))
        true_ans = int(a * b)
    elif calc == ':':
        true_ans = round((a / b),2)

    wrong_ans = random.randint(-10, 100)
    random_ans = choice([true_ans, wrong_ans], p=[0.65,0.35])

    print(f'{a} {calc} {b} = {random_ans}')
    inp = int(input('1 for True, 0 for False: '))

    if inp == 1 and random_ans == true_ans:
        score = score + 1
        print(f'Score: {score}')
    elif inp == 0 and random_ans == wrong_ans:
        score = score + 1
        print(f'Score: {score}')
    else:
        print('Incorrect.')
    return score
     
print('== FREAKING MATH CONSOLE ==')
print('Give correct answers to get scores')

times = int(input('\nHow many times do you want to play? '))

for i in range(times):
    print('\n')
    score = generate_question(score)  

print('\n== GAME OVER ==')
print(f'Your total score is {score}')

