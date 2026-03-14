products = {"phone": 5, "laptop": 2}
coupon = "SAVE10"
payments = ["card", "upi", "cod"]

try:
    item = input("Enter product: ")
    qty = int(input("Enter quantity: "))
    code = input("Enter coupon: ")
    pay = input("Enter payment method: ")

    if products[item] < qty:
        raise Exception("Out of stock")

    if code != "" and code != coupon:
        raise Exception("Invalid coupon code")

    if pay not in payments:
        raise Exception("Invalid payment method")

    products[item] -= qty
    print("Order placed successfully")

except KeyError:
    print("Product not found")

except ValueError:
    print("Invalid quantity")

except Exception as e:
    print("Error:", e)


try:
    ret = input("Return order? (yes/no): ")
    if ret == "yes":
        products[item] += qty
        print("Order returned")
        print("Refund processed")
except:
    print("Return error")