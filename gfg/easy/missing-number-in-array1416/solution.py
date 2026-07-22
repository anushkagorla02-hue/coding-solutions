class Solution:
    def missingNum(self, arr):
     arr.sort() 
     expect=1# code here
     for num in arr:
         if num != expect:
             return expect
         expect+=1
     return expect
        