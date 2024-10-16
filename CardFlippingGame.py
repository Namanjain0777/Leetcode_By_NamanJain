class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """   
        possible_values = set()
        discarded = set()
        for front, back in zip(fronts, backs):
            if front == back:
                discarded.add(front)
            else:
                if front not in possible_values:
                    possible_values.add(front)
                if back not in possible_values:
                    possible_values.add(back)
            
        possible_values -= discarded
        return min(possible_values) if possible_values else 0 
