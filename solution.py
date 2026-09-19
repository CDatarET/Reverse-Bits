class Solution:
    def reverseBits(self, n: int) -> int:
        rev = []
        while n > 0:
            rev.append(str(n % 2))
            n //= 2
        
        while len(rev) < 32:
            rev.append('0')
        
        print(rev)
        return int("".join(rev), 2)
