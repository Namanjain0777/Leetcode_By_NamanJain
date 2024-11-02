class Solution(object):
    def minimumAbsDifference(self, arr):
        arr=sorted(arr)
        l1=[]
        mindiff=float('inf')
        for i in range(1,len(arr)):
            ans=arr[i]-arr[i-1]
            if ans<mindiff:
                mindiff=ans
                l1=[[arr[i-1],arr[i]]]
            elif ans==mindiff:
                l1.append([arr[i-1],arr[i]])
        return l1
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
