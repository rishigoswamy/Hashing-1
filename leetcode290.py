#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 20:17:44 2026

@author: rishigoswamy

    Problem:
    ----------
    https://leetcode.com/problems/word-pattern/
    
    Given a pattern and a string s, determine if s follows the same pattern.
    
    A valid match requires a bijection between letters in pattern and
    non-empty words in s:
    - Each letter maps to exactly one word
    - Each word maps to exactly one letter
    
    Approach:
    ----------
    Split the input string s into words and first check whether the number
    of words matches the length of the pattern.
    
    Use a hash map to map each pattern character to its corresponding word,
    and a set to track words that have already been mapped.
    While iterating, if a pattern character has not been seen before, map it
    only if the word is unused; if it has been seen, verify that it maps to
    the same word.
    
    If all characters satisfy these conditions, the pattern is followed.
    
    Time Complexity:
    ----------------
    O(n), where n is the number of words in s.
    Each word is processed exactly once.
    
    Space Complexity:
    -----------------
    O(n), due to the set storing mapped words.
    (The pattern-to-word map is O(1) since pattern characters are limited to
    26 lowercase English letters.)

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strList = s.split(" ")
        patternList = [char for char in pattern]
 
        mappedCharSet = set()
        patternMap = {}

        if len(strList) != len(patternList):
            return False

        for i in range(len(strList)):
            if patternList[i] not in patternMap:
                if strList[i] in mappedCharSet:
                    return False
                patternMap[patternList[i]] = strList[i]
                mappedCharSet.add(strList[i])
            if patternList[i] in patternMap:
                if patternMap[patternList[i]] != strList[i]:
                    return False
            
        return True        