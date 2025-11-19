def monthlyRepayment(principalAmount, interest, years):
    finalAmount = principalAmount * ((1+interest)**years)
    monthlyAmount = (finalAmount / (years * 12))
    return round(monthlyAmount,2)

testCase1 = monthlyRepayment(10000, 0.032, 6)
print(testCase1)
    