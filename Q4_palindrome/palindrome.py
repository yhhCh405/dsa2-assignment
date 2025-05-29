import sys

def isPalindrome(s):
    if len(s) <= 1: return True
    if s[0].lower() != s[-1].lower(): return False
    return isPalindrome(s[1:-1])

if __name__=='__main__':
    word=input('Enter word: ').strip()
    print('Palindrome?' , isPalindrome(''.join(ch for ch in word if ch.isalnum())))