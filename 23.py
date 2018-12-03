def is_abundant(n):
    
    def divisors(n):
        divs = [i for i in range(1,round(n/2)+1) if n%i == 0]
        return divs
    
    if sum(divisors(n)) > n:
        return True
    else:
        return False
    
ab_nums = [n for n in range(2,28123) if is_abundant(n)]

def all_sums(nums):
    def ab_sum(n, nums):
        ans = [n + nums[i] for i in range(len(nums)) if n + nums[i] < 28123]
        return ans
    res  = [ab_sum(nums[i], nums) for i in range(len(nums))]
    return res
    
a = all_sums(ab_nums)

ans = []
b = [[ans.append(i) for i in row if i not in ans] for row in a]

answer = [i for i in range(1,28124) if i not in ans]

sum(answer)
4207994

#close. right ans is 4179871
