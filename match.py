import random
import pandas as pd
import glob


def bowl():

    randstate = random.randint(0, 100)

    if(randstate < 60):
        runs = random.randint(0, 100)

        if(runs < 20):
            return("6")
        elif(runs < 40):
            return("4")
        elif(runs < 70):
            return("1")
        elif(runs < 90):
            return("2")
        else:
            return("3")

    elif(randstate < 70):
        out = random.randint(0, 100)

        if(out < 20):
            return("caught")
        elif(out < 40):
            return("run out")
        elif(out < 60):
            return("stupmed")
        elif(out < 80):
            return("lbw")
        else:
            return("bowled")
    else:
        runs = random.randint(0, 100)

        if(runs < 20):
            return("no ball")
        elif(runs < 40):
            return("bye")
        elif(runs < 70):
            return("wide")
        elif(runs < 90):
            return("dead")
        else:
            return("leg bye")


def T20(batsmans, bowlers):
    score = 0
    opening = batsmans[0:2]
    playing = True
    batting_count = 2
    current_player = opening[0]
    current_bowler = bowlers[0]
    current_pair = opening
    player_stats = {}
    bowler_stats = {}
    wickets_by = {}
    # add players to the dictionery
    for bmans in batsmans:
        # [score, no of bowls,wicket by,type]
        player_stats[bmans] = [0, 0, "", "Not Out"]

    # add all the bowlers to the dictionery
    for bowls in bowlers:
        # [no of overs bowled,scores given, wickets]
        bowler_stats[bowls] = [0, 0, 0]
    ball_count = 0
    over_count = 0
    while(playing):
        if(batting_count < 10 and over_count < 20):
            while(ball_count < 6):
                # count balls given for a single player
                player_stats[current_player][1] += 1
                ball_result = bowl()
                if(ball_result in ["stumped", "caught", "lbw", "run out"]):
                    # print("{} is out by {}".format(
                    # current_player, current_bowler))
                    current_pair.remove(current_player)
                    current_player = batsmans[batting_count]
                    current_pair.append(current_player)
                    bowler_stats[current_bowler][2] += 1
                    player_stats[current_player][2] = current_bowler
                    player_stats[current_player][3] = ball_result
                    batting_count += 1

                elif(ball_result in ["no ball", "wide"]):
                    ball_count -= 1
                    score += 1
                    player_stats[current_player][0] += 1
                    bowler_stats[current_bowler][1] += 1
                else:
                    # change players considering the number of runs
                    if(ball_result in ["1", "3"]):

                        if(current_pair.index(current_player) == 1):
                            current_player = current_pair[0]
                        else:
                            current_player = current_pair[1]

                    try:
                        score += int(ball_result)
                        player_stats[current_player][0] += int(ball_result)
                        bowler_stats[current_bowler][1] += int(ball_result)
                    except:
                        pass

                ball_count += 1
            over_count += 1
            ball_count = 0
            bowler_stats[current_bowler][0] += 1
            # change the bowler
            if(bowlers.index(current_bowler) + 1 < len(bowlers)):
                current_bowler = bowlers[bowlers.index(current_bowler) + 1]
            else:
                current_bowler = bowlers[0]
        else:
            playing = False

    return [over_count, batting_count, player_stats, bowler_stats, score]


def inning(group, teams):

    team1 = pd.read_csv("files/group{}/{}.csv".format(group, teams[0]))
    team2 = pd.read_csv("files/group{}/{}.csv".format(group, teams[1]))

    bowlers = []
    for player in range(len(team2["Player_Role"])):
        if(team2["Player_Role"][player] in ["Bowler", "All-Rounder"]):
            bowlers.append(team2["Player_Name"][player])

    batsmans = []
    # select allrounders and batsmans first
    for player in range(len(team1["Player_Role"])):
        if(team1["Player_Role"][player] in ["Batsman", "All-Rounder"]):
            batsmans.append(team1["Player_Name"][player])

    for player in range(len(team1["Player_Role"])):
        if(team1["Player_Role"][player] in ["Bowler"]):
            batsmans.append(team1["Player_Name"][player])

    try:
        return T20(batsmans, bowlers)
    except:
        return T20(batsmans, bowlers)


def bestPlayer(batsman, bowler):
    # get bats mans and bowlers from both teams and find whose the best
    # get best from team1
    bestbatsman = [0, ""]
    bestbowler = [0, ""]
    for player in batsman[0].keys():
        if(batsman[0][player][0] > bestbatsman[0]):
            bestbatsman[0] = batsman[0][player][0]
            bestbatsman[1] = player
    # select from team2
    for player in batsman[1].keys():
        if(batsman[1][player][0] > bestbatsman[0]):
            bestbatsman[0] = batsman[1][player][0]
            bestbatsman[1] = player

    for player in bowler[0].keys():
        if(bowler[0][player][0] > bestbowler[0]):
            bestbowler[0] = bowler[0][player][0]
            bestbowler[1] = player
    # select from team2
    for player in bowler[1].keys():
        if(bowler[1][player][0] > bestbowler[0]):
            bestbowler[0] = bowler[1][player][0]
            bestbowler[1] = player

    with open("bestplayers.txt", "a") as file:
        string = "---------\nBest batsman : {} , Scored : {}\nBest bowler : {} , Wickets : {}\n".format(
            bestbatsman[1], bestbatsman[0], bestbowler[1], bestbowler[0])
        file.write(string)

    with open("stats", "a") as f:
        string = "{},{}|{},{}\n".format(
            bestbatsman[1], bestbatsman[0], bestbowler[1], bestbowler[0])
        f.write(string)


def match():
    # clear results
    file = open("results-groupa.txt", "w")
    file.write("")
    file.close()

    '''
    # workingon , but produce errors running in windows
    groupa = [x.split("/")[3].split(".")[0]
              for x in glob.glob("./files/groupa/*.csv")]
    groupb = [x.split("/")[3].split(".")[0]
              for x in glob.glob("./files/groupb/*.csv")]

    '''
    groupa = ["srilanka", "india", "bangladesh", "westindies"]
    groupb = ["australia", "england", "pakistan", "southafrica"]

    c = 1
    # play group A
    for i in groupa:
        for j in range(c, len(groupa)):
            teams = [i, groupa[j]]
            teamtotoss = random.randint(0, 1)
            teamtocall = 0
            if(teamtotoss == 1):
                teamtocall = 0
            else:
                teamtocall = 1
            toss = random.randint(0, 1)
            call = random.randint(0, 1)
            battingorbowling = random.randint(0, 1)
            firstbatting = ""
            firstbowling = ""
            firstbatScore = 0
            secondbatScore = 0
            if(toss == call):
                # calling team won the toss
                if(battingorbowling == 1):
                    firstbatting = teams[teamtocall]
                    firstbowling = teams[teamtotoss]

                else:
                    firstbatting = teams[teamtotoss]
                    firstbowling = teams[teamtocall]

            else:
                # calling team loose the toss
                if(battingorbowling == 1):
                    firstbatting = teams[teamtotoss]
                    firstbowling = teams[teamtocall]

                else:
                    firstbatting = teams[teamtocall]
                    firstbowling = teams[teamtotoss]

            i1 = inning("a", [firstbatting, firstbowling])
            i2 = inning("a", [firstbowling, firstbatting])

            bestPlayer([i1[2], i2[2]], [i1[3], i2[3]])

            string = "---------\n{} vs {}\n{} choose to bat first\n".format(
                firstbatting, firstbowling, firstbatting)

            string += "\nfirst inning\n"

            for player in i1[2].keys():
                arr = i1[2][player]
                # <player name> <#> runs/(<#>) {wicket type} - {wicket by}
                string += "{} {} runs/({}) {} - {}\n".format(player,
                                                             arr[0], arr[1], arr[3], arr[2])

            string += "\nOvers : {}\nWickets : {}\nScore : {}\n".format(
                i1[0], i1[1], i1[4])

            string += "\n\nsecond inning\n"

            for player in i2[2].keys():
                arr = i2[2][player]
                # <player name> <#> runs/(<#>) {wicket type} - {wicket by}
                string += "{} {} runs/({}) {} - {}\n".format(player,
                                                             arr[0], arr[1], arr[3], arr[2])

            string += "\nOvers : {}\nWickets : {}\nScore : {}\n".format(
                i2[0], i2[1], i2[4])

            string += "\n\n"

            firstbatScore = i1[4]
            secondbatScore = i2[4]
            wonby = ""
            lostby = ""
            if(firstbatScore > secondbatScore):
                string += "{} won the match\n".format(firstbatting)
                wonby = firstbatting
                lostby = firstbowling

            elif(secondbatScore > firstbatScore):
                string += "{} won the match\n".format(firstbowling)
                wonby = firstbowling
                lostby = firstbatting

            else:
                string += "Match ended as draw\n"
                wonby = "draw"

            # record won or lost
            data = pd.read_csv("standings.csv")
            values = data.values
            if(wonby != "draw"):
                for k in range(8):
                    if(values[k][0] == wonby):
                        data.at[k, "played"] = values[k][1] + 1
                        data.at[k, "won"] = values[k][2] + 1
                    elif(values[k][0] == lostby):
                        data.at[k, "played"] = values[k][1] + 1
                        data.at[k, "lost"] = values[k][3] + 1
            else:
                # increment both the teams if draw
                for l in range(8):
                    if(values[l][0] == firstbatting):
                        data.at[l, "played"] = values[l][1] + 1
                        data.at[l, "draw"] = values[l][4] + 1
                    if(values[l][0] == firstbowling):
                        data.at[l, "played"] = values[l][1] + 1
                        data.at[l, "draw"] = values[l][4] + 1
            data.to_csv("standings.csv", index=False)

            with open("results-groupa.txt", "a") as file:
                file.write(string)

        c += 1

    c = 1
    # play group B
    for i in groupb:
        for j in range(c, len(groupb)):
            teams = [i, groupb[j]]
            teamtotoss = random.randint(0, 1)
            teamtocall = 0
            if(teamtotoss == 1):
                teamtocall = 0
            else:
                teamtocall = 1
            toss = random.randint(0, 1)
            call = random.randint(0, 1)
            battingorbowling = random.randint(0, 1)
            firstbatting = ""
            firstbowling = ""
            firstbatScore = 0
            secondbatScore = 0
            if(toss == call):
                # calling team won the toss
                if(battingorbowling == 1):
                    firstbatting = teams[teamtocall]
                    firstbowling = teams[teamtotoss]

                else:
                    firstbatting = teams[teamtotoss]
                    firstbowling = teams[teamtocall]

            else:
                # calling team loose the toss
                if(battingorbowling == 1):
                    firstbatting = teams[teamtotoss]
                    firstbowling = teams[teamtocall]

                else:
                    firstbatting = teams[teamtocall]
                    firstbowling = teams[teamtotoss]

            i1 = inning("b", [firstbatting, firstbowling])
            i2 = inning("b", [firstbowling, firstbatting])

            bestPlayer([i1[2], i2[2]], [i1[3], i2[3]])

            string = "---------\n{} vs {}\n{} choose to bat first\n".format(
                firstbatting, firstbowling, firstbatting)

            string += "\nfirst inning\n"

            for player in i1[2].keys():
                arr = i1[2][player]
                # <player name> <#> runs/(<#>) {wicket type} - {wicket by}
                string += "{} {} runs/({}) {} - {}\n".format(player,
                                                             arr[0], arr[1], arr[3], arr[2])

            string += "\nOvers : {}\nWickets : {}\nScore : {}\n".format(
                i1[0], i1[1], i1[4])

            string += "\n\nsecond inning\n"

            for player in i2[2].keys():
                arr = i2[2][player]
                # <player name> <#> runs/(<#>) {wicket type} - {wicket by}
                string += "{} {} runs/({}) {} - {}\n".format(player,
                                                             arr[0], arr[1], arr[3], arr[2])

            string += "\nOvers : {}\nWickets : {}\nScore : {}\n".format(
                i2[0], i2[1], i2[4])

            string += "\n\n"

            firstbatScore = i1[4]
            secondbatScore = i2[4]
            wonby = ""
            lostby = ""
            if(firstbatScore > secondbatScore):
                string += "{} won the match\n".format(firstbatting)
                wonby = firstbatting
                lostby = firstbowling

            elif(secondbatScore > firstbatScore):
                string += "{} won the match\n".format(firstbowling)
                wonby = firstbowling
                lostby = firstbatting

            else:
                string += "Match ended as draw\n"
                wonby = "draw"

            # record won or lost
            data = pd.read_csv("standings.csv")
            values = data.values
            if(wonby != "draw"):
                for k in range(8):
                    if(values[k][0] == wonby):
                        data.at[k, "played"] = values[k][1] + 1
                        data.at[k, "won"] = values[k][2] + 1
                    elif(values[k][0] == lostby):
                        data.at[k, "played"] = values[k][1] + 1
                        data.at[k, "lost"] = values[k][3] + 1
            else:
                # increment both the teams if draw
                for l in range(8):
                    if(values[l][0] == firstbatting):
                        data.at[l, "played"] = values[l][1] + 1
                        data.at[l, "draw"] = values[l][4] + 1
                    if(values[l][0] == firstbowling):
                        data.at[l, "played"] = values[l][1] + 1
                        data.at[l, "draw"] = values[l][4] + 1
            data.to_csv("standings.csv", index=False)

            with open("results-groupb.txt", "a") as file:
                file.write(string)

        c += 1

    bestbats = []
    bestbowls = []

    maxBestbat = [0, ""]
    maxBestbowl = [0, ""]

    file = open("stats", "r")
    line = file.readline()
    while(line != ""):
        temp = line.split("|")
        bestbats.append(temp[0].split(","))
        bestbowls.append(temp[1].split(","))
        line = file.readline()

    for p in bestbats:
        if(maxBestbat[0] < int(p[1])):
            maxBestbat = [int(p[1]), p[0]]

    for p in bestbowls:
        if(maxBestbowl[0] < int(p[1])):
            maxBestbowl = [int(p[1]), p[0]]

    with open("bestplayers.txt", "a") as file:
        string = "\n\n###########\nBest batsman of the tournament : {}, Scored : {}\nBest Bowler of the tournament : {}, Wickets : {}\n#########".format(
            maxBestbat[1], maxBestbat[0], maxBestbowl[1], maxBestbowl[0])
        file.write(string)
