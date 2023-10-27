#Temperature conversion
class temperature:
    def __init__(self, temp):
        self.temp = temp

    def convertCelcius(self):
        x = self.temp * 9/5+32
        return x
    def convertFahrenheit(self):
        z = self.temp - 32 * 5/9
        return z

temp = temperature(19)
print(temp.convertCelcius())
print(temp.convertFahrenheit())
