from collections import deque
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''res=[]

        length=len(words[0])

        dc={}

        #frequency of all words
        for word in words:
            dc[word]=dc.get(word,0)+1
        
        initial_dc=copy.deepcopy(dc)
        #keep track of substring
        queue=deque([])

        for j in range(length):
            left=j
            current=Counter()
        for i in range(0,len(s),length):
            item=s[i:i+length]
            
            # if found, frequency-=1, append to queue
            # else, reset everything
            if item in words:
                queue.append(item)
                dc[item]-=1
            else:
                queue=deque([])
                dc=initial_dc
            print(dc,queue)
            #if length of queue == length of words,
            #append index to res, remove first entry of queue
            if len(queue)==len(words):
                if all(value==0 for value in dc.values()):
                    res.append(i-(length*(len(words)-1)))
                dc[queue.popleft()]+=1

        return res
'''
        if not s or not words:
            return []

        res = []
        word_len = len(words[0])
        total_words_len = word_len * len(words)
        words_count = Counter(words)
        for i in range(word_len):
            left = i
            current = Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                current[word] += 1
                while current[word] > words_count[word]:
                    current[s[left:left+word_len]] -= 1
                    left += word_len
                
                if j - left + word_len == total_words_len:
                    res.append(left)
        
        return res