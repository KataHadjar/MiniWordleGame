import random

def random_word(digit_number):
    result = ''
    for i in range(digit_number):
        result += str(random.randrange(10))
    return result

def get_match(user_word, game_word):
    if len(user_word) != len(game_word):
        print("Слова разной длины")
        return "diflen"
    if user_word == game_word:
        print("Победа! Было загадно число", game_word)
        return "ok"
    bull_number = [0] * 10
    bull_sum = 0
    for i in range(len(game_word)):
        if user_word[i] == game_word[i]:
            bull_number[ord(user_word[i]) - ord('0')] += 1
    cow_number = [0] * 10
    cow_sum = 0
    for i in range(10):
        cow_number[i] = min(user_word.count(chr(i+ord('0'))), game_word.count(chr(i+ord('0'))))
        cow_number[i] -= bull_number[i]
        bull_sum += bull_number[i]
        cow_sum += cow_number[i]
    print('Найдено', bull_sum, 'быков и', cow_sum, 'коров. Попробуйте ещё раз!')
    return 'next'


new_game = random_word(5)
user_word = input()
while get_match(user_word, new_game) != 'ok':
    user_word = input()
