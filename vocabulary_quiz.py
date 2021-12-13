import random

voca = {}
q = "q"

with open('practice/mini_project/vocabulary/vocabulary_text/vocabulary.txt', 'r') as v:

    for line in v:
        data = line.strip().split(': ')
        eng, kor = data[0], data[1]

        voca[eng] = kor


    while True:
        mix_voca = random.choice(list(voca.items()))
        random_eng, random_kor = mix_voca[0], mix_voca[1]

        answer_voca = input('{}: '.format(random_eng))
        
        if answer_voca == q:
            break
        elif answer_voca == random_kor:
            print('맞았습니다!\n')
        elif answer_voca != random_kor:
            print('아쉽습니다. 정답은 {}입니다.\n'.format(random_kor))