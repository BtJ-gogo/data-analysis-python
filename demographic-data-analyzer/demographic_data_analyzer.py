import numpy as np
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    #print(df.head())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['race'].count()
    #print(type(race_count))

    # What is the average age of men?
    average_age_men = df['age'][df['sex'] == 'Male'].mean()
    average_age_men = round(average_age_men, 1)
    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df['education'][df['education'] == 'Bachelors'].size / df['education'].size * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['salary'][(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df['salary'][~(df['education'] == 'Bachelors') & ~(df['education'] == 'Masters') & ~(df['education'] == 'Doctorate')]
    #print(higher_education['education'].drop_duplicates()) #['education','salary'] 'salary'
    #print(lower_education)
    #print(df['education'].size, higher_education.size + lower_education.size)

    # percentage with salary >50K
    higher_education_rich = higher_education[higher_education == '>50K'].size / higher_education.size * 100
    higher_education_rich = round(higher_education_rich, 1)
    #print(higher_education[higher_education == '>50K'].drop_duplicates())
    lower_education_rich = lower_education[lower_education == '>50K'].size / lower_education.size * 100
    lower_education_rich = round(lower_education_rich, 1)
    #print(lower_education.drop_duplicates())
    #print(lower_education[lower_education == '>50K'].drop_duplicates())

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    #print(df[df['hours-per-week'] < df['hours-per-week'].min()])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['salary'][df['hours-per-week'] == min_work_hours]
    #print(num_min_workers) #['hours-per-week','salary']

    rich_percentage = num_min_workers[num_min_workers == '>50K'].size / num_min_workers.size * 100
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_percentage = (df[['native-country', 'salary']][df['salary'] == '>50K'].groupby('native-country').count() / df[['native-country', 'salary']].groupby('native-country').count() * 100).max()[0]
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)
    #df[df['salary'] == '>50K']???
    #df[['native-country', 'salary']][df['salary'] == '>50K'].groupby('native-country').count() / df[['native-country', 'salary']].groupby('native-country').count() * 100
    #print(highest_earning_country_percentage)
    highest_earning_country = (df[['native-country', 'salary']][df['salary'] == '>50K'].groupby('native-country').count() / df[['native-country', 'salary']].groupby('native-country').count() * 100).idxmax()[0]
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].mode()[0]
    #.sort_values('native-country', ascending=False)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
