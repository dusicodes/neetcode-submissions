class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string +=  word + ":,/."
        return string
    def decode(self, s: str) -> List[str]:
        result = s.split(":,/.")
        result.pop()
        return result