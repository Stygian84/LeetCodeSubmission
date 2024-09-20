class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #front
        hour_angle = minutes/60*30 + (hour-12 if hour>=12 else hour) * 30
        minute_angle = minutes/60*360

        return min(abs(hour_angle-minute_angle),360-abs(hour_angle-minute_angle))