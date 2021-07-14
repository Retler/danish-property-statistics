# Boliga house market statistics scraper
Boliga.dk exposes an [API](https://api.boliga.dk/) with various statistics on the housing market.
This small script uses the API to fetch the historical number of properties for sale in Denmark and
the historical square meter price. The data is partitioned by:
* Region (hovedstaden|sjaelland|midtjylland|all)
* Property type (villa|terraced house|holiday home|appartment|country estate|lots)
* Month and year
