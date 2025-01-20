#testpalindrome.py
#palindrome
"""
>>> import palindrome
>>> palindrome.is_palindrome("") #Empty variable
True
>>> palindrome.is_palindrome("a") #len(s)==1
True
>>> palindrome.is_palindrome("abba") #len(s) = even number
True
>>> palindrome.is_palindrome("racecar") #len(s) = odd number
True
>>> palindrome.is_palindrome("hello")  # Not a palindrome
False
"""
import doctest
doctest.testmod(verbose=True)