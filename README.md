# Compatibility Predictor
Application that takes an input: an array of applicants and an array of team members, and produces an output: an array of applicants with their respective compatibility score.

## Instructions

Read in file and import json.
```bash
import json
```

Assign team scores to variables.
```bash
#example
eddie_lead = 6
eddie_creat = 6
eddie_learn = 3
eddie_work = 7
```

Add applicant scores to team scores and assign to variables.
```bash
#example
jon_lead = team_lead + 3
jon_creat = team_creat + 6
jon_learn = team_learn + 2
jon_work = team_work + 9
```

## Explanation
Code takes team data and applicant data to yield applicant compatibility scores. Team members and applicants are measured against DataHouse Principles of Success.

To calculate compatibility score, we first calculate the team's overall score. This is done by setting an arbitrary maximum of 30 and calculating the average of the team's attribute scores.

```bash
Team Member Name: Eddie
Leadership: 6
Creativity: 6
Learning: 3
Working Hard: 7

Team Member Name: Will
Leadership: 3
Creativity: 6
Learning: 8
Working Hard: 2

Team Member Name: Mike
Leadership: 5
Creativity: 7
Learning: 2
Working Hard: 4

Team's total leadership score: 6 + 3 + 5 = 14/30 = 0.46667
Team's total creativity score: 6 + 6 + 7 = 19/30 = 0.63333
Team's total learning score: 3 + 8 + 2 = 13/30 = 0.43333
Team's total working hard score: 7 + 2 + 4 = 13/30 = 0.43333

Team score = 0.46667 + 0.63333 + 0.43333 + 0.43333 = 0.49167

```

Then, calculate each applicant's score by adding the applicant's points to the team's total, taking the average of the attribute scores. The maximum now becomes 40.
```bash
Applicant Name: Jon
Leadership: Team leadership score + 3 = 17/40 = 0.425
Creativity: Team creativity score + 6 = 25/40 = 0.625
Learning: Team learning score + 2 = 15/40 = 0.375
Working Hard: Team working hard score + 9 = 22/40 = 0.55

Jon's score = 0.425 + 0.625 + 0.375 + 0.55 = 0.49375
```

This is repeated for the other two applicants. The final output is:
```bash
Team: 0.4916666666666667
Jon: 0.49375
Jane: 0.46875
Joe: 0.50625
```
This means that Joe is the most "compatible" with the team because he would increase the team's overall average score. Joe is more compatible than Jon and Jane.
