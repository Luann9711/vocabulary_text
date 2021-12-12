

eng = input('영어 단어를 입력하세요: ')
kor = input('한국어 뜻을 입력하세요: ')

with open('vocabulary.txt', 'a') as v:
    v.write(eng)
    v.write(kor)