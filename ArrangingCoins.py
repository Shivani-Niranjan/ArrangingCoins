
def arrangingCoins(coins):
    i = 0
    stair = 1   # intialized 1 coz to multiply the formula for the first cycle
    while i <= coins:
        i = (stair * (stair+1))/2   # used sum of N numbers formula
        stair +=1
    return stair-2    # -2 coz at first decalred stair = 1 instead of 0 and also stair +=1 increments and only stops so we minus both of that 1s


coins = int(input())
print(arrangingCoins(coins))