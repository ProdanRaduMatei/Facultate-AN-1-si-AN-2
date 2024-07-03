import domain.water as Water

class Repository:
    def __init__(self, List=None):
        self.__List = []
        if List is not None:
            for water in List:
                if isinstance(water, Water):
                    self.__List.append(water)
                else:
                    raise ValueError("Not a Team!")

    def addWater(self, pressure, hour_of_day, temperature):
        """
        Add a new measurement.
        :param pressure: water pressure
        :param hour_of_day: hour of day
        :param temperature: water temperature
        :return: water object
        """
        """add a new measurement, measurement validation"""
        ok = True
        if (pressure < 0) or (pressure > 10):
            raise ValueError("Pressure must be between 0 and 10")
        elif (hour_of_day < 0) or (hour_of_day > 23):
            raise ValueError("Hour of day must be between 0 and 0-23")
        elif (temperature < 0) or (temperature > 100):
            raise ValueError("Temperature must be between 0 and 100")
        else:
            water = Water(pressure, hour_of_day, temperature)
            self.__List.append(water)
    
    def getPressureValueGreater(pressure):
        return Repository(filter(lambda water: water.pressure > pressure, self.__List))
    
    def displayAveragePressureAndTemperatureOfHour(hour_of_day):
        #display the average pressure and temperature of a given hour of day
        pressure = 0
        temperature = 0
        cnt = 0
        for water in self.__List:
            if (water.hour_of_day == hour_of_day):
                pressure += water.pressure
                temperature += water.temperature
                ++cnt
        pressure /= cnt
        temperature /= cnt
        print(f"Average pressure for hour {hour_of_day} is: {pressure} Average temperature for hour {hour_of_day} is: {temperature}")

    def __repr__(self):
        return str(self.__List)