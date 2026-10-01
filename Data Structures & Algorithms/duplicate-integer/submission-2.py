class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # dups = {}

        # for dup in dups:
        #     nums[dup] = dups.get(num, 0) + 1

        # for val in dups.values():
        #     if val > 1:
        #         return True
        #     else:
        #         return False

        st = set()

        for i in range(len(nums)):
            if nums[i] in st:
                return True
            else:
                st.add(nums[i])

        return False



        