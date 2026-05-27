class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for word in strs:
            if word:
                for char in word:
                    ch = str(ord(char) + 10)
                    result = result+"."+ch
            else:
                result = result + "em"
            result = result + "|"
        print("result",result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        words = s.split("|")
        print("decoded",words)
        for word in words:
            if word:
                if word == "em":
                    decoded_word = ""
                else:
                    decoded_word = ""
                    print("char",word)
                    char_split = word.split(".")
                    for ch in char_split:
                        if ch:
                            decoded_word += (chr(int(ch)-10))
                result.append(decoded_word)
        print(result)
        return result

        
