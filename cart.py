from collections import defaultdict
import time
import os

# Dictionary to store items and their prices
items = {
    "MOBILE": {"SAMSUNG": 15000, "REDMI": 12000, "APPLE": 100000},
    "LAPTOP": {"HP": 40000, "LENOVO": 35000, "MACBOOK": 250000},
    "COURSE": {"C": 1000, "C++": 3000, "JAVA": 4000, "PYTHON": 3500}
}

# Function to fill items into the data structure
def fill_items():
    items["MOBILE"]["SAMSUNG"] = 15000
    items["MOBILE"]["REDMI"] = 12000
    items["MOBILE"]["APPLE"] = 100000
    items["LAPTOP"]["HP"] = 40000
    items["LAPTOP"]["LENOVO"] = 35000
    items["LAPTOP"]["MACBOOK"] = 250000
    items["COURSE"]["C"] = 1000
    items["COURSE"]["C++"] = 3000
    items["COURSE"]["JAVA"] = 4000
    items["COURSE"]["PYTHON"] = 3500

# Class representing a customer
class Customer:
    def __init__(self):
        self.selected_items = defaultdict(lambda: defaultdict(int))
        self.name = input("Enter your name: ").upper()
        print(f"HI {self.name}\n\n")

    def add_to_cart(self, category, model):
        self.selected_items[category][model] += 1

    def remove_from_cart(self, category, model):
        if self.selected_items.get(category) and self.selected_items[category].get(model):
            del self.selected_items[category][model]
            print(f"{model} removed from the cart.")
        else:
            print("Item not found in the cart.")

    def increase_quantity(self, category, model, quantity):
        self.selected_items[category][model] += quantity
        print(f"Quantity of {model} increased by {quantity}.")

    def decrease_quantity(self, category, model, quantity):
        if self.selected_items.get(category) and self.selected_items[category].get(model):
            if self.selected_items[category][model] >= quantity:
                self.selected_items[category][model] -= quantity
                print(f"Quantity of {model} decreased by {quantity}.")
            else:
                print("Requested quantity is greater than available quantity in the cart.")
        else:
            print("Item not found in the cart.")
    def print_bill(self):
     total_amount = 0
     total_items = 0
     print("Category\tItem\tQuantity\tCost")

     for category, models in self.selected_items.items():
         for model, quantity in models.items():
             temp = quantity * items[category][model]
             total_amount += temp
             total_items += quantity
             print(f"{category}\t\t{model}\t{quantity}\t\t{temp}")

     print("-------------------------------")
     print(f"Total amount before discount:\t\t{total_amount}")

    # Applying discount strategies based on total_amount
     if total_items >= 4:
          # Strategy 1: Buy 4 or more Get 1 free for cheaper ones
          eligible_items = []
          for category, models in self.selected_items.items():
              for model, quantity in models.items():
                  item_cost = items[category][model]
                  for _ in range(quantity):
                      eligible_items.append((category, model, item_cost))

          eligible_items.sort(key=lambda x: x[2])  # Sort items by price
          discount_items = min(len(eligible_items) // 4, len(eligible_items))
          discount = sum(item[2] for item in eligible_items[:discount_items]) * 0.1
          total_amount -= discount
          print(f"Discount applied (Buy 4 or more Get 10% off on one item):\t{discount}")


    # Apply discount based on total_amount range
     if 1000 < total_amount <= 5000:
        # Strategy 2: If price above 1000 to 5000 discount of 20% up to 500
         discount = min(500, int(0.2 * total_amount))
         total_amount -= discount
         print(f"Discount applied (20% up to 500):\t\t{discount}")
     elif 5000 < total_amount <= 50000:
        # Strategy 3: If price above 5000 to 50000 discount of 20% up to 5000
         discount = min(5000, int(0.2 * total_amount))
         total_amount -= discount
         print(f"Discount applied (25% up to 5000):\t\t{discount}")
     elif 50000 < total_amount <= 200000:
        # Strategy 4: If price above 50000 to 200000 discount of 20% up to 15000
         discount = min(15000, int(0.2 * total_amount))
         total_amount -= discount
         print(f"Discount applied (20% up to 15000):\t\t{discount}")
     elif 200000 < total_amount <= 1000000:
        # Strategy 5: If greater than 200000 and less than 1000000 flat 10% upto 25000
         discount = min(25000, int(0.1 * total_amount))
         total_amount -= discount
         print(f"Discount applied (10%) upto 25000:\t\t{discount}")
     elif total_amount > 1000000:
         # Strategy 6: If greater than 1000000 flat 10% upto 35000
         discount = min(35000, int(0.2 * total_amount))
         total_amount -= discount
         print(f"Discount applied (20%) upto 35000:\t\t{discount}")

     print("-------------------------------")
     print(f"Total amount after discount:\t\t{total_amount}")
     print("-------------------------------")
     print("***** THANK YOU & HAPPY ONLINE SHOPPING *****")

    

   # Class representing the shop
class Shop:
    def show(self):
        pass

    def select(self, obj):
        pass

    def show_menu(self):
        print("Menu")
        print("-----------------------------------------")
        print("1. MOBILE")
        print("2. LAPTOP")
        print("3. Programming COURSEs")
        print("4. Checkout")
        print("5. Exit")
        print("-----------------------------------------")
# Subclass MOBILE inheriting from Shop
class MOBILE(Shop):
    def show(self):
        print("- - - - - - - - - - - -\nItem    Cost")
        cnt = 1
        for key, value in items["MOBILE"].items():
            print(f"{cnt}. {key} --- Rs.{value}/-")
            cnt += 1
        print("- - - - - - - - - - - -\n\n")

    def select(self, obj):
        print("These are the smartphone categories we have....")
        num = int(input("Enter your selection: "))
        qua = int(input("Enter the quantity: "))

        if num < 1 or num > 3 or qua <= 0:
            print("Wrong Input\n")
            return

        print(f"\n\nPURCHASE SUCCESSFUL!! {qua} {list(items['MOBILE'].keys())[num-1]}(s) ADDED TO THE CART\n\n")
        for _ in range(qua):
            obj.add_to_cart("MOBILE", list(items['MOBILE'].keys())[num-1])

# Subclass LAPTOP inheriting from Shop
class LAPTOP(Shop):
    def show(self):
        print("- - - - - - - - - - - -\nItem    Cost")
        cnt = 1
        for key, value in items["LAPTOP"].items():
            print(f"{cnt}. {key} --- Rs.{value}/-")
            cnt += 1
        print("- - - - - - - - - - - -\n")

    def select(self, obj):
        print("These are the LAPTOP categories we have....")
        num = int(input("Enter your selection: "))
        qua = int(input("Enter the quantity: "))

        if num < 1 or num > 3 or qua <= 0:
            print("Wrong Input\n")
            return

        print(f"\n\nPURCHASE SUCCESSFUL!! {qua} {list(items['LAPTOP'].keys())[num-1]}(s) ADDED TO THE CART\n\n")
        for _ in range(qua):
            obj.add_to_cart("LAPTOP", list(items['LAPTOP'].keys())[num-1])

# Subclass COURSEs inheriting from Shop
class COURSEs(Shop):
    def show(self):
        print("- - - - - - - - - - -\nItem    Cost")
        cnt = 1
        for key, value in items["COURSE"].items():
            print(f"{cnt}. {key} --- Rs.{value}/-")
            cnt += 1
        print("- - - - - - - - - - -\n")

    def select(self, obj):
        print("These are the COURSEs categories we have....")
        num = int(input("Enter your selection: "))
        qua = int(input("Enter the quantity: "))

        if num < 1 or num > 4 or qua <= 0:
            print("Wrong Input\n")
            return

        print(f"\n\nPURCHASE SUCCESSFUL!! {qua} {list(items['COURSE'].keys())[num-1]}(s) ADDED TO THE CART\n\n")
        for _ in range(qua):
            obj.add_to_cart("COURSE", list(items['COURSE'].keys())[num-1])

def main_menu():
    print("Press Y if you want to return to the main menu")
    print("Press N if you want to exit")
    ch2 = input().upper()
    if ch2 == 'Y':
        print("REDIRECTING TO THE MAIN MENU.....\n\n")
        time.sleep(1)
        
        
        
        
        # Clear screen
    elif ch2 == 'N':
        exit(0)
    else:
        print("Invalid Input")
       
def main():
    fill_items()
    
    print("WELCOME TO OUR SHOP. WE ARE DELIGHTED THAT YOU ARE HERE. HOW CAN WE HELP YOU? WE DEAL IN ELECTRONIC GADGETS AND COURSES.")
    c = Customer()
    s = Shop()
    
    while True:
        s.show_menu()
        val = int(input("Please select an option to proceed further: "))

        if val == 1:
            mb = MOBILE()
            s = mb
            s.show()
            s.select(c)
            main_menu()
        elif val == 2:
            lp = LAPTOP()
            s = lp
            s.show()
            s.select(c)
            main_menu()
        elif val == 3:
            cs = COURSEs()
            s = cs
            s.show()
            s.select(c)
            main_menu()
        elif val == 4:
            c.print_bill()

            ch3 = input("\nDo you want to modify items in the cart (Y/N): ")
            if ch3.lower() == 'y':
                print("1. To increase the quantity")
                print("2. To decrease the quantity")
                ch4 = input("Enter your choice: ")
                if ch4 == '1':
                    category = input("Enter the category of the item to modify (e.g., MOBILE, LAPTOP, COURSEs): ").upper()
                    item = input("Enter the name of the item: ")
                    quantity = int(input("Enter the quantity to increase: "))
                    c.increase_quantity(category, item, quantity)
                elif ch4 == '2':
                    category = input("Enter the category of the item to modify (e.g., MOBILE, LAPTOP, COURSEs): ").upper()
                    item = input("Enter the name of the item: ")
                    quantity = int(input("Enter the quantity to decrease: "))
                    c.decrease_quantity(category, item, quantity)
                else:
                    print("Invalid choice")
                    main_menu()
        elif val == 5:
            exit(0)
        else:
            print("Wrong Input. If you want to checkout, you can press 4\n")

if __name__ == "__main__":
    main()
