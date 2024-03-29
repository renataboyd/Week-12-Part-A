# Renata Boyd
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(my_input):
    return print('OUTPUT', my_input)

def LoadFile(filename):
    file = open(filename, 'r')
    string = file.read().splitlines()
    list1 = list(string)
    return list1
    file.close()

def UpdateString(string1, string2, index):
    string1 = list(string1)
    string1[index] = string2
    string1 = ''.join(string1)
    new_string = str(string1)
    print('OUTPUT', new_string)

def FindWordCount(input_list, string): 
    i = 0
    input_list = (''.join(input_list)).split()
    for word in input_list:
        if word == string:
            i += 1
    return i
 
def ScoreFinder(players, scores, find_player):
    players = ' '.join(players)
    players = str(players)
    players = players.lower()
    players = players.split()
    i = 0
    y = 0
    while i < len(players):
        if find_player == players[i]:
            score = scores[i]
            find_player = find_player.title()
            y = 1
            break
        elif find_player != players[i]:
            i += 1
    if y == 1:
        print('OUTPUT', find_player, 'got a score of', score)
    else:
        print('OUTPUT player not found')

def Union(list1, list2):
    list3 = list1 + list2
    list4 = [] 
    for element in list3: 
        if element not in list4: 
            list4.append(element) 
    return list4

def Intersection(list1, list2):
    list3 = []
    i = 0
    while i < len(list1):
        if list1[i] in list2:
            list3.append(list1[i])
            i += 1
        else:
            i += 1
    return list3

def NotIn(list1, list2):
    list3 = []
    i = 0
    while i < len(list1):
        if list1[i] not in list2:
            list3.append(list1[i])
            i += 1
        else:
            i += 1
    return list3

