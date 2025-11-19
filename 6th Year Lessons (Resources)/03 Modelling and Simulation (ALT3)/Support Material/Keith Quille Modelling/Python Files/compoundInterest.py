


def monthlyRepayment(principalAmount, interest, years):
    T = principalAmount * ((1+interest)** years)
    M = (T / (years * 12))
    return round(M,2)


testCase1 = monthlyRepayment(10000,0.032,6)
print(testCase1)
