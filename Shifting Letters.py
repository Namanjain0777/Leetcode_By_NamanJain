class Solution:
    def shiftingLetters(self, s, shifts) :
        self.letters = {chr(97+i):i for i in range(26)}
        ans = ''
        summ = sum(shifts)
        for elm,i in zip(s,shifts):
            ans += self.shift(elm,summ%26)
            summ -= i
        return ans
    
    def shift(self,letter,bit):
        letter = (self.letters[letter] + bit)%26
        return chr(97+letter)
