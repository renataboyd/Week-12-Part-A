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

