class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        num = 0
        for i in range(
            1, len(s)
        ):
            if num_dict.get(s[i-1]) >= num_dict.get(s[i]):
                num += num_dict.get(s[i-1])
            else:
                num -= num_dict.get(s[i-1])
        num += num_dict.get(s[-1])

        return num
