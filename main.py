class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cart:
    def __init__(self):
        self.items = {}
    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity):
        if product in self.items:
            self.items[product] -= quantity
        else:
            self.items[product] = quantity
    def calculate_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total
class Store:
    def __init__(self, name, price, floor=2):
        self.price = price
        self.name = name
        self.products = []
        self.floors = floor
        self.total_price = 0
    def add_products(self, product):
        self.products.append(product)
    def display_products(self):
        print(f"Available products at {self.name} store:")
        for product in self.products:
            print(f"{product.name} - ${product.price:.2f}")
    def display_store_info(self):
        print("{name} store information:".format(name=self.name))
        print("Number of floors: {floors}".format(floors=self.floors))
        print("Total price of all products: ${total_price}".format(total_price=self.total_price))
if __name__ == "__main__":
    apples = Product("Apple", 2.0)
    bananas = Product("Banana", 1.0)
    strawberries = Product("Strawberries", 4.0)
    avocados = Product("Avocados", 10.0)
    bell_peppers = Product("Bell Peppers", 6.0)
    carrots = Product("Carrots", 4.0)
    broccoli = Product("Broccoli", 5.0)
    garlic = Product("Garlic", 3.0)
    lemons = Product("Lemons", 2.0)
    onion = Product("Onions", 2.0)
    parsley = Product("Parsley", 1.0)
    cilantro = Product("Cilantro", 5.0)
    chicken = Product("Chicken", 18.0)
    eggs = Product("Eggs", 5.0)
    ground_beef = Product("Ground Beef", 17.0)
    sliced_turkey = Product("Sliced Turkey", 15.0)
    lunch_meat = Product("Lunch Meat", 20.0)
    laptop = Product("Laptop", 1000.0)
    phone = Product("Phone", 500.0)
    headphones = Product("Headphones", 100.0)

    groceries_store = Store("Tubermarket Supermarket", 1)
    electronic_store = Store("Tubermarket Electronics", 2)

    groceries_store.add_products(apples)
    groceries_store.add_products(bananas)
    groceries_store.add_products(strawberries)
    groceries_store.add_products(avocados)
    groceries_store.add_products(bell_peppers)
    groceries_store.add_products(carrots)
    groceries_store.add_products(broccoli)
    groceries_store.add_products(garlic)
    groceries_store.add_products(lemons)
    groceries_store.add_products(onion)
    groceries_store.add_products(parsley)
    groceries_store.add_products(cilantro)
    groceries_store.add_products(chicken)
    groceries_store.add_products(eggs)
    groceries_store.add_products(sliced_turkey)
    groceries_store.add_products(lunch_meat)

    electronic_store.add_products(laptop)
    electronic_store.add_products(phone)
    electronic_store.add_products(headphones)

    groceries_store.display_store_info()
    electronic_store.display_store_info()

    groceries_store.display_products()
    electronic_store.display_products()

    my_cart = Cart()

    while True:
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Remove Item From Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your Choice (1-5): ")

        if choice == '1':
            product_name = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))

            for store in [groceries_store, electronic_store]:
                for product in store.products:
                    if product.name.lower() == product_name.lower():
                        my_cart.add_item(product, quantity)
                        print(f"{quantity} {product.name}(s) added to the cart.")
                        break

        elif choice == '2':
            product_name = input("Enter the product name to remove: ")
            quantity = int(input("Enter the quantity to remove: "))

            for store in [groceries_store, electronic_store]:
                for product in store.products:
                    if product.name.lower() == product_name.lower():
                        my_cart.remove_item(product, quantity)
                        print(f"{quantity} {product.name}(s) removed from the cart.")

        elif choice == '3':
            print("\nItems in the cart:")
            for product, quantity in my_cart.items.items():
                print(f"{quantity} {product.name}")

        elif choice == '4':
            total_cost = my_cart.calculate_total()
            print(f"\nTotal cost: ${total_cost:.2f}")
            print("Thank you for shopping with us!")
            break

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
