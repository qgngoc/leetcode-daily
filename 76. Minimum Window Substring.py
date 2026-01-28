
def check_included(s_map, t_map):
    for key in t_map.keys():
        if key not in s_map:
            return False
        if s_map[key] < t_map[key]:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 1:
            return s if s == t else ""
        if len(t) == 1:
            return t if t in s else ""

        t_map = {}
        s_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        # check first
        for key in t_map.keys():
            if key not in s_map:
                return ""
            if s_map[key] < t_map[key]:
                return ""
        

        i = 0
        j = 0
        prev_included = False
        candidate = s
        sub_s_map = {s[i]: 1}
        while j < len(s):
            # print(i, j, s[i:j+1])
            if prev_included:
                # print(f"included: {s[i:j+1]}\t{sub_s_map}")
                if j - i + 1 < len(candidate):
                    candidate = s[i:j+1]
                sub_s_map[s[i]] -= 1
                if s[i] in t_map:
                    if sub_s_map[s[i]] < t_map[s[i]]:
                        prev_included = False
                i += 1
            else:
                j += 1
                if j >= len(s):
                    continue
                sub_s_map[s[j]] = sub_s_map.get(s[j], 0) + 1
                prev_included = check_included(sub_s_map, t_map)
        return candidate
            
        