with open('practice/mini_project/vocabulary/vocabulary_text/vocabulary.txt', 'r') as v:

    for i in v:
        line = (i.strip().split(': '))
        eng = line[0]
        kor = line[1]

        answer_voca = input('{}: '.format(eng))

        if answer_voca == kor:
            print('맞았습니다!')
        elif answer_voca != kor:
            print('아쉽습니다. 정답은 {}입니다.'.format(kor))