class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length_w1 = len(word1)
        length_w2 = len(word2)

        merge_str = ''
        if length_w1 <= length_w2:
            length = length_w1
        else:
            length = length_w2
        
        for i in range(length):
            merge_str += word1[i] + word2[i]
        
        merge_str += word1[i+1:] + word2[i+1:]

        return merge_str
