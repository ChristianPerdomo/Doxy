#!/usr/bin/python3

# Definición de colores para salida en la consola
class Color:
    CYAN = "\033[1;36m"
    GREEN = "\033[1;32m"
    RESET = "\033[00m"

# Función para imprimir los resultados de búsqueda
def print_search_results(user_id, category, types):
    print(f"{Color.CYAN}\n___{category}___{Color.RESET}")
    for type_name, url_part in types.items():
        print(f"{Color.GREEN}{type_name}:{Color.RESET} https://www.facebook.com/search/{user_id}/{url_part}")

# Validación del ID de usuario de Facebook
def is_valid_user_id(user_id):
    # Puedes expandir esta función con expresiones regulares o criterios específicos
    return len(user_id) > 0

def main():
    user_id = input("Please enter the Facebook profile ID to search: ")

    if not is_valid_user_id(user_id):
        print("Please provide a valid Facebook user ID.")
        return

    # Diccionarios con tipos de búsquedas disponibles
    profile_types = {
        "Pictures": "photos-by",
        "Videos": "videos-by",
        "Posts": "stories-by",
        "Groups": "groups",
        "Future events": "events-joined/",
        "Past events": "events-joined/in-past/date/events/intersect/",
        "Games": "apps-used/game/apps/intersect",
        "Apps": "apps-used/",
    }

    tags_types = {
        "Pictures": "photos-of/intersect",
        "Video": "videos-of/intersect",
        "Posts": "stories-tagged/intersect",
    }


    comments_types = {
        "Pictures": "photos-commented/intersect",
    }

    liked_types = {
        "Pictures": "photos-liked/intersect",
        "Videos": "videos-liked/intersect",
        "Posts": "stories-liked/intersect",
    }

    places_types = {
        "All": "places-visited/",
        "Bars": "places-visited/110290705711626/places/intersect/",
        "Restaurants": "places-visited/273819889375819/places/intersect/",
        "Stores": "places-visited/200600219953504/places/intersect/",
        "Outdoors": "places-visited/935165616516865/places/intersect/",
        "Hotels": "places-visited/164243073639257/places/intersect/",
        "Theaters": "places-visited/192511100766680/places/intersect/",
    }

    people_types = {
        "Family": "relatives/intersect",
        "Friends": "friends/intersect",
        "Friends of friends": "friends/friends/intersect",
        "Co-workers": "employees/intersect/",
        "Classmates": "schools-attended/ever-past/intersect/students/intersect/",
        "Locals": "current-cities/residents-near/present/intersect",
    }

    interests_types = {
        "Pages": "pages-liked/intersect",
        "Political parties": "pages-liked/161431733929266/pages/intersect/",
        "Religion": "pages-liked/religion/pages/intersect/",
        "Music": "pages-liked/musician/pages/intersect/",
        "Movies": "pages-liked/movie/pages/intersect/",
        "Books": "pages-liked/book/pages/intersect/",
        "Places": "places-liked/",
    }

    # Impresión de resultados para cada categoría
    print_search_results(user_id, "Profile", profile_types)
    print_search_results(user_id, "Tags", tags_types)
    print_search_results(user_id, "Comments", comments_types)
    print_search_results(user_id, "Liked", liked_types)
    print_search_results(user_id, "Places", places_types)
    print_search_results(user_id, "People", people_types)
    print_search_results(user_id, "Interests", interests_types)

if __name__ == "__main__":
    main()
