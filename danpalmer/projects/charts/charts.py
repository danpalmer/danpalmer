import datetime

from django_google_charts import charts


class StepsChart(charts.Chart):

    columns = (
        ('datetime', "Date"),
        ('number', "Steps"),
    )

    options = {
        'title': "Steps per Day",
        'height': 250,
        'legend': {'position': 'none'},
    }

    def get_data(self):
        return (
            (datetime.datetime(2016, 1, 1), 6000),
            (datetime.datetime(2016, 1, 2), 8000),
            (datetime.datetime(2016, 1, 3), 7000),
            (datetime.datetime(2016, 1, 4), 7500),
            (datetime.datetime(2016, 1, 5), 9000),
            (datetime.datetime(2016, 1, 6), 10000),
            (datetime.datetime(2016, 1, 7), 12000),
        )
