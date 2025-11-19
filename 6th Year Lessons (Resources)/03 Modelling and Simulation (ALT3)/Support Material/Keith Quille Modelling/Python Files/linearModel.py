



def predictWeather(morningTemperature, morningLimit= 20):
    if morningTemperature < morningLimit:
        return "Bad"
    else:
        return "Good"

prediction = predictWeather(14,12)
print(prediction)