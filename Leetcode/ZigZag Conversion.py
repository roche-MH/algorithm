Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lin = 0
        pl =1
        output = [""] * numRows
        for i in range(len(s)):
            output[lin] +=s[i]
            if numRows > 1:
                lin +=pl
                if lin == 0 or lin==numRows -1:
                    pl*=-1
        return ''.join(output)