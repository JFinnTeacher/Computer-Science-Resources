def tempModel(hour, startTemp):
    if hour < 12:
        return startTemp + hour
    elif hour == 12:
        return startTemp + 11
    else:
        return (startTemp + 11) - (hour - 12)

temp = tempModel(21,5)
print(temp)