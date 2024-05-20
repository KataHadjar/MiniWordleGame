import random


def random_word(digit_number):
    result = ''
    for i in range(digit_number):
        result += str(random.randrange(10))
    return result


def get_match(user_word, game_word):
    if len(user_word) != len(game_word):
        return "Слова разной длины"
    if not user_word.isnumeric():
        return "Слово должно состоять только из цифр"
    if user_word == game_word:
        return "Победа! Было загадно число " + game_word
    bull_number = [0] * 10
    bull_sum = 0
    for i in range(len(game_word)):
        if user_word[i] == game_word[i]:
            bull_number[ord(user_word[i]) - ord('0')] += 1
    cow_number = [0] * 10
    cow_sum = 0
    for i in range(10):
        cow_number[i] = min(user_word.count(chr(i + ord('0'))), game_word.count(chr(i + ord('0'))))
        cow_number[i] -= bull_number[i]
        bull_sum += bull_number[i]
        cow_sum += cow_number[i]
    return 'Быков: ' + str(bull_sum) + '. Коров: ' + str(cow_sum) + '. Попробуйте ещё раз!'
