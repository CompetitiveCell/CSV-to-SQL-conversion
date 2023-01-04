from csv import writer

file = open("rank_data.csv", "w")
write = writer(file)

choice = int(input("Enter how many data to enter : "))
write.writerow(["Name", "Roll_Number", "Ranks"])
for i in range(choice):
    name = input("Enter Name : ")
    roll_no = input("Enter Roll Number : ")
    rank = input("Enter Olympiad Rank : ")
    data_list = [name, roll_no, rank]
    write.writerow(data_list)

print("Data saved in a file named : rank_data.csv")
file.close()
