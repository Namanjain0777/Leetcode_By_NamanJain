class Solution:
	def maxHeightOfTriangle(self, red, blue) :

		r,b,i = 0,1,1
		mini,maxi = min(red,blue), max(red,blue)

		while r <= mini and b <= maxi: 
			i += 1 
			r+=i
			r,b = min(r,b), max(r,b)
		return i-1
