class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start_times =  sorted([x[0] for x in intervals], key=lambda x:x)
        end_times = sorted([x[1] for x in intervals], key=lambda x:x)

        start_ptr = 0
        end_ptr = 0
        
        
        count = 0
        while start_ptr < len(intervals):
            if start_times[start_ptr] < end_times[end_ptr]:
                start_ptr += 1
                count += 1
            else:
                end_ptr += 1
                start_ptr += 1

        return count
