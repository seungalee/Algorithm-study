class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #딕셔너리 사용?
        #계속 차례로 순회하는 건 최악의 경우 O(n^2)이라 너무 비효율적이지 않을까
        #시간초과 코드

        # max_temp = max(temperatures)
        # output = [0]*len(temperatures)

        # for i in range(len(temperatures)-1):
        #     if temperatures[i] == max_temp:
        #         output[i] = 0    
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             output[i] = j-i
        #             break
        # output[len(temperatures)-1] = 0
        # return output

        output = [0]*len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                output[last] = i - last
            stack.append(i)
        return output