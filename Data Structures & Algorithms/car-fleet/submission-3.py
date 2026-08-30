class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_ = {}

        for i, el in enumerate(position):
            speed_[el] = speed[i]

        position.sort(reverse=True)

        num_fleets = 0
        prev_time = 0

        for pos in position:
            cur_time = (target - pos) / speed_[pos]

            if cur_time > prev_time:
                num_fleets += 1
                prev_time = cur_time

        return num_fleets

        