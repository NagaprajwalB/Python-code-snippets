print("-----------Menu----------")
print("1.Breakfast\n2.Lunch\n3.Dinner\n4.Snacks\n5.Beverages")
option = int(input("Enter your Choise:"))
print("---------------------------------")
match option:
    case 1:
        print("You have selected Breakfast")
        print("1.Idly\n2.Dosa\n3.Puri\n4.Uppittu")
        option1 = int(input("What would you like to have for bre;akfast:"))
        match option1:
            case 1:
                print("You have selected Idly - Rs.10")
                plates = int(input("Enter number of Plates:"))
                amount = 10 * plates
                gst = amount * 0.05
                payable_amount = amount + (amount * 0.05)
                print("--------------Bill---------------")
                print("Amount:",amount)
                print("GST 5%",gst)
                print("---------------------------------")
                print("Total Payable Amount: Rs",payable_amount)
            case 2:
                print("You have selected Dosa - Rs.20")
                plates = int(input("Enter number of Plates:"))
                amount = 20 * plates
                gst = amount * 0.05
                payable_amount = amount + (amount * 0.05)
                print("--------------Bill---------------")
                print("Amount:",amount)
                print("GST 5%",gst)
                print("---------------------------------")
                print("Total Payable Amount: Rs",payable_amount)
            case 3:
                print("You have selected Puri - Rs.30")
                plates = int(input("Enter number of Plates:"))
                amount = 30 * plates
                gst = amount * 0.05
                payable_amount = amount + (amount * 0.05)
                print("--------------Bill---------------")
                print("Amount:",amount)
                print("GST 5%",gst)
                print("---------------------------------")
                print("Total Payable Amount: Rs",payable_amount)
            case 4:
                print("You have selected Uppittu - Rs.10")
                plates = int(input("Enter number of Plates:"))
                amount = 10 * plates
                gst = amount * 0.05
                payable_amount = amount + (amount * 0.05)
                print("--------------Bill---------------")
                print("Amount:",amount)
                print("GST 5%",gst)
                print("---------------------------------")
                print("Total Payable Amount: Rs",payable_amount)
            case 5: 
                print("You have selected Bisibele Bath - Rs.30")
                plates = int(input("Enter number of Plates:"))
                amount = 30 * plates
                gst = amount * 0.05
                payable_amount = amount + (amount * 0.05)
                print("--------------Bill---------------")
                print("Amount:",amount)
                print("GST 5%",gst)
                print("---------------------------------")
                print("Total Payable Amount: Rs",payable_amount)
            case _:
                print("Invalid Option")
               

                