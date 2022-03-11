from unicodedata import name
from unreliable_car import UnreliableCar

unreliable = UnreliableCar(name='Camry_unreliable', fuel=100, reliability=10)

unreliable.drive(10)
unreliable.drive(10)
unreliable.drive(10)
