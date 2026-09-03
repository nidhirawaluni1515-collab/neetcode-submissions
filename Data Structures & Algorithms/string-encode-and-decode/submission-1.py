class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs :
            res += str(len(s)) + "#" + s
        return res     
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s) :
            k = i
            while s[k] != "#" :
                 k += 1
            lenght = int(s[i:k])     
            i = k + 1 
            j = lenght + i 
            res.append(s[i:j])
            i = j 
        return res