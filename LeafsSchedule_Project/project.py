import json
import requests

def main():
    team = input("Leafs vs ?: ")
    year = input("Which season? ")
    season_start,season_end = get_year(year)
    leafs_season = get_schedule(season_start,season_end)
    get_scorers(leafs_season, team)


def get_schedule(start_year, end_year):

    team_schedule = requests.get(
    f"https://statsapi.web.nhl.com/api/v1/schedule?teamId=10&startDate={start_year}-10-07&endDate={end_year}-04-13" #regular season for the leafs
    )

    output = team_schedule.json()
    season = []

    #creates a list of dicts for every game the leafs played in 2022 season, specifies the team, score, outcome and gameID
    dates = output["dates"]
    for date_info in dates:
        game_info = date_info["games"]
        for game in game_info:
            if game["gameType"] == "R":

                if game['teams']['away']['team']['name'] == "Toronto Maple Leafs":
                    if game['teams']['away']['score'] > game['teams']['home']['score']:
                        outcome = "W"
                    else:
                        outcome = "L"

                    season.append({"Team": game['teams']['home']['team']['name'], "Score": f"{game['teams']['away']['score']}-{game['teams']['home']['score']}", "Outcome":{outcome}, "Game ID":{game["gamePk"]}})

                else:
                    if game['teams']['away']['score'] > game['teams']['home']['score']:
                        outcome = "L"
                    else:
                        outcome = "W"
                    season.append({"Team": game['teams']['away']['team']['name'], "Score": f"{game['teams']['home']['score']}-{game['teams']['away']['score']}", "Outcome":{outcome}, "Game ID":{game["gamePk"]}})
    return season

def get_scorers(season_list, team):
    x=1
    for entry in season_list:
        outcome = (str(entry['Outcome']).strip("\'{}"))
        if entry["Team"] == team:
            print("\n")
            print(f"Game {x}: Leafs vs {team} - Score: {entry['Score']} {outcome}")
            gameID = str(entry["Game ID"])
            game_request = requests.get(f"https://statsapi.web.nhl.com/api/v1/game/{gameID.strip('{}')}/boxscore").json()

            away_player = game_request["teams"]["away"]["players"]
            away_team = game_request['teams']['away']['team']['name']

            if away_team == "Toronto Maple Leafs":
                print(f"Toronto Maple Leafs Scorers:")
            else:
                print(f"{away_team} Scorers:")

            for player_ID, person in away_player.items():
                if "skaterStats" in person["stats"] and person["stats"]["skaterStats"]["goals"] > 0:

                    if away_team == "Toronto Maple Leafs":
                        print(f"{person['person']['fullName']} {person['stats']['skaterStats']['goals']}")

                    else:
                        print(f"{person['person']['fullName']} {person['stats']['skaterStats']['goals']}")
                else:
                    continue

            home_player = game_request["teams"]["home"]["players"]
            home_team = game_request['teams']['home']['team']['name']

            if home_team == "Toronto Maple Leafs":
                print(f"Toronto Maple Leafs Scorers:")
            else:
                print(f"{home_team} Scorers:")

            for player_ID, person in home_player.items():
                if "skaterStats" in person["stats"] and person["stats"]["skaterStats"]["goals"]>0:

                    if home_team == "Toronto Maple Leafs":
                        print(f"{person['person']['fullName']} {person['stats']['skaterStats']['goals']}")

                    else:
                        print(f"{person['person']['fullName']} {person['stats']['skaterStats']['goals']}")
                else:
                    continue
            x+=1

def get_year(x):
    season_start,season_end = x.split("-")
    return season_start,season_end

if __name__ == "__main__":
    main()