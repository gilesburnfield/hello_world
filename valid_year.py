def valid_year(year):
    if year and year.isdigit:
        year = int(year)
        if year >1900 and year <2010:
            return year


        