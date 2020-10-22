# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:01:51 2020

@author: Hagar Farouk
"""

import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    validcity = True
    while validcity:
        print('which city you want to analyze?   (chicago, new york city, washington)')
        city = input()
        if city.lower()  in ['chicago', 'new york city', 'washington']:
            validcity = False
    
    

    # TO DO: get user input for month (all, january, february, ... , june)
    validmonth = True
    while validmonth:
        month = input('Which month you want to filter (all, january, february, ... , june) ? \n')
        if month.lower()  in ['all', 'january', 'february', 'march','april','may' ,' june']:
            validmonth = False
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    validday = True
    while validday:
        day = input('Which day of week you want to filter (all, monday, tuesday, ... sunday) ? \n')
        if day.lower()  in ['all', 'monday', 'tuesday', 'wednesday','thursday','friday' ,' saturday','sunday']:
            validday = False


    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month: {}'.format(df['month'].mode()[0]))
    

    # TO DO: display the most common day of week
    print('The most common day of week: {}'.format(df['day_of_week'].mode()[0]))



    # TO DO: display the most common start hour
    print('The most common start hour: {}'.format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: {}'.format(df['Start Station'].mode()[0]))
    


    # TO DO: display most commonly used end station
    print('The most commonly used end station: {}'.format(df['End Station'].mode()[0]))



    # TO DO: display most frequent combination of start station and end station trip
    print('the most frequent combination of start station and end station trip: {}'.format(df.groupby([df['Start Station'],df['End Station']]).size().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('Mean travel time: {}'.format(df['Trip Duration'].mean()))
        
    print('-'*40)
    
    
def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n {}'.format(df['User Type'].value_counts()))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: \n{}'.format(df['User Type'].value_counts()))


    # TO DO: Display counts of gender
    print('Counts of gender:\n {}'.format(df['Gender'].value_counts()))


    # TO DO: Display earliest, most recent, and most common year of birth
    
    print('The earliest year of birth: {}'.format(df['Birth Year'].min()))
    
    print('The most recent year of birth: {}'.format(df['Birth Year'].max()))
    
    print('The most common year of birth: {}'.format(df['Birth Year'].mode()[0]))
           


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city.lower(), month.lower(), day.lower())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city.lower() != 'washington':
            user_stats(df)
        display = 'yes'
        i=1
        while display =='yes':
            display = input('\nWould you like to display 5 more raw data? Enter yes or no.\n')
            if display.lower() == 'no':
                break
            else:
               print( df.head(i*5))
               i += 1
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
