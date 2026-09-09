class Solution:

    def encode(self, strs: List[str]) -> str:
        self.key = "&%$^"

        encoded_str = ""
        for s in strs:
            encoded_str += self.key + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        return s.split(self.key)[1:]
