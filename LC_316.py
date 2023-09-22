def removeDuplicateLetters(self, s: str) -> str:
        result = []        
        seen = set()

        rightmost = {char: i for i, char in enumerate(s)}
        
        for i, char in enumerate(s):
            if char not in seen:
                while result and char < result[-1] and i < rightmost[result[-1]]:
                    removed_char = result.pop()
                    seen.remove(removed_char)

                result.append(char)
                seen.add(char)
        
        return ''.join(result)