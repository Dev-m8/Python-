# Byte coding challenge - Script to parse csv file 
import csv
from datetime import datetime
from typing import TYPE_CHECKING

# Function to parse multiple date formats
def parse_date(date: str) -> str:
    for fmt in ('%m/%d/%Y','%Y/%m/%d', '%Y%m%d', '%m-%d-%Y', '%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%d%m%Y'):
        try:
            return datetime.strptime(date, fmt).strftime('%m/%d/%Y')
        except ValueError:
            pass
    return "null" # assumed we could set invalid date to null instead of raising exception

# Function to transform trade list with invalid date to list with valid date
def fmt_date_in_list(trade_list: list[list[str]]) -> list[list[str]]:
    new_trade_list = map(lambda x: [x[0], parse_date(x[1]), x[2], x[3]],trade_list)
    return new_trade_list

# Function will take input csv and return csv with updated dates
def update_csv(input_csv: str, output_csv: str) -> None:
    try:
        csv_file = open(input_csv, mode='r')
    except FileNotFoundError as e:
        print(e)
    else:
        parsed_csv_lines = list(csv.reader(csv_file))
        updated_csv_lines = fmt_date_in_list(parsed_csv_lines)
        csv_file.close
        try:
            new_csv_file = open(output_csv, mode='w')
        except Exception as e:
            print(e)
        else:
            new_csv_writer = csv.writer(new_csv_file, delimiter=',')
            for line in updated_csv_lines:
                new_csv_writer.writerow(line)
                new_csv_file.close

def main():
  update_csv("trades.csv", "updated_trades.csv")
  
if __name__== "__main__":
  main()

'''
Testing
(base) 192:byte-ch dev$ diff trades.csv updated_trades.csv 
1,2c1,2
< 10001,03/09/2022,200.00,100
< 10002,2022/03/09,300.00,50
---
> 10001,03/09/2022,200.00,100
> 10002,03/09/2022,300.00,50
'''
