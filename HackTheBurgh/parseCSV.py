import csv

if __name__ == "__main__":

    with open('market_data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        instruments = []
        bid_prices = []
        bid_volumes = []
        for row in readCSV:
            instrument = row[1]
            instruments.append(instrument)

        print(instruments)
           
        


