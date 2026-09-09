class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []

        for s in strs:
            sizes.append(len(s))
        
        encoded_str = ""
        for size in sizes:
            encoded_str += str(size) + ","

        encoded_str += "#"

        for s in strs:
            encoded_str += s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        start = 0
        curr_size = ""
        sizes = []
        for i in range(len(s)):
            if s[i] == ",":
                sizes.append(int(curr_size))
                curr_size = ""
            elif s[i] == "#":
                start = i + 1
                break
            else:
                curr_size += s[i]
        
        decoded_list = []
        for size in sizes:
            decoded_list.append(s[start : start + size])
            start += size
        
        return decoded_list
        
            
