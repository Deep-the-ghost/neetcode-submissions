class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen1 = {}
        seen2 = {}

        for ch in t:
            seen1[ch] = seen1.get(ch, 0) + 1

        l = 0
        have = 0
        need = len(seen1)

        count = float('inf')
        ans = [-1, -1]

        for i in range(len(s)):

            # Add current character
            if s[i] in seen1:
                seen2[s[i]] = seen2.get(s[i], 0) + 1

                if seen2[s[i]] == seen1[s[i]]:
                    have += 1

            # Window is valid
            while have == need:

                # Save smallest window
                if i - l + 1 < count:
                    count = i - l + 1
                    ans = [l, i]

                # Remove left character
                if s[l] in seen1:
                    seen2[s[l]] -= 1

                    if seen2[s[l]] < seen1[s[l]]:
                        have -= 1

                l += 1

        if ans[0] == -1:
            return ""

        return s[ans[0]:ans[1] + 1]