class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_key='a'
        longest_duration=0
        releaseTimes=[0]+releaseTimes
        for idx in range(len(keysPressed)):
            duration=releaseTimes[idx+1]-releaseTimes[idx]
            if duration >= longest_duration:

                if duration==longest_duration:
                    if ord(keysPressed[idx])>ord(longest_key):
                        longest_key=keysPressed[idx]
                else:
                    longest_key=keysPressed[idx]
                longest_duration=duration

        return longest_key