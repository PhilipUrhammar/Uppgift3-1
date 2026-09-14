import csv
import subprocess
import locale


def format_currency(value):
   return locale.currency(value,grouping=True)



def list_products(products):
   for idx, product in enumerate(products): # or (products, 1)
      
      name = product['name']
      price = format_currency(product['price'])
      quantity = product['quantity']

      print(f"{idx+1}) {name} \t {price} \t {quantity:<5}")



def view_product(idx, products):
   subprocess.run('cls', shell=True),

   product = products[idx]

   print("Product Details:")
   print(f"Name: {product['name']}")
   print(f"Description: {product['desc']}")
   print(f"Price: {format_currency(product['price'])}")
   print(f"Quantity: {product['quantity']}")



def remove_product(idx, products):
   if idx >= 1 and idx <= len(products) + 1:
      products.pop(idx-1)
      return "Produkten har tagits bort."
   
   else:
      return "Produkten finns inte."


def load_data(filename): 
   products = []           #lista
   
   with open(filename, 'r') as file: #öppnar en fil med read-rättighet
      reader = csv.DictReader(file)
      for row in reader:
         id = int(row['id'])
         name = row['name']
         desc = row['desc']
         price = float(row['price'])
         quantity = int(row['quantity'])
         
         products.append(
               {                   
                  "id": id,       
                  "name": name,
                  "desc": desc,
                  "price": price,
                  "quantity": quantity
               }
         )
         
   return products



#TODO: gör så man kan se en numrerad lista som börjar på 1. KLAR
#TODO: skriv klart funktionen som returnerar en specifik produkt med hjälp av id & products
#TODO: skriv en funkion som skapar en ny produkt - den behöver inte spara till fil!
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

   # found_max = max(products, key=lambda id: id['id'])
   # max_id = found_max['id']
   # new_id = max_id + 1
   
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

subprocess.run('cls',shell=True)

products = load_data('db_products.csv')


while True:
   list_products(products)
   
   print("-" * 140)
   option = input("Vad vill du göra? [# = visa produkt | L = lägg till | T = ta bort | E = ändra | Q = avsluta] ")
   
   
   if option.isdigit(): #if it is number digits
      idx = int(option) # 4: gör om inmatade option siffror till heltal och idx är en variabel som är datatyp heltal, int

      if idx >= 1 and idx <= len(products) + 1: # om idx är större än 1 och mindre än eller lika med längden på products + 1
         view_product(idx-1, products) # idx-1 för att få rätt index i listan (0-baserad)
         input() #bara vänta till tangentbordsklick
      
      if 0 < idx <= len(products):   
         view_product(idx, products)
         input() #bara vänta till tangentbordsklick

   else:
      if option.upper() == 'Q':
         exit(0)

      elif option.upper() == 'L':
         name = input("Ange produktens namn: ")
         desc = input("Ange produktens beskrivning: ")
         price = float(input("Ange produktens pris: "))
         quantity = int(input("Ange produktens kvantitet: "))

         new_product = {
            "id": len(products) + 1,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
         }

         products.append(new_product)
         print(f"Produkten '{name}' har lagts till.")

      elif option.upper() == 'T':

         which = int(input("Vilken produkt vill du ta bort? (Ange produktens nummer): "))

         print(remove_product(which, products))

      elif option.upper() == 'E':
         which = int(input("Vilken produkt vill du ändra? (Ange produktens nummer): "))

         if 0 < which <= len(products):
            product = products[which - 1]

            print(f"Nuvarande namn: {product['name']}")
            new_name = input("Ange nytt namn (eller tryck Enter för att behålla): ")
            if new_name:
               product['name'] = new_name

            print(f"Nuvarande beskrivning: {product['desc']}")
            new_desc = input("Ange ny beskrivning (eller tryck Enter för att behålla): ")
            if new_desc:
               product['desc'] = new_desc

            print(f"Nuvarande pris: {format_currency(product['price'])}")
            new_price_input = input("Ange nytt pris (eller tryck Enter för att behålla): ")
            if new_price_input:
               product['price'] = float(new_price_input)

            print(f"Nuvarande kvantitet: {product['quantity']}")
            new_quantity_input = input("Ange ny kvantitet (eller tryck Enter för att behålla): ")
            if new_quantity_input:
               product['quantity'] = int(new_quantity_input)

            print(f"Produkten '{product['name']}' har uppdaterats.")
         else:
            print("Produkten finns inte.")