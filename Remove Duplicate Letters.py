class Solution:
    def removeDuplicateLetters(self, s):
        char_last_occ_idx_map = {}
        for i in range(len(s)):
            char_last_occ_idx_map[s[i]] = i
        stack = []
        used = set()
        for i in range(len(s)):
            if s[i] in used:
                continue
            while stack and stack[-1] > s[i] and char_last_occ_idx_map[stack[-1]] > i :
                used.remove(stack[-1]) 
                stack.pop() 
            if s[i] not in used:
                stack.append(s[i])
                used.add(s[i])
        
        return ''.join(stack)
