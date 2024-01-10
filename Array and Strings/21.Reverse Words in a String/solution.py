class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = []
        for i in range(len(s)):
            if s[i] == "":
                continue
            ans.append(s[i])

        return " ".join(ans[::-1])