class Water:
    def __init__(self, pressure, hour_of_day, temperature):
        if (pressure < 0) or (pressure > 10):
            raise ValueError("Pressure must be between 0 and 10")
        else:
            self.__pressure = pressure
        if (hour_of_day < 0) or (hour_of_day > 23):
            raise ValueError("Hour of day must be between 0 and 23")
        else:
            self.__hour_of_day = hour_of_day
        if (temperature < 0) or (temperature > 100):
            raise ValueError("Temperature must be between 0 and 100")
        else:
            self.__temperature = temperature
    
    @property
    def pressure(self):
        return self.__pressure
    @property
    def hour_of_day(self):
        return self.__hour_of_day
    @property
    def temperature(self):
        return self.__temperature
    @pressure.setter
    def pressure(self, pressure):
        if (pressure < 0) or (pressure > 10):
            raise ValueError("Pressure must be between 0 and 10")
        else:
            self.__pressure = pressure
    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        if (hour_of_day < 0) or (hour_of_day > 23):
            raise ValueError("Hour of day must be between 0 and 23")
        else:
            self.__hour_of_day = hour_of_day
    @temperature.setter
    def temperature(self, temperature):
        if (temperature < 0) or (temperature > 100):
            raise ValueError("Temperature must be between 0 and 100")
        else:
            self.__temperature = temperature
    
    @pressure.getter
    def pressure(self):
        return self.__pressure
    
    @hour_of_day.getter
    def hour_of_day(self):
        return self.__hour_of_day
    
    @temperature.getter
    def temperature(self):
        return self.__temperature
    
    def __repr__(self):
        return f"Water(pressure={self.__pressure}, hour_of_day={self.__hour_of_day}, temperature={self.__temperature})"
    
    