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
 
