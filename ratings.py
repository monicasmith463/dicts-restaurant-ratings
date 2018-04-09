"""Restaurant rating lister."""


def get_file_ratings(filename):
    """Adds restaurant and rating from user to ratings from file."""

    file_ratings = {}

    with open(filename) as scores:
        for line in scores:
            restaurant, rating = line.strip().split(":")
            file_ratings[restaurant] = rating

    return file_ratings


def get_user_ratings(file_ratings):
    """Adds user restaurant and rating"""

    user_restaurant = raw_input("Please enter a restaurant: ")
    user_rating = raw_input("Please enter the rating: ")

    file_ratings[user_restaurant] = user_rating


def sort_ratings(restaurants):
    """Sorts restaurant ratings by restaurant name."""

    sorted_restaurants = sorted(restaurants.items())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant[0], restaurant[1])


def show_ratings(filename):
    """Get file ratings, get usr rating, sort all ratings and print"""

    ratings = get_file_ratings(filename)

    get_user_ratings(ratings)

    sort_ratings(ratings)

show_ratings("scores.txt")
