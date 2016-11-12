from csv import reader

# reading csv file of nse-dataset-codes
csv_file = open("../NSE-datasets-codes.csv")
csv_rows = list(reader(csv_file))
rows = len(csv_rows)

number_of_stocks = 20
# for each stock do the following
# for i in range(0, rows):
for i in range(0, number_of_stocks):
    companycode = csv_rows[i][0]
    print(companycode)

                        # The headers are as follows:
# ---------------------------------------------------------------------------------
#   Date    Open   High   Low   Last  Close  Total Trade-Quantity  Turnover(Lacs)
# ---------------------------------------------------------------------------------