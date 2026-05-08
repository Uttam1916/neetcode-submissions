class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0

        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1

        sfreq = {}

        chars = set(t)

        shortest = ""
        minlen = float("inf")

        def valid():
            for ch in freq:
                if sfreq.get(ch, 0) < freq[ch]:
                    return False
            return True

        for r in range(len(s)):

            if s[r] in chars:
                sfreq[s[r]] = sfreq.get(s[r], 0) + 1

            while l <= r and s[l] not in chars:
                l += 1

            while valid():

                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    shortest = s[l:r+1]

                if s[l] in chars:
                    sfreq[s[l]] -= 1

                l += 1

                while l <= r and s[l] not in chars:
                    l += 1

        return shortest