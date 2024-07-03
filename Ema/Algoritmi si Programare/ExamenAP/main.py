from domain.water import Water
from infrastructure.repository import Repository

wr = Repository(
    [Water(3.3, 10, 55),
     Water(4, 11, 40),
     Water(2.5, 9, 90),
     Water(7.7, 10, 20),
     Water(8.9, 11, 60)]
)

print(wr)
try:
    wr.addWater(5,15,80)
except ValueError as err:
	print(err)


print(wr)
print(wr.getPressureValueGreater(5))

print(wr.displayAveragePressureAndTemperatureOfHour(10))
