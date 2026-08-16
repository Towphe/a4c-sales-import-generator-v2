import pandas as pd
from .sales_persons import sitegiant_marketplace_dict


def extract_from_sitegiant(xl_dir: str) -> dict:
    """Read a SiteGiant Excel export and return a standardised output dict.

    The file may contain orders from multiple marketplaces. Each row's
    marketplace is looked up individually so mixed exports are supported.

    Returns:
        {'output': pd.DataFrame, 'filename': str}

    Raises:
        ValueError  on validation failure, unknown marketplace, or missing config
    """
    try:
        sitegiant: pd.DataFrame = pd.read_excel(xl_dir, dtype=str)
    except Exception as e:
        raise ValueError(f"Could not read Excel file: {e}") from e

    # Forward-fill order-level fields so that multi-item orders have values on
    # every row (SiteGiant only populates them on the first row per order).
    order_level_cols = [
        'order_id', 'order_status', 'payment_status', 'marketplace',
        'marketplace_order_id', 'shipping_method', 'order_creation_date',
        'shipping_firstname', 'shipping_lastname', 'shipping_address1',
        'shipping_town', 'shipping_city', 'shipping_state',
    ]
    for col in order_level_cols:
        if col in sitegiant.columns:
            sitegiant[col] = sitegiant[col].ffill()

    # Validate all marketplaces present in the file are configured and complete.
    for marketplace in sitegiant['marketplace'].unique():
        if marketplace not in sitegiant_marketplace_dict:
            raise ValueError(
                f"Marketplace '{marketplace}' is not configured. "
                "Add it to sitegiant_marketplace_dict in sales_persons.py."
            )
        store_info = sitegiant_marketplace_dict[marketplace]
        if 'TODO' in store_info.get('debtor', '') or 'TODO' in store_info.get('name', ''):
            raise ValueError(
                f"Marketplace '{marketplace}' has not been configured yet. "
                "Please update sitegiant_marketplace_dict in sales_persons.py."
            )

    output = _convert_sitegiant_to_output(sitegiant)

    # Use a single marketplace's filename when the file contains only one;
    # fall back to a generic name for mixed exports.
    unique_marketplaces = sitegiant['marketplace'].unique()
    if len(unique_marketplaces) == 1:
        filename = sitegiant_marketplace_dict[unique_marketplaces[0]]['filename']
    else:
        filename = "SITEGIANT"

    return {
        'output': output,
        'filename': filename,
    }


def _convert_sitegiant_to_output(sg: pd.DataFrame) -> pd.DataFrame:
    """Map SiteGiant columns to the standard output DataFrame columns."""
    out = pd.DataFrame()
    out["SalesOrderCode"] = ""
    out["SalesOrderDate"] = sg["order_creation_date"]
    out["IsApproved"] = True
    out["TaxDate"] = sg["order_creation_date"]
    out["Debtor"] = sg["marketplace"].map(
        lambda m: sitegiant_marketplace_dict[m]["debtor"]
    )
    out["CurrencyRate"] = 1
    out["ReverseRate"] = ""
    out["SalesPerson"] = sg["marketplace"].map(
        lambda m: sitegiant_marketplace_dict[m]["name"]
    )
    out["Term"] = "C.O.D."
    out["ReferenceNo"] = sg["marketplace_order_id"]
    out["Ref1"] = (
        sg["shipping_firstname"].fillna("").str.strip()
        + " "
        + sg["shipping_lastname"].fillna("").str.strip()
    ).str.strip()
    out["Ref2"] = sg["shipping_address1"].fillna("")
    out["Ref3"] = sg["shipping_town"].fillna("")
    out["Ref4"] = sg["shipping_city"].fillna("")
    out["Ref5"] = sg["shipping_state"].fillna("")
    out["Remark1"] = ""
    out["Remark2"] = ""
    out["Remark3"] = ""
    out["Remark4"] = ""
    out["Remark5"] = ""
    out["Project"] = ""
    out["StockLocation"] = ""
    out["DORegistationNo"] = ""
    out["DOArea"] = ""
    out["CostCentre"] = ""
    out["IsCancelled"] = ""
    out["IsTaxInclusive"] = True
    out["IsRounding"] = ""
    out["IsNonTaxInvoice"] = ""
    out["_"] = ""  # COL AD - must be grey
    out["ProgressInvoicingRate"] = ""
    out["SerialNumber"] = ""
    out["StockType"] = ""
    out["StockBatchNumber"] = ""
    out["DebtorItem"] = ""
    out["PackingUOM"] = ""
    out["Packing"] = ""
    out["PackingQty"] = ""
    out["Stock"] = sg["product_sku"]
    out["StockLocation_2"] = ""
    out.rename(columns={"StockLocation_2": "StockLocation"}, inplace=True)
    out["Qty"] = pd.to_numeric(sg["product_quantity"], errors='coerce').fillna(0).astype(int)
    out["UOM"] = "UNIT(S)"
    out["UnitPrice"] = pd.to_numeric(sg["product_price"], errors='coerce').fillna(0)
    out["Discount"] = ""
    out["CostCentre_2"] = ""
    out.rename(columns={"CostCentre_2": "CostCentre"}, inplace=True)
    out["Description"] = sg["product_name"]
    out["IsTaxInclusive_2"] = True
    out.rename(columns={"IsTaxInclusive_2": "IsTaxInclusive"}, inplace=True)
    out["Project_2"] = ""
    out.rename(columns={"Project_2": "Project"}, inplace=True)
    out["ReferenceNo_2"] = ""
    out.rename(columns={"ReferenceNo_2": "ReferenceNo"}, inplace=True)
    out["Ref"] = ""
    out["Ref2_2"] = ""
    out.rename(columns={"Ref2_2": "Ref2"}, inplace=True)
    out["Ref3_2"] = ""
    out.rename(columns={"Ref3_2": "Ref3"}, inplace=True)
    out["Ref4_2"] = ""
    out.rename(columns={"Ref4_2": "Ref4"}, inplace=True)
    out["Ref5_2"] = ""
    out.rename(columns={"Ref5_2": "Ref5"}, inplace=True)
    out["DateRef1"] = ""
    out["DateRef2"] = ""
    out["NumRef1"] = ""
    out["NumRef2"] = ""
    out["TaxCode"] = "SR-SP"
    out["TaxRate"] = "12.00%"
    out["WTaxCode"] = 0.00
    out["WTaxRate"] = 0.00

    return out
