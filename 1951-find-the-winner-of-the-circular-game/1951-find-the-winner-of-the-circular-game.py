class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        ptr = 0
        length = n

        while length > 1:
            # print(arr, ptr, ptr + k - 1)
            if ptr + k - 1 >= length:
                ptr = (k - (length - ptr) - 1) % length
                arr.pop(ptr)
            else:
                ptr = ptr + k - 1
                arr.pop(ptr)

            length -= 1

        return arr[0]
