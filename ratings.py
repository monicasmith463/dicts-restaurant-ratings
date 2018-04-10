"""Restaurant rating lister."""

import random


def get_file_ratings(filename):
    """Adds restaurant and rating from user to ratings from file."""

    file_ratings = {}

    with open(filename) as scores:
        for line in scores:
            restaurant, rating = line.strip().split(":")
            file_ratings[restaurant] = rating

    return file_ratings


def get_user_choice():
    user_prompt = """
    Choose from the following:
    1 to see all ratings
    2 to add a new restaurant
    3 to update a rating
    'q' to quit"""

    print user_prompt
    user_choice = raw_input("> ")

    return user_choice


def execute_choice(choice, ratings):
    """Executes user choice"""

    if choice == "q":
        exit()
    elif choice == "1":
        sort_ratings(ratings)
    elif choice == "2":
        get_user_ratings(ratings)
        sort_ratings(ratings)
    elif choice == "3":
        update_rating(ratings)
        sort_ratings(ratings)
    else:
        print "Invalid input."
        choice = get_user_choice()


def update_rating(ratings):
    random_choice = random.choice(ratings.keys())
    print "{} is rated at {}.".format(random_choice, ratings[random_choice])
    get_user_ratings(ratings, random_choice)


def get_user_ratings(file_ratings, random_choice=None):
    """Adds user restaurant and rating"""

    user_restaurant = random_choice

    while True:
        try:
            if not random_choice:
                user_restaurant = raw_input("Please enter a restaurant: ")
            user_rating = int(raw_input("Please enter the rating: "))

        except ValueError:
            print "Rating must be a number between 1 and 5. Please try again."
            continue

        if user_rating < 1 or user_rating > 5:
            print "Rating must be a number between 1 and 5. Please try again."

        else:
            break

    file_ratings[user_restaurant] = user_rating


def sort_ratings(restaurants):
    """Sorts restaurant ratings by restaurant name."""

    sorted_restaurants = sorted(restaurants.items())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant[0], restaurant[1])


def show_ratings(filename):
    """Get file ratings, get usr rating, sort all ratings and print"""

    ratings = get_file_ratings(filename)

    while True:

        user_choice = get_user_choice()

        execute_choice(user_choice, ratings)


show_ratings("scores.txt")
