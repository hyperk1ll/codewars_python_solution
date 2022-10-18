# UEFA EURO 2016

def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return "At match %s - %s, %s won!" % (teams[0], teams[1], teams[0])
    elif scores[0] < scores[1]:
        return "At match %s - %s, %s won!" % (teams[0], teams[1], teams[1])
    else:
        return "At match %s - %s, teams played draw." % (teams[0], teams[1])