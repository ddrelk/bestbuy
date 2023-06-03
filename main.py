import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(store_object):
    while True:
        try:

            print("""
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
            """)
            user_input = int(input("Please choose a number: "))
            if user_input == 4:
                print("Quitting program!!")
                break
            if user_input == 1:
                print("-----")
                store_object.list_product()
                print("-----")
            if user_input == 2:
                total_quantity = store_object.get_total_quantity()
                print(f"Total of {total_quantity} items in store")
            if user_input == 3:
                while True:
                    all_product = store_object.get_all_products()
                    print("-----")
                    store_object.list_product()
                    print("-----")
                    print("When you want to finish order, enter empty text.")
                    item_input = input("Which product # do you want? ")
                    amount_input = input("What amount do you want? ")
                    if not item_input or not amount_input:
                        print("********")
                        total_price = store_object.order(order_list)
                        print(f"Order made! Total payment: ${total_price}")
                        break
                    try:
                        item_index = int(item_input)
                        amount = int(amount_input)
                        if item_index < 1 or item_index > len(all_product):
                            print("Invalid product number! Please try again.")
                            continue
                        product = all_product[item_index - 1]
                        order_list = [(product, amount)]
                        print("Product added to list!")
                    except ValueError:
                        print("Invalid input! Please enter a valid number.")
        except ValueError:
            print("Error with your choice! Try again!")


if __name__ == "__main__":
    start(best_buy)
