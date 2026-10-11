import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hass = collections.defaultdict(list)
        
        for word in strs:
            # sorted(word) turns "eat" into ['a', 'e', 't']
            # We must turn it into a tuple so it can be a dictionary key
            key = tuple(sorted(word))
            
            # Group it!
            hass[key].append(word)
            
        return list(hass.values())