def largestRectangleArea(heights):
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                tmp = stack.pop()
                res = max(res, heights[tmp]*(i-stack[-1]-1))
            stack.append(i)
        return res
