# Asling-20190513
# best RT: 36 ms, faster than 97.53%
#      MU: 13.1 MB, less than 5.53%

'''
0050:Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

# 递归 [36ms & 13.1MB]
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0):return 1
        elif(n < 0):
            ans = self.myPow(x,-n)
            return 1/ans
        elif(n == 1):return x
        elif(n%2 == 1):
            ans = self.myPow(x*x,(n-1)/2)
            return ans*x
        elif(n%2 == 0):
            ans = self.myPow(x*x,n/2)
            return ans

# Python 自带pow [36ms & 13.2MB]
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)

# math.pow [40ms & 13.5MB]
import math
class Solution3:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x,n)

# 非递归 [36ms & 13.4MB]
class Solution4:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        flag = n
        if(n == 0):return 1
        elif(n < 0):n = -n

        while int(n/2) > 0:
            if(n%2 > 0):
                ans *= x
            x *= x
            n = int(n/2)

        if(flag < 0):
            return 1/(x*ans)
        
        return x*ans