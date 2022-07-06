# If in ur python environment doesn't have country module, should pip first to install
# !pip install CountryInfo

from countryinfo import CountryInfo

memproses = input("Masukkan nama negaramu: ")
negara = CountryInfo(memproses)

print("Informasi : ", negara.info())
print("Populasi : ", negara.population())