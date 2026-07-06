class Solution:
    def isAnagram(self, string1, string2):
        return sorted(list(string1)) == sorted(list(string2))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output: List[List[str]] = []
        length = len(strs)

        strs_sorted = list(map(lambda a : sorted(list(a)), strs))

        while(length != 0):

            temp: str = strs[0]
            temp_sorted = strs_sorted[0]

            local: List[str] = [temp]

            strs.remove(temp)
            strs_sorted.remove(temp_sorted)

            length = length-1 # remove an element as it is checked

            for j in range(0, length): # look at all elements onwards

                if j >= length:
                    break

                temp2: str = strs[j]
                temp2_sorted = strs_sorted[j]

                if temp_sorted == temp2_sorted:
                    local.append(temp2)
                    strs.remove(temp2)
                    strs_sorted.remove(temp2_sorted)

                    length = length-1

            isInOut = False

            for i in range(0, len(output)):
                arr: List[str] = output[i]
                if self.isAnagram(temp, arr[0]):
                    arr += local
                    isInOut = True
                    break
            
            if not isInOut:
                output.append(local)

        return output

    