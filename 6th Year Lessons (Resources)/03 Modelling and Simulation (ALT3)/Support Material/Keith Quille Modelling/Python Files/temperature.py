


def temperatureModel(hour, startTemp = 5):
    if hour < 12:
        return startTemp + hour
    elif hour == 12:
        return startTemp + 11
    else:
        return (startTemp + 11) - (hour - 12)

temp = temperatureModel(20)
print(temp)