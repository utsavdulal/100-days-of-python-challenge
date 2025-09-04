travel_log = [
    {
        "country_visited": "Nepal",
        "total_visits": 1000,
        "cities_visited": ["Kathmandu", "Pokhara", "Chitwan", "Sauraha", "Itahari"],
    },
    {
        "country_visited": "India",
        "total_visits": 24,
        "cities_visited": ["Delhi", "Mumbai", "Kolkata", "Banglore", "Goa"],
    },
]


def add_new_country(country, visits, cities):
    new_country = {
        "country_visited": country,
        "total_visits": visits,
        "cities_visited": cities,
    }
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
