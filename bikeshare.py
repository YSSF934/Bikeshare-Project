import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


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
    
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?").lower()
        if city not in CITIES:
            print('Sorry, this is not one of the cities available in our database. Please enter again.')
        else:
            break
    else:
        print("Invalid Input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to look at (say all if you want!)').lower()
        if month not in MONTHS:
            print('Sorry, this is not one of the months available in our database. Please enter again.')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input('And finally, which day of the week would you like to look at (say all if you want!)')
        if day not in DAYS:
            print('Sorry, this is not one of the days available in our database. Please enter again.')
        else:
            break

    print('-'*40)
    return city, month, day


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
    
    df = pd.read_csv(CITY_DATA[city])
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # filter by month if applicable
    df['month'] = df['Start Time'].dt.month
    if month != 'all': 
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
    #filter day of weekif applicable
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
    #filter by day of week to create new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
   
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most popular month traveled: {}.\n'.format(common_month))

    # TO DO: display the most common day of week
    pop_day_of_week = df['day_of_week'].mode()[0]
    print('Most popular day of week: {}.'.format(pop_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('Most popular hour: {}.'.format(pop_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('{} is the most commonly used start station.\n'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('{} is the most commonly used end station.\n'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    
    
    frequent_combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(n=1)
    print('frequent_combination is: {}'.format(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["travel_time"] = df["End Time"] - df["Start Time"]
    total_travel_time = df["travel_time"].sum()
    print("Total Travel Time:", total_travel_time)
    
    # TO DO: display mean travel time
    average_travel_time = df["travel_time"].mean()
    print("Average Travel Time:", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The total amount of each user type is:\n{}\n'.format(user_type))

    try:
    # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('The gender count is: ', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('The earliest birth year: {}.\n'.format(earliest_year))
        latest_year = df['Birth Year'].max()
        print('The latest birth year: {}.\n'.format(latest_year))
        common_year = df['Birth Year'].mode()
        print('The most common birth year: {}.\n'.format(common_year))
    except:
        print("Gender or birth year column is not available for washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input(df):
    i = 0
    while True:
        display_more=input("Do you want to see 5 more lines of data? Yes or No.\n").lower()
        if display_more=='yes':
            five_rows=df.iloc[:i+5]
            print(five_rows)
            i+= 5
        else:
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
