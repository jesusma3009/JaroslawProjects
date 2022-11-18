import matplotlib.pyplot as plt
import pandas as pd
import requests

def spainData():
    df = pd.read_csv('https://raw.githubusercontent.com/andrzejmp/some_codes/main/python/tourism/data.csv')

    years = df["YEAR"]
    country = df[" SP"]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.bar(years, country)
    ax.set_title("Data on tourism in Spain by year", fontsize=24)
    ax.set_xlabel('Years', fontsize=16)
    ax.set_ylabel("Number of people", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

