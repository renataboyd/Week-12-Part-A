# Renata Boyd
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(my_input):
    return print('OUTPUT', my_input)

def LoadFile(filename):
    file = open(filename, 'r')
    string = file.read().splitlines()
    return string
    file.close()

def UpdateString(string1, string2, index):
    string1 = list(string1)
    string1[index] = string2
    string1 = ''.join(string1)
    new_string = str(string1)
    print(new_string)
    return new_string


