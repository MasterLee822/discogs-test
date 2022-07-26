from flask import Flask, jsonify, Response
from rate_functions import validate_currencies, return_fail_json, valid_api_key, get_conversion_rate
import logging
log = logging.getLogger(__name__)
app = Flask(__name__)

service_unavailable_message = f"Service unavailable. Contact support."


@app.route("/get-rate/<string:rate1>/<string:rate2>")
def get_currency_rate(rate1, rate2) -> Response:
    """Get currency conversion rate."""
    log.info(f"Get currency rate. {rate1}, {rate2}")
    inputs = [rate1, rate2]

    if not valid_api_key():
        return jsonify(return_fail_json(service_unavailable_message, inputs))

    validation_success, message = validate_currencies(rate1, rate2)
    if validation_success:
        conversion_rate = get_conversion_rate(rate1, rate2)
        json_success_return = {"inputs": inputs, "module_requested": "get-rate",
                               "success": True, "status": "success", "conversion_rate": conversion_rate}
        return jsonify(json_success_return)
    else:
        return jsonify(return_fail_json(message, inputs))


@app.route("/convert-rate/<string:rate1>/<string:rate2>/<float:amount>")
def convert_rate(rate1: str, rate2: str, amount: float) -> Response:
    """Get conversion rate.  You will get a 404 if amount is not a float.  100 --> 100.0"""
    log.info(f"convert currency rate. {rate1}, {rate2}. Amount: {amount}")
    inputs = [rate1, rate2, amount]
    if not valid_api_key():
        return jsonify(return_fail_json(service_unavailable_message, inputs))

    validation_success, message = validate_currencies(rate1, rate2)
    if validation_success:
        conversion_rate = get_conversion_rate(rate1, rate2)
        conversion_amount = amount*conversion_rate
        json_success_return = {"inputs": inputs, "module_requested": "convert-rate", "success": True,
                               "status": "success", "conversion_rate": conversion_rate,
                               "conversion_amount": round(conversion_amount,2)}
        return jsonify(json_success_return)
    else:
        return jsonify(return_fail_json(message, inputs))
