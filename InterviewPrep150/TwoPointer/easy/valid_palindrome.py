class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution with ASCII code (I think it's not a Two Pointers method)
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                i += 1
                continue
            c = ord(s[i])
            if 64 < c and c < 91:
                c += 32
                s = s[0:i] + chr(c) + s[i+1:]
                i += 1
            elif 96 < c and c < 123:
                i += 1
            else:
                s = s[0:i] + s[i+1:]
        print(s)
        
        start = 0
        end = len(s) - 1
        flag = True
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                flag = False
                break
          
        return flag

    def isPalindrome2(self, s:str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isdigit() or checkValid(s[i]):
                if s[j].isdigit() or checkValid(s[j]):
                   if s[i] == s[j]:
                       i += 1
                       j -= 1 
            else:
                i += 1
            
    def checkValid(self, item) -> bool:
        c = ord(item)
        if 64 < c and c < 91:
            return True
        elif 96 < c and c < 123:
            return True
        else:
            return False
            

sol = Solution()
a = "\"Stop!\" nine myriad murmur. \"Put up rum, rum, dairymen, in pots.\""
print(sol.isPalindrome(a))