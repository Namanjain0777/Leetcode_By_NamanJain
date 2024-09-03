class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        Palindrome = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            Palindrome = Palindrome * 10 + digit
            temp //= 10

        return Palindrome == x
