class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            freq = [0] * 26
            for l in word:
                freq[ord(l) - ord('a')] += 1
            freq = tuple(freq)
            if freq in anagram_map:
                anagram_map[freq].append(word)
            else:
                anagram_map[freq] = [word]

        return list(anagram_map.values())