# mp media platforms
def mp():
    platforms_options = {
        "1": "LinkedIn",
        "2": "Instagram"
    }

    platforms = input(
        """\nWhat platform are you posting? \n1.LinkedIn  -  2.Instagram:  """)

    platforms = platforms_options.get(platforms, "Unknown")

    return platforms