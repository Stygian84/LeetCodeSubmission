class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result=[first]
        for idx in range(len(encoded)):
            result.append(result[idx]^encoded[idx])
        return result