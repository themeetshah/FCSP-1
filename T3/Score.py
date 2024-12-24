# Find the average of the points scored over all the games in the file.
# Pick your favorite team and scan through the file to determine how many games they won and how many games they lost.
# Find the team(s) that lost by 30 or more points the most times
# Find all the teams that averaged at least 90 points a game.

with open("D:\A1_MeetS\Python\T3\scores.txt") as f:
    fav=input("Fav Team: ")
    matches = f.readlines()
    team_scores={}
    matches_played={}
    wins={}
    lost={}
    lost_by_30={}
    avg_scores_90={}
    avg=0
    for i in matches:
        i = i.strip()
        if i:
            splitted = i.split()
            team1, team2, score1, score2 = splitted[1], splitted[3], int(splitted[2]), int(splitted[4])
            avg+=score1+score2

            matches_played[team1]=matches_played.get(team1,0)+1
            team_scores[team1]=team_scores.get(team1,0)+score1

            matches_played[team2]=matches_played.get(team1,0)+1
            team_scores[team2]=team_scores.get(team1,0)+score2
                
            if score1>score2:
                wins[team1]=wins.get(team1,0)+1
                lost[team2]=lost.get(team2,0)+1
                if score1-score2>=30:
                    lost_by_30[team2]=lost_by_30.get(team2,0)+1
            elif score2>score1:
                wins[team2]=wins.get(team2,0)+1
                lost[team1]=lost.get(team1,0)+1
                if score2-score1>=30:
                    lost_by_30[team1]=lost_by_30.get(team1,0)+1

    for i in team_scores:
        avg_team = team_scores[i]/matches_played[i]
        if avg_team>=90:
            avg_scores_90[i] = avg_team
                
    print(avg/len(matches))
    
    if matches_played.get(team1,0)==0:
        print("No such team")
    else:
        print(f"Wins: {wins.get(fav,0)}, Loss: {lost.get(fav,0)}, Played: {matches_played.get(fav,0)}")

    max_value = max(lost_by_30.values())
    max_loss_by_30 = [f"{key} : {value}" for key, value in lost_by_30.items() if value == max_value]
    print(max_loss_by_30)

    print(avg_scores_90)