# Author: Dimgba Martha O
# @martha_samuel_
# 20   This code matches a 4 team basket ball team match making sure a team doesnt play against itself and home teams play with away teams only
teams = ['Dragons', 'Wolves', 'Pandas', 'Falcons']
for home_teams in teams :
    for away_teams in teams:
        if home_teams != away_teams:
            print(home_teams + ' vs ' + away_teams)

