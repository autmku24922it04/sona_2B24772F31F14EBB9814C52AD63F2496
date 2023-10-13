def linear_search_products(product_list, target_product):
  indices = []

  for i in range(len(product_list)):
      if product_list[i] == target_product:
          indices.append(i)

  return indices


products = ["Apple", "Banana", "Orange", "Banana", "Apple", "Mango", "Apple"]
target_product = "Apple"

result = linear_search_products(products, target_product)

if result:
  print(f"{target_product} found at indices: {result}")
else:
  print(f"{target_product} not found in the list.")
