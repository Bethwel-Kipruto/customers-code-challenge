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
        self._reviews = []

    def name(self):
        return self._name

    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews

    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer().full_name())
        return list(unique_customers)

    def average_star_rating(self):
        total_ratings = 0
        for review in self._reviews:
            total_ratings += review.rating()
        if len(self._reviews) > 0:
            return total_ratings / len(self._reviews)
        else:
            return 0.0



customer1 = Customer("Mzee", "Bikes")
customer2 = Customer("Mtu", "Kutu")
customer3 = Customer("Heri", "Wewe")

restaurant = Restaurant("KFC")
# restaurant1 = Restaurant("Kibandaski")


review1 = Review(customer1, restaurant, 5)
review2 = Review(customer2, restaurant, 3)
# review3 = Review(customer3, restaurant)

restaurant.add_review(review1)
restaurant.add_review(review2)
# restaurant.add_review(review3)

all_reviews = restaurant.reviews()
for review in all_reviews:
    print(review)


unique_customers = restaurant.customers()
print(unique_customers)



average_rating = restaurant.average_star_rating()
print (f"THE AVARAGE RATING IS {average_rating}")