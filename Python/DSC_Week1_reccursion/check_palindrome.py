def isPalindrome(string: str) -> bool:
    paliStr = string[len(string): : -1]
    if string == paliStr:
        return True
    else:
        return False