def uq():
    uq = input("\nWould you like status updates? (Y/N) ")
    if uq.lower() == "y": uq = True
    else: uq = False
    return uq