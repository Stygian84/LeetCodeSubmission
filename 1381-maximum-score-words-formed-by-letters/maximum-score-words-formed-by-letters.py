class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def calculate_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)

        def backtrack(index, remaining_letters):
            if index == len(words):
                return 0
            
            max_score = backtrack(index + 1, remaining_letters)
            
            word = words[index]
            word_count = Counter(word)
            can_include = True
            for char in word_count:
                if word_count[char] > remaining_letters[char]:
                    can_include = False
                    break
            
            if can_include:
                new_remaining_letters = remaining_letters - word_count
                score_with_word = calculate_score(word) + backtrack(index + 1, new_remaining_letters)
                max_score = max(max_score, score_with_word)
            
            return max_score
        
        letter_count = Counter(letters)
        return backtrack(0, letter_count)