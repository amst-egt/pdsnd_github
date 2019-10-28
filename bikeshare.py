import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['saturday' , 'sunday' , 'monday', 'tuesday' , 'wednesday' , 'thuresday' , 'friday']


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
        try:
            city = input("Enter city name you want to access its data\nCities: Chicago - New York City - Washington ")
            if city in CITY_DATA.keys():
                break
        except ValueError:
            print("Typing error... Please enter a valid city from\nCities: Chicago - New York City - Washington ")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Enter the month you want to access\nMonthes: JANUARY - FEBRUARY - MARCH - APRIL - MAY\nJUNE - JULY - AUGUST - SEPTEMBER - OCTOBER - NOVEMBER - DECEMBER - All ").lower()
            if month in months :
                break
        except:
            print("Typing error... Please enter a valid month from\nMonthes: JANUARY - FEBRUARY - MARCH - APRIL - MAY\nJUNE - JULY - AUGUST - SEPTEMBER - OCTOBER - NOVEMBER - DECEMBER - All ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter the month you want to access\nDays: SATURDAY - SUNDAY - MONDAY\nTUESDAY - WEDNESDAY - THURESDAY - FRIDAY - All\'for no filter\'").lower()
            if day in days:
                break
        except:
            print("Typing error... Please enter a valid day from\nDays: SATURDAY - SUNDAY - MONDAY\nTUESDAY - WEDNESDAY - THURESDAY - FRIDAY - All")


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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    mst_com_mnth = df['month'].mode()[0]
    # print the most popular traveling month
    print("the most popular traveling month: {}\n".format(mst_com_mnth))

    # TO DO: display the most common day of week

    # extract day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # find the most popular day
    mst_com_dy = df['day_of_week'].mode()[0]
    # print the most popular traveling day
    print("the most popular traveling day: {}\n".format(mst_com_dy))

    # TO DO: display the most common start hour

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    # find the most common start hour
    mst_com_hr = df['hour'].mode()[0]
    # print the most popular hour for start traveling
    print("the most popular traveling start hour: {}\n".format(mst_com_hr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # print the most common traveling start station
    mst_com_str = df['Start Station'].mode()[0]
    print("the most common traveling start station: {}\n".format(mst_com_str))

    # TO DO: display most commonly used end station

    # print the most common traveling end station
    mst_com_end = df['End Station'].mode()[0]
    print("the most common traveling end station: {}\n".format(mst_com_end))

    # TO DO: display most frequent combination of start station and end station trip

    # print the most common traveling stations
    mst_com_stn = df[['Start Station' , 'End Station']].mode().loc[0]
    print("the most common traveling stations as a start & end traveling Station respectively {}\n".format(mst_com_stn))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # print the total travel traveling time
    total_travel_time = np.sum(df['Trip Duration'])
    print("the total travel traveling time: {}\n".format(total_travel_time))

    # TO DO: display mean travel time

    # print the mean of traveling time
    mean_travel_time = np.mean(df['Trip Duration'])
    print("the mean of traveling time: {}\n".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print("users types: {}\n".format(user_types))

    # TO DO: Display counts of gender

    # check if 'Birth Year' column is excists
    if 'Gender' in df:
    # print value counts for each user gender
        user_gender = df['Gender'].value_counts()
        print("users genders: {}\n".format(user_gender))

    # TO DO: Display earliest, most recent, and most common year of birth

    # check if 'Birth Year' column is excists
    if 'Birth Year' in df:
        # print the earliest year of birth
        earliest_birth = df['Birth Year'].min()
        print("the earliest year of birth for a user: {}\n".format(earliest_birth))

        # print the most recent year of birth
        most_recent_birth = df['Birth Year'].max()
        print("the most recent year of birth for a user: {}\n".format(most_recent_birth))

        # print the most common year of birth
        most_common_birth = df['Birth Year'].mode()
        print("the most common year of birth for a user: {}\n".format(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
