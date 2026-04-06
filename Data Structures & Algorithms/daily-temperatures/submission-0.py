class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = []
        num_days = len(temperatures)
        stack=[]
        

        for index in range(1, len(temperatures)):
            added = 0
            day = temperatures[index - 1]
            stack.append(day)

            out_of_bounds = False
            while day >= temperatures[index + added]:
                stack.append(temperatures[index + added])
                added += 1

                if index + added > len(temperatures) - 1:
                    out_of_bounds = True
                    break
            if out_of_bounds:
                ret.append(0)
            else:
                ret.append(len(stack))
            stack.clear()

        ret.append(0)
        return ret