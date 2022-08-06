
def get_avr_score(subjects): 
    sum = 0
    for i in range(len(subjects)):
        j = float(input(f'Nhập điểm môn {subjects[i]}: '))
        sum += j
    avarage_score = round(sum / len(subjects), 1)
    return avarage_score

def categorize(score):
    rank = ''
    if score >= 8 and score <= 10:
        rank = 'giỏi'
    elif score >= 6.5 and score < 8:
        rank = 'khá'
    elif score >= 5 and score < 6.5:
        rank = 'trung bình'
    else:
        rank = 'yếu'
    return 'Học lực ' + rank

def main():
    subjects = ['Toán','Lý','Hoá','Anh','Văn']
    avr_score = get_avr_score(subjects)
    rank = categorize(avr_score)
    print(rank)
    
main()