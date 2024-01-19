class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        y = 0
        x = str(n)
        while x!="1":
            for cher in x:
                numone = int(cher) * int(cher)
                y = y + numone
            s.add(x)
            x = str(y)
            y = 0
            if x in s:
                return False
                break
        return True