# pyngeso

Simple python wrapper for the National Energy System Operator Portal.

## Getting started

###  Example usage

```python
from pyngeso import NgEso

resource = "historic-day-ahead-demand-forecast"
date_col = "TARGETDATE"
start_date = "2018-01-01"
end_date = "2018-01-01"

client = NgEso(resource)
# returns content of response
r: bytes = client.query(date_col=date_col, start_date=start_date, end_date=end_date)
```

## Tested reports

### Queryable via NG's api

* `demand-data-update`
* `transmission-entry-capacity-tec-register`
* `dx-eac-eso-results-summary`
* `dx-eac-eso-sell-orders`
* `dx-eac-eso-buy-orders`
* `br-eac-eso-results-summary`
* `br-eac-eso-sell-orders`
* `br-eac-eso-buy-orders`
* `br-eac-eso-results-by-units`

### Download of files

* `historic-generation-mix`
