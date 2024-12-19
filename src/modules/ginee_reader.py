import numpy as np
import pandas as pd
from datetime import datetime, date
from pandas.core.arrays import boolean
from .sales_persons import sales_persons_dict

# function that extracts data from ginee
def extract_from_ginee(xl_dir: str) -> pd.DataFrame:
    ginee:pd.DataFrame = pd.read_excel(xl_dir).fillna(method='ffill')
    if (ginee["Channel"].unique().__len__() != 1 or ginee["Store Name"].unique().__len__() != 1):
        # invalid; document must only have one channel and/or store name
        return None

    output = convert_ginee_to_output(ginee)

    # check if output is valid
    if type(output) != pd.DataFrame:
        return None

    #return (output, sales_persons_dict[ginee["Channel"]][""])
    #return output
    return {
        'output' : output,
        'filename' : sales_persons_dict[ginee['Channel'][0]][ginee["Store Name"][0]]['filename']
    }


def convert_ginee_to_output(ginee_pd: pd.DataFrame) -> pd.DataFrame:
    output_pd = pd.DataFrame()
    try:
        output_pd["SalesOrderCode"] = ""
        output_pd["SalesOrderDate"] = ginee_pd["Create Time"]
        output_pd["IsApproved"] = True
        output_pd["TaxDate"] = ginee_pd["Create Time"]
        output_pd["Debtor"] = sales_persons_dict[ginee_pd["Channel"].array[0]][ginee_pd["Store Name"].array[0]]["debtor"]
        output_pd["CurrencyRate"] = "N8"
        output_pd["ReverseRate"] = ""
        output_pd["SalesPerson"] = sales_persons_dict[ginee_pd["Channel"].array[0]][ginee_pd["Store Name"].array[0]]["name"]
        output_pd["Term"] = "C.O.D."
        output_pd["ReferenceNo"] = ginee_pd["Order ID"]
        output_pd["Ref1"] = ginee_pd["Recipient Name"]
        output_pd["Ref2"] = ginee_pd["Recipient Address"]
        output_pd["Ref3"] = ginee_pd["District"]
        output_pd["Ref4"] = ginee_pd["City"]
        output_pd["Ref5"] = ginee_pd["Province"]
        output_pd["Remark1"] = ""
        output_pd["Remark2"] = ""
        output_pd["Remark3"] = ""
        output_pd["Remark4"] = ""
        output_pd["Remark5"] = ""
        output_pd["Project"] = ""
        output_pd["StockLocation"] = ""
        output_pd["DORegistationNo"] = ""
        output_pd["DOArea"] = ""
        output_pd["CostCentre"] = ""
        output_pd["IsCancelled"] = ""
        output_pd["IsTaxInclusive"] = True
        output_pd["IsRounding"] = ""
        output_pd["IsNonTaxInvoice"] = ""
        output_pd["_"] = "" # COL `AD` - whole column must be grey
        output_pd["ProgressInvoicingRate"] = ""
        output_pd["SerialNumber"] = ""
        output_pd["StockType"] = ""
        output_pd["StockBatchNumber"] = ""
        output_pd["DebtorItem"] = ""
        output_pd["PackingUOM"] = ""
        output_pd["Packing"] = ""
        output_pd["PackingQty"] = ""
        output_pd["Stock"] = ginee_pd["SKU"]
        output_pd["StockLocation_2"] = ""
        output_pd.rename(columns={"StockLocation_2": "StockLocation"}, inplace=True)
        output_pd["Qty"] = ginee_pd["Qty"]
        output_pd["UOM"] = "UNIT(S)"
        output_pd["UnitPrice"] = ginee_pd["Product Discounted Price"]
        output_pd["Discount"] = ""
        output_pd["CostCentre_2"] = ""
        output_pd.rename(columns={"CostCentre_2": "CostCentre"}, inplace=True)
        output_pd["Description"] = ginee_pd["Product Name"]
        output_pd["IsTaxInclusive_2"] = True
        output_pd.rename(columns={"IsTaxInclusive_2": "IsTaxInclusive"}, inplace=True)
        output_pd["Project_2"] = ""
        output_pd.rename(columns={"Project_2": "Project"}, inplace=True)
        output_pd["ReferenceNo_2"] = ""
        output_pd.rename(columns={"ReferenceNo_2": "ReferenceNo"}, inplace=True)
        output_pd["Ref"] = ""
        output_pd["Ref2_2"] = ""
        output_pd.rename(columns={"Ref2_2": "Ref2"}, inplace=True)
        output_pd["Ref3_2"] = ""
        output_pd.rename(columns={"Ref3_2": "Ref3"}, inplace=True)
        output_pd["Ref4_2"] = ""
        output_pd.rename(columns={"Ref4_2": "Ref4"}, inplace=True)
        output_pd["Ref5_2"] = ""
        output_pd.rename(columns={"Ref5_2": "Ref5"}, inplace=True)
        output_pd["DateRef1"] = ""
        output_pd["DateRef2"] = ""
        output_pd["NumRef1"] = ""
        output_pd["NumRef2"] = ""
        output_pd["TaxCode"] = "SR-SP"
        output_pd["TaxRate"] = "12.00%"
        output_pd["WTaxCode"] = 0.00
        output_pd["WTaxRate"] = 0.00
    except:
         return None

    # convert `ReferenceNo` column to number format
    # pd.to_numeric(output_pd["ReferenceNo"])

    return output_pd

# df = extract_from_ginee(ginee_file_dir)
