"""Restaurant rating lister."""


def get_file_ratings(filename):
    """Adds restaurant and rating from user to ratings from file."""

    file_ratings = {}

    with open(filename) as scores:
        for line in scores:
            restaurant, rating = line.strip().split(":")
            file_ratings[restaurant] = rating

    return file_ratings


def get_user_choice():
    print "Enter 1 to see all ratings\n 2 to add a new restaurant\n 'q' to quit"
    user_choice = raw_input("> ")

    return user_choice


def execute_choice(choice, ratings):
    """Executes user choice"""
    if choice == "q":
        return
    elif choice == "2":
        get_user_ratings(ratings)

    sort_ratings(ratings)


def get_user_ratings(file_ratings):
    """Adds user restaurant and rating"""

    class Error(Exception):
        """Base class for other exceptions"""
        pass

    class notInRange(Error):
        """Raised when user_rating is smaller than 1 or bigger than 5"""
        pass

    try:
        user_restaurant = raw_input("Please enter a restaurant: ")
        user_rating = int(raw_input("Please enter the rating: "))

        if user_rating < 1 or user_rating > 5:
            raise notInRange
        file_ratings[user_restaurant] = user_rating
    except notInRange:
        print "Rating must be a number between 1 and 5. Please try again."
        get_user_ratings(file_ratings)
    except:
        print "Rating must be a number between 1 and 5. Please try again."
        get_user_ratings(file_ratings)


def sort_ratings(restaurants):
    """Sorts restaurant ratings by restaurant name."""

    sorted_restaurants = sorted(restaurants.items())

    for restaurant in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant[0], restaurant[1])


def show_ratings(filename):
    """Get file ratings, get usr rating, sort all ratings and print"""

    ratings = get_file_ratings(filename)

    user_choice = get_user_choice()

    execute_choice(user_choice, ratings)


show_ratings("scores.txt")
