
def main():

    monthDays = [["January","31"],["February","28"],["March","31"],["April","30"],["May","31"],["June","30"],["July","31"],
        ["August","31"],["September","30"],["October","31"],["November","30"],["December","31"]]

    def askMonth():
        i = 0
        while i < 12:
            displayMonthNumber = i+1
            print(str(displayMonthNumber) + " " + monthDays[i][0])
            i += 1
        selectedMonthNumber = input("Enter a month number: ")
        arrayMonthNumber = int(selectedMonthNumber)-1
        return arrayMonthNumber

    def askDay(arrayMonthNumber):
        selectedDay = input("Enter start day of month (1-" + monthDays[arrayMonthNumber][1] + ")")
        return int(selectedDay)

    def askNumberOfLessons():
        numberOfLessons = input("Enter number of lessons: ")
        return int(numberOfLessons)

    def displayResults(arrayMonthNumber, finalDayNumber, numberOfLessons):
        i=0
        while i < numberOfLessons:

            if finalDayNumber > int(monthDays[arrayMonthNumber][1]):
                if arrayMonthNumber == 11:
                    arrayMonthNumber = 0
                else:
                    arrayMonthNumber = arrayMonthNumber + 1
                    
                finalDayNumber = 1

            print(monthDays[arrayMonthNumber][0] + " " + str(finalDayNumber) + " - Ch " + str(i+1) )
            finalDayNumber += 1
            i += 1

    arrayMonthNumber = askMonth()
    finalDayNumber = askDay(arrayMonthNumber)
    numberOfLessons = askNumberOfLessons()
    displayResults(arrayMonthNumber, finalDayNumber, numberOfLessons)

    input("ENTER to end program")

if __name__ == '__main__':
    main()