import pandas as pd
from match import match


def updateTeams():
    print("Select group;\n1.Group A\n2.Group B")
    group = int(input("Enter group number : "))
    if(group == 1):
        print("Please select a team;\n1.Srilanka\n2.India\n3.WestIndies\n4.Bangladesh")

        o = int(input("Enter a team number : "))
        if(o == 1):
            data = pd.read_csv("files/groupa/srilanka.csv")
            print(data)
            temp = int(input("Enter player index to update : "))
            p_name = input("Enter name to replace : ")
            p_role = input("Enter player role : ")
            data.at[temp, 'Player_Name'] = p_name
            data.at[temp, 'Player_Role'] = p_role
            data.to_csv("files/groupa/srilanka.csv", index=False)
            print(data)

        elif(o == 2):
            data = pd.read_csv("files/groupa/india.csv")
            print(data)
            temp = int(input("Enter player index to update : "))
            p_name = input("Enter name to replace : ")
            p_role = input("Enter player role : ")
            data.at[temp, 'Player_Name'] = p_name
            data.at[temp, 'Player_Role'] = p_role
            data.to_csv("files/groupa/srilanka.csv", index=False)
            print(data)
        elif(o == 3):
            data = pd.read_csv("files/groupa/westindies.csv")
            print(data)
            temp = int(input("Enter player index to update : "))
            p_name = input("Enter name to replace : ")
            p_role = input("Enter player role : ")
            data.at[temp, 'Player_Name'] = p_name
            data.at[temp, 'Player_Role'] = p_role
            data.to_csv("files/groupa/westindies.csv", index=False)
            print(data)

        elif (o == 4):
            data = pd.read_csv("files/groupa/bangladesh.csv")
            print(data)
            temp = int(input("Enter player index to update : "))
            p_name = input("Enter name to replace : ")
            p_role = input("Enter player role : ")
            data.at[temp, 'Player_Name'] = p_name
            data.at[temp, 'Player_Role'] = p_role
            data.to_csv("files/groupa/bangladesh.csv", index=False)
            print(data)
    elif (group == 2):
        print("Please select a team;\n1.Australia\n2.England\n3.Pakistan\n4.SouthAfrica")

        o = int(input("Enter a team number : "))
        if (o == 1):
            data = pd.read_csv("files/groupb/australia.csv")
            print(data)
            temp = int(input("Enter player index to update : "))
            p_name = input("Enter name to replace : ")
            p_role = input("Enter player role : ")
            data.at[temp, 'Player_Name'] = p_name
            data.at[temp, 'Player_Role'] = p_role
            data.to_csv("files/groupb/australia.csv", index=False)
            print(data)
        if (o == 2):
            data = pd.read_csv("files/groupb/england.csv")
            print(data)
            temp = int(input("Enter player index to update : "))
            p_name = input("Enter name to replace : ")
            p_role = input("Enter player role : ")
            data.at[temp, 'Player_Name'] = p_name
            data.at[temp, 'Player_Role'] = p_role
            data.to_csv("files/groupb/england.csv", index=False)
            print(data)

        if (o == 3):
            data = pd.read_csv("files/groupb/pakistan.csv")
            print(data)
            temp = int(input("Enter player index to update : "))
            p_name = input("Enter name to replace : ")
            p_role = input("Enter player role : ")
            data.at[temp, 'Player_Name'] = p_name
            data.at[temp, 'Player_Role'] = p_role
            data.to_csv("files/groupb/pakistan.csv", index=False)
            print(data)

    c = input("Do you want to continue updating. (yes or no) : ").lower()
    if(c == "yes"):
        updateTeams()
    else:
        main()


def main():
    print("Menu\n1.View Teams\n2.View team profiles\n3.Update team profiles\n4.Start the tournament\n5.View Results")
    data = None
    try:
        option = int(input("Enter option number : "))

        if(option == 1):
            print("Select group;\n1.Group A\n2.Group B")
            group = int(input("Enter group number : "))
            if(group == 1):
                print("Srilanka\nIndia\nWestIndies\nBangladesh")
            elif(group == 2):
                print("Australia\nPakistan\nEngland\nSouthAfrica")
            else:
                print("invalid group number")

        elif(option == 2):
            print("Select group;\n1.Group A\n2.Group B")
            group = int(input("Enter group number : "))
            if(group == 1):
                print(
                    "Please select a team;\n1.Srilanka\n2.India\n3.WestIndies\n4.Bangladesh")

                o = int(input("Enter a team number : "))
                if(o == 1):
                    data = pd.read_csv("files/groupa/srilanka.csv")
                    print(data)
                elif(o == 2):
                    data = pd.read_csv("files/groupa/india.csv")
                    print(data)
                elif(o == 3):
                    data = pd.read_csv("files/groupa/westindies.csv")
                    print(data)
                elif(o == 4):
                    data = pd.read_csv("files/groupa/bangladesh.csv")
                    print(data)
            elif(group == 2):
                print(
                    "Please select a team;\n1.Australia\n2.Pakistan\n3.England\n4.SouthAfrica")

                o = int(input("Enter a team number : "))
                if(o == 1):
                    data = pd.read_csv("files/groupb/australia.csv")
                    print(data)
                elif(o == 2):
                    data = pd.read_csv("files/groupb/pakistan.csv")
                    print(data)
                elif (o == 3):
                    data = pd.read_csv("files/groupb/england.csv")
                    print(data)
                elif (o == 4):
                    data = pd.read_csv("files/groupb/southafrica.csv")
                    print(data)

            else:
                print("invalid group number")

        elif(option == 3):
            updateTeams()

        elif(option == 4):
            try:
                match()
            except IndexError:
                match()
            print("\n")
            main()
        elif(option == 5):
            data = pd.read_csv("standings.csv")
            print(data)

    except ValueError:
        print("Invalid input")
        main()


main()
