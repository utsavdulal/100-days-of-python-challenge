# nesting
capitals = {"France": "paris", "Nepal": "Kathmandu", "India": "Delhi"}

# nesting a list in a dictionary
travel_log = {
    "Nepal": ["Kathmandu", "Pokhara", "Chitwan", "Sauraha", "Itahari"],
    "India": ["Delhi", "Mumbai", "Kolkata", "Banglore", "Goa"],
}
# print(travel_log)

# nesting dictionary in dictionary
travel_log = {
    "Nepal": {
        "cities_visited": ["Kathmandu", "Pokhara", "Chitwan", "Sauraha", "Itahari"],
        "total_visits": 1000,
    },
    "India": {
        "cities_visited": ["Delhi", "Mumbai", "Kolkata", "Banglore", "Goa"],
        "total_visits": 243,
    },
}
# print(travel_log)

# nesting dictionary inside a list
travel_log = [
    {
        "country_visited": "Nepal",
        "cities_visited": ["Kathmandu", "Pokhara", "Chitwan", "Sauraha", "Itahari"],
        "total_visits": 1000,
    },
    {
        "country_visited": "India",
        "cities_visited": ["Delhi", "Mumbai", "Kolkata", "Banglore", "Goa"],
        "total_visits": 243,
    },
]
print(travel_log)
