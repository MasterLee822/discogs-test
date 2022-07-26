import sys
from typing import Tuple
from constants import available_currencies, base_currency_api_url
import requests
from requests.structures import CaseInsensitiveDict
import logging
log = logging.getLogger(__name__)

def valid_currency(currency: str) -> bool:
    if currency in available_currencies:
        return True
    else:
        return False


def validate_currencies(rate_1, rate_2) -> Tuple[bool, str]:
    if not valid_currency(rate_1):
        message = f"Rate 1 is an invalid rate. Valid rates are: {available_currencies}"
        return False, message

    if not valid_currency(rate_2):
        message = f"Rate 2 is an invalid rate. Valid rates are: {available_currencies}"
        return False, message

    return True, "Success"


def get_conversion_rate(currency_1: str, currency_2) -> float:
    log.info(f"get_conversion {currency_1}, {currency_2}")

    conversion_rate_url = f"{base_currency_api_url}&base_currency={currency_1}&currencies={currency_2}"
    response = requests.get(conversion_rate_url)

    if response.status_code != 200:
        log.error(f"get_conversion_rate returned a non-200 error. {response.json()}")
        raise ValueError

    jason_info = response.json()
    rate = jason_info['data'][currency_2]['value']
    return rate


def return_fail_json(message: str, inputs: list) -> dict:
    return_dict = {"inputs": inputs, "success": False, "status": message}
    return return_dict


def valid_api_key() -> bool:
    print(f"Check for valid API key", file=sys.stderr)

    resp = requests.get(base_currency_api_url)
    print(resp.status_code, file=sys.stderr)
    if resp.status_code == 200:
        return True
    else:
        log.critical("Currency API Key is invalid.  Check your api key.")
        return False
