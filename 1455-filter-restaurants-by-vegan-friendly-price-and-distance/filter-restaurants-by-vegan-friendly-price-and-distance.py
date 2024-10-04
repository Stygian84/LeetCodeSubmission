class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        restaurants.sort(key=lambda x : (-x[1],-x[0]))

        res = []
        for i,r,v,p,d in restaurants:
            if veganFriendly==1:
                if (v==0) or p>maxPrice or d>maxDistance:
                    continue
                res.append(i)
            else:
                if p>maxPrice or d>maxDistance:
                    continue
                res.append(i)

        
        return res