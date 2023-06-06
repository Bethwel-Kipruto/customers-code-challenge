#!/usr/bin/env python3
import ipdb;
from Customer import Customer
from Restaurant import Restaurant
from Review import Review


if __name__ == '__main__':
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Jane", "Smith")
    customer3 = Customer("Bob", "Johnson")

    restaurant1 = Restaurant("Pizza Place")
    restaurant2 = Restaurant("Burger Joint")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)
    review4 = Review(customer3, restaurant1, 2)
    review5 = Review(customer3, restaurant2, 4)

    # Accessing attributes and relationships
    print(restaurant1.name())  # Output: "Pizza Place"
    print(review2.rating())  # Output: 5
    print(review3.rating())  # Output: 3
    print(review4.rating())  # Output:2
    print(review5.rating())  # Output: 4


    print(customer1.full_name())  # Output: "John Doe"
    print(customer2.full_name())  # Output: "Jane Smith"
    print(customer3.full_name())  # Output: "Bob Johnson"


    print(restaurant1.reviews())  # Output: [review1, review2]

    print(restaurant2.get_customers())  
    print(customer1.get_all_customers())
#  WRITE YOUR TEST CODE HERE ###









# DO NOT REMOVE THIS
    ipdb.set_trace()
