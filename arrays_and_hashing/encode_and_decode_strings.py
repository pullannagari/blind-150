class Solution:

    def encode(self, strs: 'list[str]') -> str:
        result = ""
        for s in strs:
            prefix = str(len(s))+":"
            curr_s = prefix+s
            result += curr_s
        return result

    def decode(self, s: str) -> 'list[str]':
        i = 0
        result = []
        if s == "":
            return result
        while i < len(s):
            s_len, j = 0, i
            while j < len(s):
                if s[j] == ":":
                    s_len = int(s[i:j])
                    break
                j += 1
            curr = s[j+1: j+1+s_len]
            result.append(curr)
            i = j+1+s_len
        return result
            

