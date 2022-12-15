import requests, os, time
from Splash import SplashHias

class ongkirKu:
  def _init_(self):
    self.fromID = 0
    self.toID = 0
    self.weight = 0
    self.city = 0

  def getFromID(self):
    return self._fromID
      
  def setFromID(self, x):
    self._fromID = x

  def getToID(self):
    return self._toID
      
  def setToID(self, x):
    self._toID = x

  def getWeight(self):
    return self._weight
      
  def setWeight(self, x):
    self._weight = x

  def getCity(self):
    return self._city
      
  def setCity(self, x):
    self._city = x

  def search():
    print()

  def viewList():
    print()

  def cekOngkir(self):
    json = {
      'origin': self._fromID,
      'destination': self._toID,
      'weight': self._weight,
      'courier':'jne',
      'key': "c3aad4b87ecadd970bb9b08279e40ee3",
      'content-type': "application/x-www-form-urlencoded"
    }

    url = "https://api.rajaongkir.com/starter/cost"

    cost = requests.post(url, json=json)

    dataCost = cost.json()
    get = dataCost['rajaongkir']['results'][0]['costs'][0]['cost'][0]['value']
    print(f"\nOrigin\t\t: {dataCost['rajaongkir']['origin_details']['city_name']}")
    print(f"Destination\t: {dataCost['rajaongkir']['destination_details']['city_name']}")
    print(f"Courier\t\t: JNE")
    print(f"Weight\t\t: {self._weight}")
    print(f"Price\t\t: {get}")

def main():
  
  p = ongkirKu()
  SplashHias.splashName()
  print()
  print('1. View List of City')
  print('2. Search City')
  print('3. Postage Check')
  print('4. Exit')

  try:  
    menu = input('Choose menu: ')

    if menu == '1':
      p.viewList()

      back = input('Back to the main menu?(y/n)')
      if back == 'y' or back == 'Y':
        main()

    elif menu == '2':
      city = input('Input City (Case Sensitive!): ')

      p.setCity(city)
      p.search()

      back = input('Back to the main menu?(y/n)')
      if back == 'y' or back == 'Y':
        main()

    elif menu == '3':
      fromID = int(input('Input From City-ID\t\t: '))
      toID = int(input('Input Destionation City-ID\t: '))
      weight = int(input('Input Weight\t\t\t: '))

      p.setFromID(fromID)
      p.setToID(toID)
      p.setWeight(weight)
      p.cekOngkir()

      back = input('Back to the main menu?(y/n)')
      if back == 'y' or back == 'Y':
        main()

  except:
    print('Wrong input!')
    print('PLease input correctly')


prov = requests.get("https://api.rajaongkir.com/starter/province?key=c3aad4b87ecadd970bb9b08279e40ee3")
city = requests.get("https://api.rajaongkir.com/starter/city?key=c3aad4b87ecadd970bb9b08279e40ee3")
dataProv = prov.json()
dataCity = city.json()

# login()