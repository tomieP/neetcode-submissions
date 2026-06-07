class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = []
        maxr = []
        res = []
        n = len(height)
        currR =  height[n-1]
        currL = height[0]

        for i in height:
            if currL < i:
                maxl.append(currL)
                currL = i
            else: maxl.append(currL)
        for i in range(n - 1, -1, -1):
            if currR < height[i]:
                maxr.append(currR)
                currR = height[i]
            else: maxr.append(currR)
        count = 0
        maxr.reverse()
        for i in range(n):
            res.append(min(maxl[i],maxr[i]) - height[i])
            if res[i] < 0: count += 0
            else: count += res[i]

        return count
        