from random import choice
def get_description():
    """Return random weather, just like the pros"""
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
