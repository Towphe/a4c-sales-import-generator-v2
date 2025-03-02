import numpy as np
import pandas as pd
from openpyxl import Workbook, worksheet, load_workbook
# from openpyxl.styles import PatternFill, numbers, NamedStyle, Alignment
from openpyxl.styles import numbers, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
from .sales_order_code_generator import generate_sales_order_str
from .sales_persons import sales_persons_dict
import sys
from datetime import datetime

def generate_sales_import(data: pd.DataFrame, starting_num: int, output_dir  = "../../temp", version = "v1"):
    # create instance of template file
    wb = load_workbook("src/temp/TEMPLATE.xlsx")

    ws = wb.active

    previous_r = None
    current_si_no = starting_num
    # iterate thru every row of dataframe
    ctr = 7

    # print(data)
    for r in dataframe_to_rows(data, index=False, header=False):
        if previous_r == None:
            r[0] = generate_sales_order_str(current_si_no)
            current_si_no += 1
            previous_r = r

            dt_temp = datetime.strptime(r[1], '%d-%m-%Y %H:%M').strftime('%m/%d/%Y')
            ws.cell(row=ctr,column=2).value = dt_temp
            ws.cell(row=ctr,column=4).value = dt_temp
        elif r[9] != previous_r[9]:
            r[0] = generate_sales_order_str(current_si_no)
            current_si_no += 1
            previous_r = r

            dt_temp = datetime.strptime(r[1], '%d-%m-%Y %H:%M').strftime('%m/%d/%Y')
            ws.cell(row=ctr,column=2).value = dt_temp
            ws.cell(row=ctr,column=4).value = dt_temp
        else:
            # check stock code first
            for i in range(0,16):
                r[i] = ""

        ws.cell(row=ctr,column=1).value = r[0]
        ws.cell(row=ctr,column=3).value = r[2]
        ws.cell(row=ctr,column=5).value = r[4]
        ws.cell(row=ctr,column=6).value = r[5]
        ws.cell(row=ctr,column=7).value = r[6]
        ws.cell(row=ctr,column=8).value = r[7]
        ws.cell(row=ctr,column=9).value = r[8]
        ws.cell(row=ctr,column=10).value = str(r[9])
        ws.cell(row=ctr,column=10).number_format = '0'
        print(ws.cell(row=ctr,column=10).value, flush=True)
        ws.cell(row=ctr,column=11).value = r[10]
        ws.cell(row=ctr,column=12).value = r[11]
        ws.cell(row=ctr,column=13).value = r[12]
        ws.cell(row=ctr,column=14).value = r[13]
        ws.cell(row=ctr,column=15).value = r[14]
        ws.cell(row=ctr,column=16).value = r[15]
        ws.cell(row=ctr,column=17).value = r[16]
        ws.cell(row=ctr,column=18).value = r[17]
        ws.cell(row=ctr,column=19).value = r[18]
        ws.cell(row=ctr,column=20).value = r[19]
        ws.cell(row=ctr,column=21).value = r[20]
        ws.cell(row=ctr,column=22).value = r[21]
        ws.cell(row=ctr,column=23).value = r[22]
        ws.cell(row=ctr,column=24).value = r[23]
        ws.cell(row=ctr,column=25).value = r[24]
        ws.cell(row=ctr,column=26).value = r[25]
        ws.cell(row=ctr,column=27).value = r[26]
        ws.cell(row=ctr,column=28).value = r[27]
        ws.cell(row=ctr,column=29).value = r[28]
        ws.cell(row=ctr,column=30).value = r[29]
        ws.cell(row=ctr,column=31).value = r[30]
        ws.cell(row=ctr,column=32).value = r[31]
        ws.cell(row=ctr,column=33).value = r[32]
        ws.cell(row=ctr,column=34).value = r[33]
        ws.cell(row=ctr,column=35).value = r[34]
        ws.cell(row=ctr,column=36).value = r[35]
        ws.cell(row=ctr,column=37).value = r[36]
        ws.cell(row=ctr,column=38).value = r[37]
        ws.cell(row=ctr,column=39).value = r[38]
        ws.cell(row=ctr,column=40).value = r[39]
        ws.cell(row=ctr,column=41).value = r[40]
        ws.cell(row=ctr,column=42).value = r[41]
        ws.cell(row=ctr,column=43).value = r[42]
        ws.cell(row=ctr,column=44).value = r[43]
        ws.cell(row=ctr,column=45).value = r[44]
        ws.cell(row=ctr,column=46).value = r[45]
        ws.cell(row=ctr,column=47).value = r[46]
        ws.cell(row=ctr,column=48).value = r[47]
        ws.cell(row=ctr,column=49).value = r[48]
        ws.cell(row=ctr,column=50).value = r[49]
        ws.cell(row=ctr,column=51).value = r[50]
        ws.cell(row=ctr,column=52).value = r[51]
        ws.cell(row=ctr,column=53).value = r[52]
        ws.cell(row=ctr,column=54).value = r[53]
        ws.cell(row=ctr,column=55).value = r[54]
        ws.cell(row=ctr,column=56).value = r[55]
        ws.cell(row=ctr,column=57).value = r[56]
        ws.cell(row=ctr,column=58).value = r[57]
        ws.cell(row=ctr,column=59).value = r[58]
        ws.cell(row=ctr,column=60).value = r[59]
        ws.cell(row=ctr,column=61).value = r[60]
        ws.cell(row=ctr,column=62).value = r[61]

        # make sure fill is white
        for col in ws['A':'BJ']:
            col[0].fill = PatternFill(start_color='FFFFFF', fill_type="solid")
        ctr += 1

    wb.save(output_dir)
    return True
