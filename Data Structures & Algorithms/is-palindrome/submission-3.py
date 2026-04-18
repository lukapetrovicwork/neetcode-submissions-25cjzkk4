import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        clean = s.translate(str.maketrans('', '', string.punctuation))

        l, r = 0, len(clean) - 1

        while l < r:
            if clean[l].lower() == clean[r].lower():
                l = l + 1
                r = r - 1
            else:
                return False

        return True