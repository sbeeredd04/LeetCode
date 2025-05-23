class Solution:
    def tribonacci(self, n: int) -> int:
        
        #dict to store all the t values
        nums = {
            "t0" : 0, 
            "t1" : 1, 
            "t2" : 1
        }

        #first define a recursive function
        def fun(x) : 

            #if the number is greater than 2 then call the recursive function
            trib = "t" + str(x)

            #base case
            if x > 2 : 

                #if the number is already in the dictionary then return then result
                if trib in nums : 
                    return nums[trib]

                else :
                    #call the function
                    result = fun(x-3) + fun(x-2) + fun(x-1)         
                    nums[trib] = result

                    return result

            #if n is less than 2 then return the value from dict
            else : 
                return nums[trib]


        #call the function
        return fun(n)

if __name__ == "__main__" :
    sol = Solution()
    n = 4
    print(f"Tribonacci of {n} is: {sol.tribonacci(n)}")  # Output: 4
    n = 25
    print(f"Tribonacci of {n} is: {sol.tribonacci(n)}")  # Output: 1389537
    n = 30
    print(f"Tribonacci of {n} is: {sol.tribonacci(n)}")  # Output: 2082876103
    n = 35
    print(f"Tribonacci of {n} is: {sol.tribonacci(n)}")  # Output: 1214152903