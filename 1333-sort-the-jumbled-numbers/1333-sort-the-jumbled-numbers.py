class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new_nums = []

        def update_num(number):
            if number == 0:
                return mapping[number]

            new_num = 0
            lev = 1
            while number > 0:
                digit = number%10
                new_num += (mapping[digit]) * lev
                number //= 10
                lev *= 10

            return new_num      

        for i in nums:
            new_nums.append(update_num(i))

        nums = sorted(list(zip(new_nums, nums)), key = lambda i: i[0])
        
        return [j for i,j in nums]