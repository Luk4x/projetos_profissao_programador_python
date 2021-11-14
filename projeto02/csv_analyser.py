import pandas as pd


def read_csv(filepath):
    return pd.read_csv(filepath)


def read_as_list(filepath):
    df = read_csv(filepath)
    return df.values.tolist()


def analyze(filepath):
    df = read_csv(filepath)

    sum_sales = df.groupby(["Date"]).sum().reset_index()
    qty_sales = df.groupby(["Date"]).count().reset_index()

    min_value = sum_sales["Sale"].min()
    row_min_value = sum_sales[sum_sales["Sale"] == min_value]

    max_value = sum_sales["Sale"].max()
    row_max_value = sum_sales[sum_sales["Sale"] == max_value]

    min_qty = qty_sales["Sale"].min()
    row_min_qty = qty_sales[qty_sales["Sale"] == min_qty]

    max_qty = qty_sales["Sale"].max()
    row_max_qty = qty_sales[qty_sales["Sale"] == max_qty]

    dict_result = {
        "min_value": {
            "date": row_min_value["Date"].values[0],
            "value": row_min_value["Sale"].values[0],
        },
        "max_value": {
            "date": row_max_value["Date"].values[0],
            "value": row_max_value["Sale"].values[0],
        },
        "min_qty": {
            "date": row_min_qty["Date"].values[0],
            "value": row_min_qty["Sale"].values[0],
        },
        "max_qty": {
            "date": row_max_qty["Date"].values[0],
            "value": row_max_qty["Sale"].values[0],
        },
    }

    return dict_result