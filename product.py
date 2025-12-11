def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result

if __name__ == "__main__":
  product_id= "P101"
  name= "laptop"
  quantity= "1"
  price= "200000"
print(product_details(product_id, name, quantity, price))
