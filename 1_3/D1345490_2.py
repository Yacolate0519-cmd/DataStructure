class Solution:
    def __init__(self, s):
        self.s = s

    def orderlyQueue(self, k):
        if k > 1: 
            return ''.join(sorted(self.s))
        else:
            for i in range(len(self.s)):
                rotated = self.s[i:] + self.s[:i]
                selfMin = min(self.s, rotated)
            return selfMin

if __name__ == "__main__":
    data = "baaca"
    result = Solution(data)
    print(result.orderlyQueue(3))

    data2 = 'acb'
    result = Solution(data2)
    print(result.orderlyQueue(-1))