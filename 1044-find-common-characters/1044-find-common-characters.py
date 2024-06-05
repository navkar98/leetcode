class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        overall_dict = {}
        n = len(words)
        first_word = True

        for word in words:
            local_dict = {}
            remove = []

            for char in word:
                if char in local_dict:
                    local_dict[char] += 1
                else:
                    local_dict[char] = 1
            
            for i in overall_dict:
                if i not in local_dict:
                    remove.append(i)
                else:
                    overall_dict[i] = min(overall_dict[i], local_dict[i])

            for i in remove:
                del overall_dict[i]

            if first_word:
                overall_dict = local_dict
                first_word = False

        ans = []
        # print(overall_dict)

        for i in overall_dict:
            for _ in range(overall_dict[i]):
                ans.append(i)

        return ans