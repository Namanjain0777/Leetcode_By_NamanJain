class Solution:
    def secondHighest(self, s):
        toStandart = "".join(list(filter(lambda x : x.isdigit(), list(set(s)))))
        if len(toStandart) < 2 :
            return -1
        return sorted(list(map(int, list(toStandart))), reverse=True)[1]
