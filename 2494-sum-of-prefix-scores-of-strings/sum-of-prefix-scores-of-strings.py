class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        #trie = {}
        #TODO
        
        def insert(trie, word):
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {"count": 0}
                node = node[char]
                node["count"] += 1

        def calculate_prefix_score(trie, word):
            node = trie
            score = 0
            for char in word:
                if char in node:
                    node = node[char]
                    score += node["count"]
            return score

        def sum_prefix_scores(words):
            trie = {}
            
            for word in words:
                insert(trie, word)
            
            result = []
            for word in words:
                result.append(calculate_prefix_score(trie, word))
            
            return result

        return sum_prefix_scores(words)