from database import Product
try:
    p_name = input("Enter product name\n")
    p_qtty = input("Enter quantity\n")
    p_price = input("Enter price\n")
    Product.create(name=p_name, qtty=p_qtty, price=p_price)
    print("Product saved successfully")

except:
    print("An error occured.Please try again")