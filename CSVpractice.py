# using reader and dictreader and writer DictWriter
from csv import reader, DictReader, writer, DictWriter 

"""pickling syntax writing and readeig
import pickle # uses for take data and restore whenever was needed
with open("Filename.pickle", "wb") as file:
    pickle.dump(object, file)

with open("Filename.pickle","rb") as file:
    veriable = pickle.load(file)
"""


with open("fighters.csv") as file:
    csv_reader = reader(file)
    #data = list(reader(file)) turns as a list 
    next(csv_reader)# using for passing header line
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

with open("fighters.csv") as file:
    csv_reader = DictReader(file , delimiter=",") #delimeter using for change separatin behavior. "," is stok version.
    for f in csv_reader:
        #Each row returns as a dict
        print(f)

with open("StreetFighters.csv" , "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character","move"])
    csv_writer.writerow(["Ryu","Haduken"])
    csv_writer.writerow(["Bermel","Hug"])

with open("StreetFighters.csv", "w") as file:
    headrs = ["CharName","SpecialMove"]
    csv_writer = DictWriter(file , fieldnames=headrs)
    csv_writer.writeheader()
    csv_writer.writerow({
        "CharName":"Bermel",
        "SpecialMove":"Punch"
    })

    