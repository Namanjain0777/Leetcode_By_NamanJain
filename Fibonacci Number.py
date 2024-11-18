class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        fiz,prev = self.Fibbo(n)
        return fiz
    
    def Fibbo(self,n):
        if n == 1:
            return 1,0
        else:
            x,y = self.Fibbo(n-1)
            return x+y,x
        
