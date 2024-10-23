class wordDictNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = wordDictNode()
        self.wordcheck = []

    def addWord(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = wordDictNode()
            cur = cur.children[w]
        cur.endofWord = True
                
    def search(self, word): 
        
        def dfs(node, word):
            if len(word)==0:
                return True if node.endofWord else False
            elif word[0]!='.' and word[0] not in node.children:
                return False
            
            if word[0]=='.':
                for child in node.children.values():
                    if dfs(child, word[1:]): 
                        return True
            else:
                return dfs(node.children[word[0]], word[1:])
           
        
        if word in self.wordcheck:
            return True
    
        if dfs(self.root, word):
            self.wordcheck.append(word)
            return True
        else:
            return False
