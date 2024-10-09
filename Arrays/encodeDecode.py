class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        for word in strs:
            s += word + "1234567890"
        
        return s


    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        arr = s.split("1234567890")
        arr.pop()
        return arr