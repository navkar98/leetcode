class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        data = [(pos, health, direction, idx) for idx, (pos, health, direction) in enumerate(zip(positions, healths, directions))]
        data.sort()
        to_add = True

        stack = []
        for pos, health, direction, idx in data:
            if stack and stack[-1][2] != direction:
                while stack and stack[-1][2] == 'R' and direction == 'L':
                    if health > stack[-1][1]:
                        stack.pop()
                        health -= 1
                    elif health == stack[-1][1]:
                        stack.pop()
                        to_add = False
                        break
                    else:
                        curr_pos, curr_health, curr_direction, curr_idx = stack.pop()
                        stack.append((curr_pos, curr_health - 1, curr_direction, curr_idx))
                        to_add = False
                        break
                
                if to_add:
                    stack.append((pos, health, direction, idx))
                to_add = True
            else:
                stack.append((pos, health, direction, idx))

        stack.sort(key=lambda x: x[3])
        return [i[1] for i in stack]