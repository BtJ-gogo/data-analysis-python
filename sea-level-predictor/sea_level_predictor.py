import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    estimate_year_range = pd.DataFrame(range(1880,2051))
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line = result[0] * estimate_year_range + result[1]
    ax.plot(estimate_year_range, line, color='red')
    
    # Create second line of best fit
    estimate_year_range = pd.DataFrame(range(2000,2051))
    result = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    line = result[0] * estimate_year_range + result[1]
    ax.plot(estimate_year_range, line, color='green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == '__main__':
    draw_plot()