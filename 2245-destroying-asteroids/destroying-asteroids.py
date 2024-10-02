class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        n=len(asteroids)
        for i in range(n):
            if asteroids[i]<=mass:
                mass+=asteroids[i]
            else:
                return False
        return True