product_name = input()

type_product = ""
if product_name in ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']:
    type_product = 'fruit'
elif product_name in ['tomato', 'cucumber', 'pepper', 'carrot']:
    type_product = 'vegetable'
else:
    type_product = 'unknown'

print(type_product)