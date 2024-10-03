class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = "1"

        for _ in range(n - 1):
            str_out = ""
            prev_char = out[0]
            count = 1

            for j in range(1, len(out)):
                if out[j] == prev_char:
                    count += 1
                else:
                    str_out += str(count) + prev_char
                    prev_char = out[j]
                    count = 1

            str_out += str(count) + prev_char
            out = str_out

        return out
