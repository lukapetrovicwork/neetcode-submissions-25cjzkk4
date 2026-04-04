class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # frequency map of characters in current window
        left = 0
        max_freq = 0  # max frequency of any char in current window
        max_length = 0
    
        for right in range(len(s)):
            # Add current character to window
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
        
            # Window size - most frequent char count = chars to replace
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                # Note: we don't update max_freq when shrinking
        
            max_length = max(max_length, right - left + 1)
    
        return max_length