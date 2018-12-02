def m13(n):
    x = str(a)
    A = list(x)
    ans = 1
    for i in range(0,986):
        num = int(A[i])*int(A[i+1])*int(A[i+2])*int(A[i+3])*int(A[i+4])*int(A[i+5])*int(A[i+6])*int(A[i+7])*int(A[i+8])*int(A[i+9])*int(A[i+10])*int(A[i+11])*int(A[i+12])
        if num>ans:
            ans = num
    return ans
