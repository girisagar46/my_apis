from datetime import datetime

import requests

LIMIT = 10
TODAY = datetime.now()

API_URL = (
        "https://www.forbes.com/forbesapi/person/rtb/0/position/true.json"
        "?fields=personName,gender,source,countryOfCitizenship,birthDate,finalWorth"
        "&limit=" + str(LIMIT)
)


def calculate_age(unix_date: int) -> str:
    """Calculates age from given unix time format
    Returns: Age as string
    >>> calculate_age(-657244800000)
    '73'
    """
    birthdate = datetime.fromtimestamp(unix_date / 1000).date()
    return str(
        TODAY.year - birthdate.year - ((TODAY.month, TODAY.day) < (birthdate.month,
                                                                   birthdate.day))
    )


def get_top_billionares() -> list:
    """Get top 10 real time billionares"""
    response_json = requests.get(API_URL).json()
    return [
        {
            "Name": person["personName"],
            "Source": person["source"],
            "Country": person["countryOfCitizenship"],
            "Gender": person["gender"],
            "Worth ($)": f"{person['finalWorth'] / 1000:.1f} Billion",
            "Age": calculate_age(person["birthDate"]),
        }
        for person in response_json["personList"]["personsLists"]
    ]
