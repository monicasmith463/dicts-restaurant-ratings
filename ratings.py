"""Restaurant rating lister."""


# put your code here
def sort_ratings(restaurants):
    """Sorts restaurant ratings by restaurant name."""

    sorted_restaurants = sorted(restaurants.keys())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant, restaurants[restaurant])


def get_ratings(filename):
    """Adds restaurant and rating from user to ratings from file."""

    ratings = {}

    user_restaurant = raw_input("Please enter a restaurant: ")
    user_rating = raw_input("Please enter the rating: ")

    with open(filename) as scores:
        for line in scores:
            restaurant, rating = line.strip().split(":")
            ratings[restaurant] = rating

    ratings[user_restaurant] = user_rating

    sort_ratings(ratings)

get_ratings("scores.txt")
