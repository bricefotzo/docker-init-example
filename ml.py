"""
Machine Leanring module.
"""

def predict_rent(city: str, rooms: int, area: float) -> float:
    """
    Calculate the rent for a given city, number of rooms and area.

    Args:
        city (str): The city where the property is located.
        rooms (int): The number of rooms in the property.
        area (float): The area of the property.

    Returns:
        float: The rent for the property.
    
    Example:
        >>> predict_rent("paris", 2, 30)
        1000
    """

    data = {
        "paris": {
            1: {20: 800, 30: 900, 40: 1200},
            2: {20: 850, 30: 1000, 40: 1200},
            3: {20: 2000, 30: 2200, 40: 2400},
        },
        "lyon": {
            1: {20: 800, 30: 1000, 40: 1200},
            2: {20: 1300, 30: 1500, 40: 1700},
            3: {20: 1800, 30: 2000, 40: 2200},
        },
        "rouen": {
            1: {20: 350, 30: 800, 40: 1000},
            2: {20: 1100, 30: 1300, 40: 1500},
            3: {20: 1600, 30: 1800, 40: 2000},
        },
    }
    # return the value from the dictionary
    return data[city][rooms][area]