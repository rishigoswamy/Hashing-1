#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 20:13:50 2026

@author: rishigoswamy

    Problem:
    ----------
    https://leetcode.com/problems/isomorphic-strings/description/
    
    Given two strings s and t, determine if they are isomorphic.
    
    Two strings are isomorphic if the characters in s can be replaced to
    get t, such that:
    - Each character maps to exactly one character.
    - No two characters map to the same character.
    - The order of characters is preserved.
    
    Approach:
    ----------
    We use a hash map to store the mapping from characters in string s
    to characters in string t.
    
    As we iterate through both strings simultaneously, for each character
    in s, we check:
    - If it has not been mapped before, ensure that the corresponding
      character in t has not already been used (to maintain a one-to-one
      mapping).
    - If it has been mapped before, verify that it maps to the same
      character in t.
    
    A set is used to track already-mapped characters in t to prevent
    multiple characters in s from mapping to the same character.
    
    If all characters satisfy these conditions, the strings are isomorphic.
    
    Time Complexity:
    ----------------
    O(n), where n is the length of the strings.
    Each character is processed exactly once.
    
    Space Complexity:
    -----------------
    O(1), ds and t consist of any valid ascii character.

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
         
        sourceMap = {}
        mappedCharSet = set()

        for i in range(0, len(s)):
            if s[i] not in sourceMap:
                if t[i] in mappedCharSet:
                    return False
                sourceMap[s[i]] = t[i]
                mappedCharSet.add(t[i])

            if s[i] in sourceMap:
                if sourceMap[s[i]] != t[i]:
                    return False

        return True 
   