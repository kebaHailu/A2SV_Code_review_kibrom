class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        target = Counter(p)
        window = Counter(s[:len(p)])
        
        left = 0
        right = len(p)
        
        arr = []
        
        while right < len(s):
            
            if target == window:
                arr.append(left)
            
            window[s[left]] -= 1 
            if window[s[left]] == 0:
                del window[s[left]] 
            window[s[right]] += 1 
            
            left += 1
            right += 1
        
        if target == window:
            arr.append(left)
            
        return arr
                
                
