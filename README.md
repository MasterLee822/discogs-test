# Discogs Recruiting Takehome Assignment: Currency

Thanks for applying at Discogs!

We want to assess your technical ability, but we also think coding under pressure in an interview is a terrible way to do that. As a compromise, here's a takehome exercise that's a simplified version of work you'd be doing at Discogs if you were hired.

Our expectations are that you deliver functional software including readable, concise and maintainable code with some production considerations.

We do not expect you to host this, returning a zip will be suffient.

If we've made an error so grievous that you don't think you can finish the assignment, or you have any other questions after reviewing this document, feel free to email your contact at Discogs and let us know.

## Description of the Problem

As we break the Discogs monolith up into smaller microservices, currency is one of our targets to break away from our main site.

Your assignment is to create a simple currency service that can provide conversion rates and convert currencies for consumers.

To keep this assignment short, you only need to support US Dollars, British Pounds Sterling, and Euros.
Wherever currencies appear in URL parameters or return data, you should specify them by their ISO 4217 codes (USD, GBP, EUR).

To provide conversion rates, feel free to use any publicly-available free currency exchange APIs - please do not spend any money at all on this assignment.
Here are a few suggestions:
- https://freecurrencyapi.net/#documentationSection
  - Here is a key you can use for this project. `V6m3vwqx7XXBcA7Mxfvfxnkc291IhIKgJwYrZcqe`
- https://currencylayer.com/documentation (registration required)
- https://openexchangerates.org/ (registration required)


## Setup

In this directory, we've included everything you should need to run a simple Flask-based API using Docker Compose.

In case you're not too familiar with Flask, Python, or Docker, we've included a couple example API endpoints to illustrate how routing and responses work.

Assuming you have a working Docker installation locally, you should be able to just run:

`docker-compose up`

to start the app. It should be accessible on port `35000` of your docker machine's IP address.

For consuming the public currency conversion API, we've included the `requests` library, arguably Python's most popular and easiest-to-use HTTP client.

If you'd like to use a different runtime environment than `Docker` and `Python`, that's totally fine.
Please include instructions on how to run your application, in that case.

Feel free to provide any feedback about the problem or this prompt, e.g. as comments in your code.

## Goal

Please add the following endpoints to this API:

- a `GET` endpoint to get a currency rate
    - Returns the conversion rate from currency1 to currency2 as a floating point number.
    - The rate should be the value of 1 unit of currency1 in currency2.
    - The return value should be a `JSON` object restating the request parameters and the rate.

- a `GET` endpoint that converts a value in one currency to another
    - returns an amount in one currency, converted to an amount in another currency.
    - The return value should be a `JSON` object restating the request parameters and the converted amount.
    - All results should be rounded to 2 decimal points.


## Finished?

Congrats!

To get the code back to us, please:
- zip it up and email it to your contact at Discogs

See you soon, and thank you!
Discogs Marketplace

