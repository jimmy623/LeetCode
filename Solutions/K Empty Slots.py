class Solution(object):
    def kEmptySlots(self, flowers, k):
        active = []
        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1

#K Empty Slots
#https://leetcode.com/problems/k-empty-slots/description/