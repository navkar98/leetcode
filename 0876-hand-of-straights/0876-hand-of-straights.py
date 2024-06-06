class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n%groupSize != 0:
            return False

        counter = {}
        unique_card = set()

        for i in hand:
            if i not in counter:
                counter[i] = 1
                unique_card.add(i)
            else:
                counter[i] += 1

        unique_card = list(unique_card)

        heapq.heapify(unique_card)
        curr_len = 0
        last = inf

        while unique_card:
            # print(last, counter)
            if last == inf:
                while unique_card and counter[unique_card[0]] <= 0:
                    heapq.heappop(unique_card)
                
                if unique_card:
                    last = unique_card[0]
                    counter[last] -= 1
                    curr_len += 1
            else:
                if last + 1 not in counter or (last + 1 in counter and counter[last + 1] <= 0):
                    return False
                else:
                    counter[last + 1] -= 1
                    last = last + 1
                    curr_len += 1

            if curr_len == groupSize:
                curr_len = 0
                last = inf

        return True