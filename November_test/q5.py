class Product:
    products=[]
    product_set=set()
    def __init__(self,product_id,product_name,category,price):
        Product.product_set.add(product_id)
        Product.products.append(self)
        if len(Product.product_set) == len(Product.products):
            self.__product_id=product_id
            self.__product_name=product_name
            self.__category=category
            self.__price=price
        else:
            print("The id must be unique..")


    def get_price(self):
        return self.__price

    def display_product(self):
        print("The product have folowing details:") 
        print(F"Name of product:{self.__product_name}")
        print(F"ID of product:{self.__product_id}")
        print(F"Category of product:{self.__category}")
        print(F"Price of product:{self.__price}\n")

    @classmethod
    def second_highest_price(cls):
        max=0
        max2=0
        for i in range(len(cls.products)):
            if cls.products[i].get_price()>max:
                max2=max
                max=cls.products[i].__price
            elif cls.products[i].__price>max2:
                max2=cls.products[i].__price

        return max2

    @classmethod
    def average_price(cls):
        average=0
        for i in range(len(cls.products)):
            average+= cls.products[i].get_price()
        return average/len(cls.products)

    @classmethod
    def product_greater_than_10000(cls):
        print("The product price greater than 10000 are:")
        for product in cls.products:
            if product.__price>10000:
                product.display_product()

p1=Product(101,"tablet","electronics",35000)
p2=Product(201,"Flour","Grocery",500)
p3=Product(102,"Headphones","electronic",1500)
p4=Product(301,"Blazer","clothing",3000)
p5=Product(103,"Mobile","electronics",20000)

p1.display_product()
p2.display_product()
p3.display_product()
p4.display_product()
p5.display_product()

Product.product_greater_than_10000()
print(f"The second highest price is {Product.second_highest_price()}") 
print(f"The average price is {Product.average_price()}\n")

print("A new product added with same id:") 
p6=Product(101,"mouse","electronic",2000)