class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [math.inf]* (n+1)
        dp[0] = 0

        for i in range(1,n+1):
            width = 0
            maxHeight = 0

            for j in range(i-1,-1,-1):
                width += books[j][0]
                if width>shelfWidth:
                    break
                maxHeight = max(maxHeight,books[j][1])
                dp[i] = min(dp[i],dp[j]+maxHeight)
        
        return dp[-1]

        '''n = len(books)

        total = 0
        temp_width = 0
        temp_height = 0

        for w,h in books:
            temp_width += w

            if temp_width > shelfWidth:
                total += temp_height
                temp_width = w
                temp_height = h

            elif temp_width == shelfWidth:
                temp_height = max(h,temp_height)
                total += temp_height
                temp_width = 0
                temp_height = 0
            else:
                temp_height = max(h,temp_height)
            print(w,h,temp_height,temp_width,total)

        if temp_height != 0 and temp_width<shelfWidth:
            total += temp_height
        

        return total'''