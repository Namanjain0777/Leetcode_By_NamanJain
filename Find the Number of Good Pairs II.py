class Solution:
    def numberOfPairs(self, nums1, nums2, k) :
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for x in nums1:
            if x % k == 0:
                f = x // k
                map1[f] += 1

        for x in nums2:
            map2[x] += 1

        res = 0
        for x, y in map1.items():
            for i in range(1, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    cur = x // i
                    if i in map2:
                        res += map2[i] * y
                    if cur != i and cur in map2:
                        res += map2[cur] * y

        return res
