class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        ans = []
        for i in range(len(s)):
            if s[i] == "":
                continue
            ans.append(s[i])

        return len(ans[-1])
