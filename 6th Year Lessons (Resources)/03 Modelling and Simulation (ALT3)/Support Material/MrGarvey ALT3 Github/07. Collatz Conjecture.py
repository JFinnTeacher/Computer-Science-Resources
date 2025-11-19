# https://en.wikipedia.org/wiki/Collatz_conjecture
# Collatz Conjecture
# That applying two simple arithmetic operations will eventually convert any positive integer into 1.
# If the integer is even then the next term is half the previous term.
# If the integer is odd then the next term is 3*previous term  +1
# And while no one has proved the conjecture, it has been verified for every number less than 268.
# So if you're looking for a counterexample, you can start around 300 quintillion.

# Possible simulations:
# What number between 2 and 100 will take the longest to reach 1?

# Are the Collatz sequences for starting numbers that are powers of two (2, 4, 8, 16, 32, 64, 128, on so on)
# always composed of only even numbers (aside from the final 1)?

# Do the number of steps needed to reach 1 keep increasing as the input integer gets bigger?


user_in=int(input('Enter a number: '))

while user_in!=1:
    if user_in%2==0:
        user_in=user_in//2
        print(user_in)
    elif user_in%2!=0:
        user_in=(user_in*3)+1
        print(user_in)
    elif user_in==1:
        break
