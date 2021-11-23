class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda x:x[0])
        

        previous_end = 0
        
        for interval in intervals:
            if interval[0] >= previous_end:
                previous_end = interval[1]
            else:
                return False
        
        return True
