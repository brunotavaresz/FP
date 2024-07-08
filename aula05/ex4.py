teams = ["SCP", "FCP", "SLB"]
def allMatches(teams):
   assert len(teams) >= 2
   allMatches = []
   for team1 in teams:
      for team2 in teams:
         if team1 != team2:
            allMatches.append((team1, team2))
    return allMatches

print(allMatches(teams))

