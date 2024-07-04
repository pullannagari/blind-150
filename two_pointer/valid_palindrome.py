class Solution:
    def isPalindrome(self, s: str) -> bool:

        # filter string
        fs = ""
        for ch in s:
            low_ch = ch.lower()
            if ord("a") <= ord(low_ch) <= ord("z"):
                fs += low_ch
            elif ord("0") <= ord(low_ch) <= ord("9"):
                fs += low_ch
        s = fs
            
        if len(s)%2 == 0:
            right = len(s)//2
            left = right - 1
        else:
            left = right = len(s)//2
        
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1
        
        return True
        