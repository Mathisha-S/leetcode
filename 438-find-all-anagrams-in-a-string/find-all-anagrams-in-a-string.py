from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)

        p_count = Counter(p)
        window = Counter(s[:k])

        if window == p_count:
            result.append(0)

        for i in range(k, len(s)):
            window[s[i]] += 1

            left = s[i - k]
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            if window == p_count:
                result.append(i - k + 1)

        return result