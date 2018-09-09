def get_nth_prime(goal):
    if goal > 10000000000000:
        return None
    if goal == 1:  # first prime is 2
        return 2
    if goal == 2:  # second prime is 3
        return 3

    chk = 5  # the next odd number after 3, which is already taken care of above
    primes = 2  # the number of primes recorded, after counting 2 and 3.
    while primes < goal:
        if chk < 9:  # if the number is odd and below 9....
            primes += 1  # it's prime
            chk += 2  # and check the next odd number

        else:  # if it's =>9......
            odds = 3  # check to see if it's divisible by the smallest odd number
            sqrtk = chk ** .5  # all the way up to the square root of chk

            while odds < sqrtk or odds == sqrtk:  # if at any time...
                if chk % odds == 0:  # ...chk is divisible by this odd number....
                    chk += 2  # then raise the value of chk to the next odd number
                    break  # and start the check from the beginning with next k
                else:  # if not...
                    # check to see if it's divisible by the next odd number.
                    odds += 2

            # if chk isn't divisible by any odds up to the square root of chk
            if odds > sqrtk:
                primes += 1  # we have a prime number
                chk += 2  # check the next odd number to see if it's prime
                odds = 3  # and reset odds back to 3 to use it next time


    if primes == goal:  # once we've reached the desired amount of prime numbers
        return chk - 2


goal = int(input("Enter a number n, to find the nth prime number."))
print("The", goal, "prime number is:", get_nth_prime(goal))

#Also, the usage is to write your code "that actually does stuff" behind an if main guard so that you can import your code if you want to re-use your function without having any polluting. In your case, it becomes :

def main():
    """Main function"""
    goal = int(input("Enter a number n, to find the nth prime number."))
    print("The", goal, "prime number is:", get_nth_prime(goal))


if __name__ == "__main__":

    main()


