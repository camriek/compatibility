# Camrie Kubota
# DataHouse Take Home Project 

def func(var1, var2, var3, var4, max): 
    var1 = (var1/max)
    var2 = (var2/max)
    var3 = (var3/max)
    var4 = (var4/max)
    returnValue = (var1 + var2 + var3 + var4)/4 
    return returnValue

prev_max = 30
max = 40

eddie_lead = 6
eddie_creat = 6
eddie_learn = 3
eddie_work = 7

will_lead = 3
will_creat = 6
will_learn = 8
will_work = 2

mike_lead = 5
mike_creat = 7
mike_learn = 2
mike_work = 4

team_lead = eddie_lead + will_lead + mike_lead
team_creat = eddie_creat + will_creat + mike_creat
team_learn = eddie_learn + will_learn + mike_learn
team_work = eddie_work + will_work + mike_work

team_score = func(team_lead, team_creat, team_learn, team_work, prev_max)
print("Team:", team_score)

jon_lead = team_lead + 3
jon_creat = team_creat + 6
jon_learn = team_learn + 2
jon_work = team_work + 9

jon_score = func(jon_lead, jon_creat, jon_learn, jon_work, max)
print("Jon:",jon_score)

jane_lead = team_lead + 5
jane_creat = team_creat + 6
jane_learn = team_learn + 3
jane_work = team_work + 2

jane_score = func(jane_lead, jane_creat, jane_learn, jane_work, max)
print("Jane:", jane_score)

joe_lead = team_lead + 8
joe_creat = team_creat + 5
joe_learn = team_learn + 3
joe_work = team_work + 6

joe_score = func(joe_lead, joe_creat, joe_learn, joe_work, max)
print("Joe:",joe_score)


