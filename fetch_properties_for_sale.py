import requests
import pandas as pd

ROOT_URL="https://api.boliga.dk/api/v2/statistics"
FOR_SALE_API="/graphpropertiesforsale"
METER_PRICE_API="/graphaveragesquaremeterpricebbr"

PROPERTY_TYPES={"Villa": "1", 
            "Raekkehus": "2", 
            "Ejerlejlighed": "3", 
            "Fritidshus": "4", 
            "Andelsbolig": "5", 
            "Landejendom": "6", 
            "Helaarsgrund": "7", 
            "Fritidsgrund": "8",
            "Alle": ""
}

REGIONS = {"Hovedstaden": "hovedstaden", "Alle": "", "Midtjylland": "midtjylland", "Sjaelland": "sjaelland"}

# Gets the number of house for sale in Denmark grouped by month, year, region and type of property
def get_n_houses_for_sale():
    data = pd.DataFrame()
    for property_type in PROPERTY_TYPES:
        for region in REGIONS:
            print(f"fetching data for property_type: {bolig_type}, region: {region}")
            res = requests.get(ROOT_URL+FOR_SALE_API, params={"zipcode": "", "type": PROPERTY_TYPES[property_type], "region": REGIONS[region]})
            if res.status_code != 200:
                print(f"Could not get property_type: {bolig_type}, region: {region}, status_code: {res.status_code}")
                continue
            properties_for_sale = pd.DataFrame(res.json())
            properties_for_sale["region"] = region
            properties_for_sale["property_type"] = bolig_type
            data = pd.concat([data, properties_for_sale])
    return data

# Gets the house prices in Denmark grouped by month, year, region and type of property
def get_historical_house_prices():
    data = pd.DataFrame()
    for property_type in PROPERTY_TYPES:
        for region in REGIONS:
            print(f"fetching data for property_type: {bolig_type}, region: {region}")
            res = requests.get(ROOT_URL+METER_PRICE_API, params={"zipcode": "", "type": PROPERTY_TYPES[property_type], "region": REGIONS[region]})
            if res.status_code != 200:
                print(f"Could not get property_type: {bolig_type}, region: {region}, status_code: {res.status_code}")
                continue
            property_prices = pd.DataFrame(res.json())
            property_prices["region"] = region
            property_prices["property_type"] = bolig_type
            data = pd.concat([data, property_prices])
    return data

if __name__ == "__main__":
    n_houses_data = get_n_houses_for_sale()
    n_houses_data.to_csv("n_houses_data", index=False)

    house_prices_data = get_historical_house_prices()
    house_prices_data.to_csv("house_prices_data", index=False)
