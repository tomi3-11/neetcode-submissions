class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        l = 0
        r = n - 1

        while l < r:
            if s[l].lower().strip() == s[r].lower().strip():
                l+=1
                r-=1
            elif not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                return False
        return True
        