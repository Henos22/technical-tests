from itertools import combinations, repeat,product
import random

def letter_value(char):
    one_point = ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S','U' ]
    two = ['D','G']
    three = ['B','C','M','P']
    four =  ['F', 'H', 'V', 'W', 'Y'] 
    five = ['K']
    eight = ['J','X']
    ten = ['Q','Z']

    if char in one_point:
        return 1
    if char in two:
        return 2
    if char in three:
        return 3
    if char in four:
        return 4
    if char in five:
        return 5
    if char in eight:
        return 8 
    if char in ten:
        return 10


def points_for_word(word):
    points_tally = []
    for char in word:
        points_tally.append(letter_value(char.upper()))
    return sum(points_tally)

# print(points_for_word('hello'))

def bag_of_tiles():
    bag = []
    one = ['K', 'J', 'X', 'Q', 'Z'] 
    two = ['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y']
    three = ['G']
    four = ['L','S','U','D']
    six = ['N','R','T']
    eight = ['O']
    nine = ['A','I']
    twelve = ['E']

    # bag.extend(repeat(given_value,5))
    for char in one:
        bag.extend(repeat(char,1))
    for char in two:
        bag.extend(repeat(char,2))
    for char in three:
        bag.extend(repeat(char,3))
    for char in four:
        bag.extend(repeat(char,4))
    for char in six:
        bag.extend(repeat(char,6))
    for char in eight:
        bag.extend(repeat(char,8))
    for char in nine:
        bag.extend(repeat(char,9))
    for char in twelve:
        bag.extend(repeat(char,12))
    
    return bag

# print(bag_of_tiles())

def assign_player_rack():

    bag = bag_of_tiles()
    player_rack = random.choices(bag, k=7)
    return player_rack

print(assign_player_rack())



def find_words_in_rack():
    valid_words = []
    rack = assign_player_rack()
    dictionary = open("dictionary.txt")
    dict = dictionary.read()
    combinations = [''.join(comb) for comb in product(rack, repeat=len(rack))]
    print(combinations)
    for word in combinations:
        if word in dict:
            valid_words.append(word)
            break
    return valid_words

print(find_words_in_rack())