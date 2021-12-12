
while True:
    eng = ''
    kor = ''
    q = "q"

    eng = input('영어 단어를 입력하세요: ')
    if eng == q:
        break
    
    else:
        pass

    kor = input('한국어 뜻을 입력하세요: ')
 
    if kor == q:
        break

    else:
        pass


    with open('practice/mini_project/vocabulary/vocabulary_text/vocabulary.txt', 'a') as v:
        v.write(eng+': ')
        v.write(kor+'\n')
