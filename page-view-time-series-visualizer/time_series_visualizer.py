import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#print(sns.__version__)
#print(np.__version__)

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
#print(df)

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))]
df.reset_index(inplace=True)
del df['index']
#print(df)
#print(type(df['date'].iloc[1]))


def draw_line_plot():
    # Draw line plot
    plt.rcParams['font.size'] = 20
    fig, ax = plt.subplots(figsize=(32,10))
    ax.plot(df['date'], df['value'], color='r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    years = ['2016', '2017', '2018', '2019']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = [d.year for d in df_bar.date] 
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar = df_bar.groupby(['month', 'year']).mean(numeric_only=True).reset_index()
    #print(df_bar)
    df_test = pd.DataFrame(index = years ,columns = months)
    df_test.columns.name = 'Months'
    
    for year in [int(i) for i in years]:
        for month in months:
            insert_data = df_bar[(df_bar['year'] == year) & (df_bar['month'] == month)]['value']
            #print(insert_data)
            if not insert_data.empty:
                df_test.loc[str(year), month] = insert_data.item()
    #print(df_test)
    #df_bar = df_bar.groupby(['year','month']).mean()
    #print(df_bar[(df_bar['year'] == 2019) & (df_bar['month'] == 'January')]['value'])

    # Draw bar plot
    plt.rcParams['font.size'] = 20
    fig, ax = plt.subplots(figsize=(15.14,13.3))
    df_test.plot.bar(ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box = df.copy()
    #print(df_box)
    df_box.reset_index(inplace=True)
    del df_box['index']
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = [str(d.year) for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    #print(df_box)
    #print(type(df_box['date'].loc[0]))
    #print(df_box.info())

    # Draw box plots (using Seaborn)
    #fig, ax = plt.subplots()
    plt.rcParams['font.size'] = 20
    fig, ax = plt.subplots(1,2,figsize=(28.8,10.8))
    #print(df_box[['year','value']])
    sns.boxplot(data=df_box, x='year', y='value', hue='year', ax=ax[0])
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    
    df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)
    df_box.sort_values(by='month', inplace=True)
    #print(df_box)
    sns.boxplot(data=df_box, x='month', y='value', hue='month', ax=ax[1])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

if __name__ == '__main__':
    #pass
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()