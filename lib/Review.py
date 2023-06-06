class Customer:

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name


    def given_name(self):
        return self._given_name


    def family_name(self):
        return self._family_name


    def full_name(self):
        return f"{self._given_name} {self._family_name}"




class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating
    

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews


    def __str__(self):
        return f"Review by {self._customer.full_name()} for {self._restaurant.name()}: Rating {self._rating}"


class Restaurant:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


# Create customer and restaurant instances
customer = Customer("Bethwel", "Kipruto")
restaurant = Restaurant("PIZZA PIZZERIA")
# restaurant1 = Restaurant("Kibandaski")
# # Creating my customer instances
customer1 = Customer("Yesu", "Tongareni")

customer2 = Customer("Aluoch", "Okoth")



review = Review(customer, restaurant, 5)
# review1 = Review(customer1, restaurant1, 4)



review_customer = review.customer()

review_restaurant = review.restaurant()


print(review_customer.full_name())  
print(review_restaurant.name())  

print(review.rating()) 



print(review) 


all_reviews = Review.all()
