from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        result = []
        
        for i in range(max_length):
            curr_word = ""
            
            for word in words:
                if i < len(word):
                    curr_word += word[i]
                else:
                    curr_word += " "
            
            curr_word = curr_word.rstrip()  
            result.append(curr_word)
        
        return result