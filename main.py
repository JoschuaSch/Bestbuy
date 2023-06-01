from product import NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree, TwentyPercentOff, ThirtyPercentOff

from store import Store


def start(store):
    """The main function that drives the store interface.

        Parameters:
        store (Store): a Store object which contains all the products

        """
    # The text shown in the Menu as headliner.
    menu_text = "Store Menu"
    while True:
        print(f"\n{menu_text:.^30}")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        option = input("Please choose an option (1-4): ")

        # Printing all products in the store
        if option == '1':
            print("\n\n----------------------------------------------------------")
            products = store.get_all_products()
            for i, product in enumerate(products, start=1):
                print(product.show(i))
            print("----------------------------------------------------------\n")

        # Printing the total quantity of all products in the store
        elif option == '2':
            print("\n\n----------------------------------------------------------")
            print("Total quantity in store:", store.get_total_quantity())
            print("----------------------------------------------------------\n")

        elif option == '3':
            # Creates a list to hold the order details
            order_list = []
            while True:
                print("\n\n**********************************************************")
                products = store.get_all_products()
                for i, product in enumerate(products, start=1):
                    print(product.show(i))
                print("**********************************************************\n")
                product_number = input("Choose the product number. Press Enter when you are finished, "
                                       "or want to return back: ")
                if product_number == '':
                    break
                try:
                    product_number = int(product_number) - 1
                except ValueError:
                    print("\n! Invalid product. Please enter a valid number. !")
                    continue
                try:
                    # Asks for the quantity, prompts error for invalid quantity
                    quantity = int(input("Enter the quantity: "))
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
                    continue
                # Shows an Error if requested quantity is greater than the available quantity
                if quantity > products[product_number].quantity:
                    print("\n\n----------------------------------------------------------")
                    print(f"Not enough {products[product_number].name} in stock.")
                    print("----------------------------------------------------------\n")
                else:
                    # If available, add product to the list
                    order_list.append((products[product_number], quantity))
                    print("\n\n----------------------------------------------------------")
                    print(f"{products[product_number].name} with the quantity of {quantity} added to the list.")
                    print("----------------------------------------------------------\n")
            if order_list:
                # Try to make the order with the products in the order list
                try:
                    total_price = store.order(order_list)
                    print("\n\n----------------------------------------------------------")
                    print(f"Order made! Total cost: {total_price}")
                    print("----------------------------------------------------------\n")
                except Exception as e:
                    print(str(e))

        elif option == '4':
            print("Thanks for shopping! Hope to see you next time!")
            break
        else:
            print("\nInvalid option, please choose again.")


def setup_store():
    """Sets up the products and promotions for the store."""
    product_list = [
        LimitedProduct('MacBook Air M2', 1450, 100, 10, promotions=[TwentyPercentOff(), ThirtyPercentOff()]),
        LimitedProduct("Bose QuietComfort Earbuds", 250, 500, 10, promotions=[ThirdOneFree()]),
        LimitedProduct("Google Pixel 7", 500, 250, 5, promotions=[SecondHalfPrice()]),
        NonStockedProduct("Windows License", 125, float('inf'), promotions=[PercentDiscount("30% off!", 30)]),
        NonStockedProduct("Shipping", 10, 0)
    ]
    return Store(product_list)


if __name__ == '__main__':
    store = setup_store()
    start(store)
