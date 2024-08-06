# using searborn for data visualization and clean GUI
# Pie chart and histogram

# csv format: activity_name,date,duration
# sample: bruh,2024-01-01,100.9

import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def inter_convert(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{h:.0f} hours, {m:.0f} minutes, {s:.0f} seconds"


def same_week(dateString):
    d1 = datetime.datetime.strptime(dateString, "%Y-%m-%d")
    d2 = datetime.datetime.today()
    return d1.isocalendar()[1] == d2.isocalendar()[1]


def same_month(dateString):
    d1 = datetime.datetime.strptime(dateString, "%Y-%m-%d")
    d2 = datetime.datetime.today()
    return d1.month == d2.month


def get_summary(activity_name, time_period, file_name):
    current_day = datetime.date.today()
    dataframe = pd.read_csv(file_name)

    if time_period == "daily":
        criterion1 = dataframe["activity_name"].map(lambda x: x == activity_name)
        criterion2 = dataframe["date"].map(
            lambda x: x == current_day.strftime("%Y-%m-%d")
        )
        total = dataframe[criterion1 & criterion2]["duration"].sum()
        print(total)
        print(f"Daily: {inter_convert(total)}")
        return total

    elif time_period == "weekly":
        criterion1 = dataframe["activity_name"].map(lambda x: x == activity_name)
        criterion2 = dataframe["date"].map(lambda x: same_week(x))
        total = dataframe[criterion1 & criterion2]["duration"].sum()
        print(total)
        print(f"Weekly: {inter_convert(total)}")
        return total

    elif time_period == "monthly":
        criterion1 = dataframe["activity_name"].map(lambda x: x == activity_name)
        criterion2 = dataframe["date"].map(lambda x: same_month(x))
        total = dataframe[criterion1 & criterion2]["duration"].sum()
        print(total)
        print(f"Monthly: {inter_convert(total)}")
        return dataframe[criterion1 & criterion2]["duration"].sum()

    elif time_period == "yearly":
        criterion = dataframe["activity_name"].map(lambda x: x == activity_name)
        total = dataframe[criterion]["duration"].sum()
        print(total)
        print(f"Yearly: {inter_convert(total)}")
        return total


def get_advanced(activity_name, time_period, file_name):
    current_day = datetime.date.today()
    dataframe = pd.read_csv(file_name)

    if time_period == "daily":
        criterion1 = dataframe["activity_name"].map(lambda x: x == activity_name)
        criterion2 = dataframe["date"].map(
            lambda x: x == current_day.strftime("%Y-%m-%d")
        )
        total = dataframe[criterion1 & criterion2]["duration"].sum()
        print(total)
        print(f"Daily: {inter_convert(total)}")
        visualization(time_period, dataframe[criterion1 & criterion2]["date"], dataframe[criterion1 & criterion2]["duration"])
        return total

    elif time_period == "weekly":
        criterion1 = dataframe["activity_name"].map(lambda x: x == activity_name)
        criterion2 = dataframe["date"].map(lambda x: same_week(x))
        total = dataframe[criterion1 & criterion2]["duration"].sum()
        print(total)
        print(f"Weekly: {inter_convert(total)}")
        visualization(time_period, dataframe[criterion1 & criterion2]["date"], dataframe[criterion1 & criterion2]["duration"])
        return total

    elif time_period == "monthly":
        criterion1 = dataframe["activity_name"].map(lambda x: x == activity_name)
        criterion2 = dataframe["date"].map(lambda x: same_month(x))
        total = dataframe[criterion1 & criterion2]["duration"].sum()
        print(total)
        print(f"Monthly: {inter_convert(total)}")
        visualization(time_period, dataframe[criterion1 & criterion2]["date"], dataframe[criterion1 & criterion2]["duration"])
        return total

    elif time_period == "yearly":
        criterion = dataframe["activity_name"].map(lambda x: x == activity_name)
        total = dataframe[criterion]["duration"].sum()
        print(total)
        print(f"Yearly: {inter_convert(total)}")
        visualization(time_period, dataframe[criterion1 & criterion2]["date"], dataframe[criterion1 & criterion2]["duration"])
        return total

def visualization(time_period, date_column, duration_column):
    # sns.barplot(x=date_column, y=duration_column)
    # plt.title(f'{time_period} Activity Duration')
    # plt.show()
    sns.set_style("whitegrid")
    bar_plot = sns.barplot(x=date_column, y=duration_column)
    bar_plot.set_title(f'Activity Duration {time_period}')
    bar_plot.set(xlabel='Date', ylabel='Duration')
    script_dir = os.path.dirname(os.path.realpath(__file__)) + '/' + 'my-electron-app'
    plt.savefig(os.path.join(script_dir, "plot.png"))

get_advanced("bruh", "monthly", "activities_2024.csv")