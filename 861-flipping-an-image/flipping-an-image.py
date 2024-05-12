class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        for idx in range(len(image)):
            image[idx].reverse()
            for i in range(len(image[idx])):
                image[idx][i]=1-image[idx][i]

        return image