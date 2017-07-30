import pandas as pd
import pandasql

from sympy import init_printing
init_printing()

filename="../data/nyc_subway.csv"

def num_rainy_days(filename):

    weather_data = pd.read_csv(filename)
    #weather_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = """
    SELECT COUNT(DISTINCT DATEn) as 'count(*)'
    FROM weather_data 
    WHERE cast(rain as integer) = 1
    """
    rainy_days = pandasql.sqldf(q, locals())
    return rainy_days


print num_rainy_days(filename)