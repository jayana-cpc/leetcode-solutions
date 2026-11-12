class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(' ')
        res = ""
        butLast = list(reversed(words))[0:len(words) - 1]
        print(butLast)
        for word in butLast:
            if not word.isspace() and len(word) != 0:
                print(word)

                res += word + " "
        print(res)
        if not list(reversed(words))[-1].isspace() and len(list(reversed(words))[-1]) != 0:
            res += list(reversed(words))[-1]
        return res
        