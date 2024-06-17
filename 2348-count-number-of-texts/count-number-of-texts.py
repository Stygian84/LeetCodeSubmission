class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n=len(pressedKeys)


        dp=[0]*(max(3,n))
        dp[0]=1
        dp[1]=2
        dp[2]=4

        nine_dp=[0]*(max(4,n))
        nine_dp[0]=1
        nine_dp[1]=2
        nine_dp[2]=4
        nine_dp[3]=8

        for i in range(3,n):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%(10**9+7)
            if i>=4:
                nine_dp[i]=(nine_dp[i-1]+nine_dp[i-2]+nine_dp[i-3]+nine_dp[i-4])%(10**9+7)
            

        total=1
        count=1
        current=pressedKeys[0]
        for i in range(1,n):
            if pressedKeys[i]!=current:
                if current=="9" or current=="7":
                    total*=nine_dp[count-1]
                else:
                    total*=dp[count-1]
                total%=(10**9+7)
                count=1
                current=pressedKeys[i]
            else:
                count+=1
                if i==n-1:
                    if current=="9" or current=="7":
                        total*=nine_dp[count-1]
                    else:
                        total*=dp[count-1]
                    total%=(10**9+7)
                  
        return total
