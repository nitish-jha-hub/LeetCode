class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        finalfine = 0
        if date % 2 == 0:
            print("even")
            for pos, finers in enumerate(car):
                if finers %2 !=0:
                    print(fine[pos])
                    finalfine += fine[pos]
        else:
            print("odd")
            for pos, finers in enumerate(car):
                if finers %2 ==0:
                    finalfine += fine[pos]
        return finalfine
date = 5
car = [12,13, 11, 4, 5, 19, 2, 8, 7, 12, 5]
fine = [10, 10, 20, 17, 15, 12, 13, 9, 1, 3, 1]
solution1 = Solution()
print(solution1.totalFine(date,car,fine))