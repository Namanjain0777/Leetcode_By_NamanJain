class Solution:
    
    def gcd(self, a, b):
            if a % b == 0:
                return b
            else:
                return self.gcd(b, a % b)
            
    def hasGroupsSizeX(self, deck):
        
        if len(deck) <= 1:
            return False
        
        counter = dict()
        for i in deck:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        
        if len(counter) == 1:
            return True
        
        g = counter[deck[0]]
        
        for v in counter.values():
            g = self.gcd(g, v)
            if g == 1:
                return False
                
        return True
