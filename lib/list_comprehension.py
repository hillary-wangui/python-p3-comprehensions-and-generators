#!/usr/bin/env python3

num_list = [0, 1, 3, 5, 7, 8, 9]

def return_evens(num_list):
    evens_list = [x for x in num_list if x % 2 == 0]
    
    return evens_list
    
print(return_evens(num_list))


sentence_list = ["Hello", "I'm doing great", "Python is fun"]

def make_exclamation(sentence_list):
    exclamation_list = [x + "!" for x in sentence_list ]

    return exclamation_list
    
print(make_exclamation(sentence_list))