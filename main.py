from item import Item


def calculate_sum(state: str, items: list[Item]):
    sum = 0
    rates = fetch_rates()

    for item in items:
        tax = 0.01 * float(rates[state][item.category])
        cost_with_tax = item.cost * (1.0 + tax)
        sum += cost_with_tax

    return round(sum, 2)


def fetch_rates():
    rates_file = open("../taxrates.txt", "r")
    rates_JSON = rates_file.read()
    # Cleans up JSON into a dict organized by state
    rates_by_state = parse_JSON(rates_JSON)

    return rates_by_state


def parse_JSON(raw_JSON: str) -> dict:
    # Removes {} from beginning and end of file.
    list_JSON = raw_JSON[1:-1]
    # Removes all new line characters
    list_JSON = list_JSON.replace("\n", "")
    # Parses JSON to isolate entries for each state. Removes empty set that appears at the end.
    list_JSON = list_JSON.split("]")[:-1]
    #declare clean_JSON before working with it
    clean_JSON = dict()

    for item in list_JSON:
        # item should be split into the state code and a dict of its tax rates
        raw_dict = item.split("[    ")
        # Removes formatting characters from state code
        state = raw_dict[0].replace("\"", "").replace(":", "")
        # Removes formatting characters from tax rate dictionary
        rates = raw_dict[1].replace("\"", "").replace("{", "").replace("}", "")

        # Make a list of the different tax rates and convert rates to an empty dictionary
        itemized_rates = rates.split(", ")
        rates = dict()

        for rate in itemized_rates:
            split_rate = rate.split(":")
            category = split_rate[0]
            percent = split_rate[1]

            rates[category] = percent

        clean_JSON[state] = rates

    return clean_JSON
