import datetime
orderdate = None
while orderdate == None:
    try:
                orderdate = input('Please enter the order date (format YYYY-MM-DD): ')
                checkdate = orderdate.split('-')
                print(datetime.date(int(checkdate[0]),int(checkdate[1]),int(checkdate[2])))

    except:
                print('Invalid date entered. Please try again.')
                orderdate = None

itemsordered = None
while itemsordered == None:
        try:
            itemsordered = input('Please enter the items to be ordered seperated by a comma(I.e 3,4,5): ')
            itemsordered.strip()
            checkitems = itemsordered.split(',')
            for item in checkitems:
                int(item)
        except:
            print('Invalid data entered. Please try again ensuring ONLY commas(,) seperate values.' )
            itemsordered = None