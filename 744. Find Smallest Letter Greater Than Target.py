class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # min_letter = ''
        for letter in letters:
            if letter <= target:
                continue
            return letter
            # min_letter = min(min_letter, letter)
        return letters[0]