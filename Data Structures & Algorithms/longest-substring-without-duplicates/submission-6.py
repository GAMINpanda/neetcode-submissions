class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer1 = 0
        pointer2 = 1
        length = len(s)
        if length == 0:
            return 0
        cur_substring = [s[0]]
        max_ = 1
        # slide pointers over string until a new character is found
        # if it is, store value before and start pointers from where the previous
        # char is

        while pointer2 != length:
            char1 = s[pointer2]
            #print(cur_substring)

            if char1 not in cur_substring:
                cur_substring.append(char1)
                pointer2 += 1
            else:
                char_index = cur_substring.index(char1)
                pointer1 += char_index + 1
                cur_substring = cur_substring[char_index + 1:]
                cur_substring.append(char1)
                pointer2 += 1

            max_ = max(max_, pointer2 - pointer1)

        return max_

        