teams = {
    "Team1": 45,
    "Team2": 42,
    "Team3": 39,
    "Team4": 37,
    "Team5": 35,
    "Team6": 32,
    "Team7": 30,
    "Team8": 28,
    "Team9": 25
}

new_team_name = "NewTeam"
new_team_points = 36

if new_team_name in teams:
    print(f"Команда з назвою '{new_team_name}' вже існує!")
else:
    teams[new_team_name] = new_team_points

    teams_sorted = sorted(teams.items(), key=lambda x: x[1], reverse=True)

    new_team_place = [team[0] for team in teams_sorted].index(new_team_name) + 1

    print(f"Нова команда '{new_team_name}' зайняла {new_team_place}-е місце.")

    teams_below = [team[0] for team in teams_sorted if team[1] < new_team_points]

    print(f"Команди, які набрали менше очок: {', '.join(teams_below)}.")
