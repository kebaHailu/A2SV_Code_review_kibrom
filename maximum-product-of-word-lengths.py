class Solution:
    def maxProduct(self, words: List[str]) -> int:
        di = defaultdict(int)

        for word in words:
            mask = 0

            for w in word:
                mask |= 1 << (ord(w)-97)
            
            if di.get(mask,0) != 0:
                m = di[mask]
                di[mask] = max(m,len(word))
            else:
                di[mask] = len(word)
    
      
        print(di)
        max_pos = 0

        for i in di:
            for j in di:
                
                if i != j and i & j == 0:
                    max_pos = max(max_pos,di[i]*di[j])
        
        return max_pos