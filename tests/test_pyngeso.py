import csv
import json
from datetime import date, datetime, timedelta

from pyngeso import NgEso


#
def test_dx_eac_eso_buy_orders():
    date_col = "deliveryStart"
    start_date = datetime(2023, 11, 2, 23)
    end_date = datetime(2023, 11, 3, 23)
    client = NgEso("dx-eac-eso-buy-orders")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0


def test_dx_eac_eso_results_summary():
    date_col = "deliveryStart"
    start_date = datetime(2023, 11, 2, 23)
    end_date = datetime(2023, 11, 3, 23)
    client = NgEso("dx-eac-eso-results-summary")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")

    for r in records:
        print(r)
    assert isinstance(records, list)
    assert len(records) > 0
    assert len(records) == 42


def test_dx_eac_eso_sell_orders():
    date_col = "deliveryStart"
    start_date = datetime(2023, 11, 2, 23)
    end_date = datetime(2023, 11, 3, 23)
    client = NgEso("dx-eac-eso-sell-orders")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0


def test_br_eac_eso_buy_orders():
    date_col = "deliveryStart"
    start_date = datetime(2024, 3, 14, 23)
    end_date = datetime(2024, 3, 15, 23)
    client = NgEso("br-eac-eso-buy-orders")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0


def test_br_eac_eso_results_by_units():
    date_col = "deliveryStart"
    start_date = datetime(2024, 3, 14, 23)
    end_date = datetime(2024, 3, 15, 23)
    client = NgEso("br-eac-eso-results-by-units")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0


def test_br_eac_eso_results_summary():
    date_col = "deliveryStart"
    start_date = datetime(2024, 3, 14, 23)
    end_date = datetime(2024, 3, 15, 23)
    client = NgEso("br-eac-eso-results-summary")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0
    assert len(records) == 98


def test_br_eac_eso_sell_orders():
    date_col = "deliveryStart"
    start_date = datetime(2024, 3, 14, 23)
    end_date = datetime(2024, 3, 15, 23)
    client = NgEso("br-eac-eso-sell-orders")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0


def test_demand_data_update():
    date_col = "SETTLEMENT_DATE"
    start_date = (datetime.now() - timedelta(days=1)).date()
    end_date = (datetime.now() - timedelta(days=1)).date()
    client = NgEso("demand-data-update")
    r = client.query(date_col=date_col, start_date=start_date, end_date=end_date)

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0
    unique_target_dates = {record.get(date_col) for record in records}
    assert len(unique_target_dates) == 1
    assert len(records) == 48


def test_demand_data_update_with_filter():
    date_col = "SETTLEMENT_DATE"
    start_date = (datetime.now() - timedelta(days=1)).date()
    end_date = (datetime.now() - timedelta(days=1)).date()
    filter_condition = "\"FORECAST_ACTUAL_INDICATOR\" = 'A'"
    client = NgEso("demand-data-update")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
        filters=[filter_condition],
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0
    unique_target_dates = {record.get(date_col) for record in records}
    assert len(unique_target_dates) == 1
    assert len(records) == 48


def test_dc_volume_forecast():
    date_col = "Forecast_Target_Date"
    start_date = date(2022, 5, 21)
    end_date = date(2022, 5, 21)
    filter_condition = "\"Service_Type\" = 'DC-L'"
    client = NgEso("dc-volume-forecast")
    r = client.query(
        date_col=date_col,
        start_date=start_date,
        end_date=end_date,
        filters=[filter_condition],
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0
    unique_target_dates = {record.get(date_col) for record in records}
    assert len(unique_target_dates) == 1
    assert len(records) == 4


def test_transmission_entry_capacity_tec_register():
    start_date = datetime(2024, 3, 14, 23)
    end_date = datetime(2024, 3, 15, 23)
    client = NgEso("transmission-entry-capacity-tec-register")
    r = client.query(
        start_date=start_date,
        end_date=end_date,
    )

    assert isinstance(r, bytes)
    r_dict = json.loads(r)
    records = r_dict.get("result").get("records")
    assert isinstance(records, list)
    assert len(records) > 0


def test_historic_generation_mix():
    client = NgEso("historic-generation-mix", "file")
    r = client.download_file()
    # test response type
    assert isinstance(r, bytes)

    # test bytes -> csv
    decoded_content = r.decode("utf-8")
    c = csv.reader(decoded_content.splitlines(), delimiter=",")
    headers_row = next(c)
    first_row = next(c)

    assert "DATETIME" in headers_row
    assert "2009-01-01 00:00:00" in first_row
    assert len(headers_row) == len(first_row)
