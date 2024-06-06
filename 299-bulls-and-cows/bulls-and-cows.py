class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        new_secret,new_guess={},{}
        for s,g in zip(secret,guess):
            if s==g:
                bull+=1
            else:
                new_secret[s]=new_secret.get(s,0)+1
                new_guess[g]=new_guess.get(g,0)+1
        for key,values in new_guess.items():
            curr_values=values
            while key in new_secret and new_secret[key]>0 and curr_values>0:
                new_secret[key]-=1
                cow+=1
                curr_values-=1

        

        return str(bull)+"A"+str(cow)+"B"
        