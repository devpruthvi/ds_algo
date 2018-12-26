import random
heights = [random.randint(1, 10) for i in range(10)]
# heights = [8, 9, 7, 3, 5, 2, 2, 7, 10, 3]
def getMaxRectInHistogram(heights):
    s = []
    maxRect = 0

    for i,h in enumerate(heights):
        if len(s) == 0 or h >= heights[s[-1]]:
            s.append(i)
            i += 1
        else:
            while len(s) != 0 and heights[s[-1]] > h:
                top = s.pop(-1)
                curRect = heights[top] * ((i - s[-1] - 1) if len(s) != 0 else i)
                maxRect = max(maxRect, curRect)
            s.append(i)
    if len(s) != 0:
        while len(s) > 0:
            top = s.pop(-1)
            curRect = heights[top] * ((len(heights) - s[-1] - 1) if len(s) != 0 else len(heights))
            maxRect = max(maxRect, curRect)
    return maxRect

print(getMaxRectInHistogram(heights))
