import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
city_name = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs
    city = input(" please choose a city between:\n1.chicago\n2.new york city\n3.washington\n ").lower()
    while city not in city_name:
        city = input("invalid input!!!\nplease choose a city\n1.chicago\n2.new york city\n3.washington\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(" please choose a month\n1.January\n2.February\n3.March\n4.April\n5.May\n6.June\n7.All\n ").lower()
    while month not in months:
        if month == "all":
            break
        month = input(
            "invalid input!!!\nplease choose a month\n1.January\n2.February\n3.March\n4.April\n5.May\n6.June\n7.All\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        " please choose a day\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday\n8.All\n ").lower()
    while day not in days:
        if day == "all":
            break
        day = input(
            "invalid input!!!\nplease choose a day\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6"
            ".Saturday\n7.Sunday\n8.All\n")

    print('-' * 40)
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
    df['month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != "all":
        month = months.index(month) + 1
        df = df[df["month"] == month]
    if day != "all":
        df = df[df['Weekday'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is:\n", most_common_month, "\n")

    # TO DO: display the most common day of week
    print("The most common day is:\n", str(df['Weekday'].mode()[0]), "\n")

    # TO DO: display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    print("The most common start hour is:\n", str(df['hour'].mode()[0]), "\n")

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most most commonly used start station is:\n" + str(df["Start Station"].value_counts().idxmax()), "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is:\n" + str(df["End Station"].value_counts().idxmax()), "\n")

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip commonly used start station is:\n" +
          str(df.groupby(['Start Station', 'End Station']).size().nlargest(1)), "\n")

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is:\n" + str(sum(df["Trip Duration"])) + " days\n")

    # TO DO: display mean travel time
    print("The mean travel time is:\n" + str(int(df["Trip Duration"].mean())) + " days\n")

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types:\n" + str(df["User Type"].value_counts()), "\n")

    # TO DO: Display counts of gender
    try:
        print("Gender types:\n" + str(df["Gender"].value_counts()), "\n")
    except:
        (print("Washington city does not has gender registrations\n"))
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("Earliest birth year:\n" + str(int(df["Birth Year"].min())), "\n")
        print("Most recent birth year:\n" + str(int(df["Birth Year"].max())))
        print("Most common birth year:\n" + str(int(df["Birth Year"].mode()[0])))
    except:
        (print("Also Washington does not has a birth dates!\n"))
    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):

    i = 0
    # TO DO: convert the user input to lower case using lower() function
    raw = input("Would you like to see the raw data?\n").lower()
    pd.set_option('display.max_columns', 200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            print(df[i:i + 5])
            # TO DO: convert the user input to lower case using lower() function
            raw = input("Would you like to see more raw data?\n").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
