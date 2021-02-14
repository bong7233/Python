# 행맨..
# 잘만드는것보다는 큰틀을 짜보자

# 기본프로그램 큰 흐름을짜고
# 그다음 다양한 라이브러리를 활용 및 테스트

import time
import csv
import random
import winsound

name = input("What is your name?")
print("Hi, " + name, "Time to play game")
print()
time.sleep(1)
print("Start loading..")
print()
time.sleep(0.5)

word = []

# 문제 csv 파일을 로드해보기

with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)

q = random.choice(words)

word = q[0].strip()

guesses = ""

turn = 10

while turn > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print("_", end=' ')
            failed += 1
    if failed == 0:
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Good mission complete')
        break
    print()

    print('Hint : {}'.format(q[1].strip()))
    print()
    guess = input("guess a character.")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong..")
        print("You have", turn, 'more guesses.')

        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print('You failed. BYE')
