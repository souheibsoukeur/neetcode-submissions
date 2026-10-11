class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        def freqana(word): 
            arrr = [0] * 26 
            for c in word: 
                n = ord(c) - 97 
                arrr[n] += 1
            return tuple(arrr) 
        
        hass = {} 
        
        for word in strs: 
            key = freqana(word)
            
            if key not in hass:
                hass[key] = [word]  
            else:
                hass[key].append(word) 
        return list(hass.values())