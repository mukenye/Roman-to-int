class Solution:
    def romanToInt(self, s: str) -> int:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        total = 0
        for char in s:
            if char == 'IV':
                total += 4
            elif char == 'XC':
                total += 90
            if char == 'CM':
                total += 900
            else:
                if char == 'I':
                    total += 1
                elif char == 'V':
                    total += 5
                elif char ==  'X':
                    total += 10
                elif char == 'L':
                    total += 50
                elif char == 'C':
                    total += 100
                elif char == 'D':
                    total += 500
                elif char == 'M':
                    total += 1000

        
        return total
