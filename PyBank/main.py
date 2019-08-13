import os
import csv
bank_path = os.path.join("Resources", "budget_data.csv")

months = []
profit_lossess = []

with open(bank_path, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        months.append(row[0])
        profit_lossess.append(int(row[1]))

    net_total_amount = 0
    for row in csvreader:
        net_total_amount += int(row[1])

    change_PL = []
    for x in range(1, len(profit_lossess)):
        change_PL.append((int(profit_lossess[x]) - int(profit_lossess[x-1])))

    avg_change_PL = sum(change_PL) / len(change_PL)

    total_months = len(months)

    print("Financial Analysis")

    print("---------------------------------------------------")

    print("Total months: " + str(total_months))

    print("Total amount of P&L: " + "$" + str(net_total_amount))

    print("Average change in P&L: " + "$" + str(avg_change_PL))

output_file = os.path.join("output.txt")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow("Financial Analysis")
    writer.writerows("----------------------------------------")

    writer.writerows("Total months: " + str(total_months))

    writer.writerows("Total amount of P&L: " + "$" + str(net_total_amount))

    writer.writerows("Average change in P&L: " + "$" + str(avg_change_PL))
    





