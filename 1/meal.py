def main():
    answer = input("What time is it?   ")  # request for time input

    tym = convert(answer)  # call the convert function

    if tym >= 7 and tym <= 8:  # returns true if time falls between 7am and 8am
        print("breakfast time")
    elif tym >= 12 and tym <= 13:  # returns true if time falls between 12pm and 1pm
        print("lunch time")
    elif tym >= 18 and tym <= 19:  # returns true if time falls between 6pm and 7pm
        print("dinner time")
    else:
        print("Obolo, its not time to eat") # result if none of the conditions are met


def convert(time):
    h, m = time.split(":")  # separate user's input with the ":" delimitter

    # convert string part of minute to float and divide by 60
    min = float(m) / 60

    return float(h) + min  # convert hour to float and add to minute


main()
