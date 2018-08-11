import uuid;

class Codec:

	def __init__(self):
		self.hash = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = uuid.uuid4().hex.upper()[0:6]
        self.hash[key] = longUrl;
        return "http://tinyurl.com/" + key
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.replace("http://tinyurl.com/","")
        url = self.hash[key]
        del self.hash[key]
        return url

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
#Encode and Decode TinyURL
#https://leetcode.com/problems/encode-and-decode-tinyurl/description/