from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi(name='Hummer', fuel=100, fanciness=4)
print(str(hummer))

silver = SilverServiceTaxi(name='silver taxi', fuel=100, fanciness=2)
silver.drive(18)
print(silver.get_fare())
