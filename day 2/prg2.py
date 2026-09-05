# Shopping Cart CRUD Program

cart = []

print("   Welcome to Fruit Shopping")

while True:
    print("\n1. Add Fruit")
    print("2. View Cart")
    print("3. Update Fruit")
    print("4. Delete Fruit")
    print("5. Checkout")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter fruit name: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == "2":
        print("\nShopping Cart")
        print("cart type:", type(cart))
        print("Total items:", len(cart))
        print("Cart:", cart)

    elif choice == "3":
        old_item = input("Enter fruit to update: ")

        if old_item in cart:
            new_item = input("Enter new fruit name: ")
            index = cart.index(old_item)
            cart[index] = new_item
            print("Item updated successfully.")
        else:
            print("Item not found.")

    elif choice == "4":
        item = input("Enter fruit to delete: ")

        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")

print("\n===== Shopping Cart =====")
print("cart type:", type(cart))
print("Total items:", len(cart))
print("Cart:", cart)

cart = tuple(cart)

print("\nAfter converting to tuple")
print("cart type:", type(cart))
print("Cart:", cart)

print("\nCheckout Successful!")
print("Thank you for shopping.")