class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        possible_words = set()

        for word in startWords:
            sorted_word = ''.join(sorted(word))
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char not in word:
                    new_word = ''.join(sorted(word + char))
                    possible_words.add(new_word)

        count = 0
        for target in targetWords:
            if ''.join(sorted(target)) in possible_words:
                count += 1

        return count