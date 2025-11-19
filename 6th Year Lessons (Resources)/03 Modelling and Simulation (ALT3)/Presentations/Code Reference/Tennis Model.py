def playTennis(outlook, humidity, wind):
    if outlook == "sunny":
        if humidity == "high":
            return False
        else:
            return True
    elif outlook == "overcast":
        return True
    else:
        if wind == "strong":
            return False
        else:
            return True


willIPlayTennis = playTennis("sunny", "high", "weak")

if willIPlayTennis:
    print("Yes, go play")
else:
    print("Not today")