class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        while i < len(s)-1:
            if s[i:i+2] == "IV":
                ans += 4
                i += 2
            elif s[i:i+2] == "IX":
                ans += 9
                i += 2
            elif s[i:i+2] == "XL":
                ans += 40
                i += 2
            elif s[i:i+2] == "XC":
                ans += 90
                i += 2
            elif s[i:i+2] == "CD":
                ans += 400
                i += 2
            elif s[i:i+2] == "CM":
                ans += 900
                i += 2
            elif s[i] == "I":
                ans += 1
                i += 1
            elif s[i] == "V":
                ans += 5
                i += 1
            elif s[i] == "X":
                ans += 10
                i += 1
            elif s[i] == "L":
                ans += 50
                i += 1
            elif s[i] == "C":
                ans += 100
                i += 1
            elif s[i] == "D":
                ans += 500
                i += 1
            elif s[i] == "M":
                ans += 1000
                i += 1
        if i < len(s):
            if s[i] == "I":
                ans += 1
                i += 1
            elif s[i] == "V":
                ans += 5
                i += 1
            elif s[i] == "X":
                ans += 10
                i += 1
            elif s[i] == "L":
                ans += 50
                i += 1
            elif s[i] == "C":
                ans += 100
                i += 1
            elif s[i] == "D":
                ans += 500
                i += 1
            elif s[i] == "M":
                ans += 1000
                i += 1
        return ans
