class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X",
              20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC", 100:"C",
              200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM"}
        s = ""
        i = 0
        old = num
        while num > 0:
            a = num % 10
            num = num // 10
            if a*(10**i) in dic:
                s = dic[a*(10**i)] + s
            i += 1
        while old >= 1000:
            s = "M" + s
            old -= 1000
        return s