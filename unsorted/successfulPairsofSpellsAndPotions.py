from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = []
        
        for spell in spells:
            # Find minimum potion needed: success/spell
            target = (success + spell - 1) // spell  # Ceiling division
            # Find index of first potion >= target
            index = bisect.bisect_left(potions, target)
            pairs.append(m - index)
        
        return pairs
