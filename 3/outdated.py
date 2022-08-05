# list of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# loop forever
while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        year = year.replace(" ", "")
        month = month.replace(" ", "")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            month_alt, day_alt, year_alt = date.split(" ")
            for ind in range(len(months)):
                if month_alt == months[ind]:
                    month = ind + 1
            if not day_alt.endswith(","):
                continue
            day = day_alt.replace(",", "")
            year = year_alt
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass


print(f"{year}-{int(month):02}-{int(day):02}")
