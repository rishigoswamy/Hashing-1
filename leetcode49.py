#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 20:07:23 2026

@author: rishigoswamy

    Problem:
    ----------
    https://leetcode.com/problems/group-anagrams/
    
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.
    
    An anagram is a word or phrase formed by rearranging the letters
    of a different word or phrase, typically using all the original
    letters exactly once.
    
    Approach:
    ----------
    To group anagrams efficiently, we use a frequency-based key
    instead of sorting each word.
    
    For every word, we create an array of size 26 that counts the
    frequency of each character ('a' to 'z').
    This frequency array uniquely represents the anagram group and
    is converted to a tuple so it can be used as a dictionary key.
    
    Words with identical character frequency arrays belong to the
    same anagram group and are collected together using a hash map.
    
    Time Complexity:
    ----------------
    O(n * k), where n is the number of words and k is the maximum
    length of a word.
    Each word is processed once, and counting characters takes O(k).
    
    Space Complexity:
    -----------------
    O(n * k), due to storing the frequency keys and grouped anagrams
    in the hash map.

"""

import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = defaultdict(list)
        res =[]

        for word in strs: 
            charArray = [0] * 26
            for char in word:
                charArray[ord(char)-ord('a')]+=1
            hMap[tuple(charArray)].append(word)

        for key in hMap:
            res.append(hMap[key])
        return res

