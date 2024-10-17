class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        dd={k[0]:k[1] for k in knowledge }
        res=[]; NoBr=True; kkey=''
        for i,s1 in enumerate(s):
            if s1=='(':
                kkey=''
                NoBr = False
            elif NoBr:
                res.append(s1)
            elif s1==')':
                if kkey in dd:
                    res.append(dd[kkey])
                else:
                    res.append("?")
                NoBr = True
            elif not NoBr:
                kkey += s1
        return ''.join(res)
