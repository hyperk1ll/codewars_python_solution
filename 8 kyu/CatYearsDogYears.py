# Cat years, Dog years

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years, human_years * 15, human_years * 15]
    elif human_years == 2:
        return[human_years, 15 + 9, 15 + 9]
    else:
        return [human_years, 15 + 9 + ((human_years - 2) * 4), 15 + 9 + ((human_years - 2) * 5)]
