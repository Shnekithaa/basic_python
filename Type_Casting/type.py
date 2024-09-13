# - **To convert to Integer datatype** : `int()`
# - **To convert to String datatype** : `str()`
# - **To convert to Float datatype** : `float()`
# - **To convert to Boolean datatype** : `bool()`

unra_number = input()

type_of_unra_number = type(unra_number)
print(type_of_unra_number)

converted_unra_number = int(unra_number)
type_of_converted_unra_number = type(converted_unra_number)
print(type_of_converted_unra_number)

print("Nikitha" + str(20))

unra_peru = input()
unra_vayasu = int(input())
perum_vayasum = unra_peru + " " + str(unra_vayasu)
print(perum_vayasum)