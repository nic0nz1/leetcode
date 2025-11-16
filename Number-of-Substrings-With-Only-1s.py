class Solution:
    def numSub(self, s: str) -> int:
        total = 0
        counter = 0
        for char in s:
            if char == "0":
                total += ((counter + 1) * counter)//2
                counter = 0
            else:
                counter += 1
        total += ((counter + 1) * counter)//2
        return total % (10**9 +7)