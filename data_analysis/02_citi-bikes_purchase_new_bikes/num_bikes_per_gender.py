#
# Program uses Citi Bikes trip data from summer of 2016 (June, July, August)
# for the following scenario:
#
# Citi Bikes wants to acquire an additional 700 bicycles. The new bicycles are
# gender-specific (M/F) and will be reserved for its subscribers who are 50yrs
# of age or older. Taking into account that summer is the busiest season, how
# many bicycles should it purchase for each gender?
#

from zipfile import ZipFile
import csv

import datetime

import matplotlib.pyplot as plt
import numpy as np

DATA_FOLDER = '../data/'


class Riders:
    def __init__(self, label="", jun=0, jul=0, aug=0):
        """Instantiate a class for tracking number or riders during summer."""
        self.label = label
        self.jun = jun
        self.jul = jul
        self.aug = aug

    def summerTotal(self):
        """Return total number of riders for the summer"""
        return self.jun + self.jul + self.aug

    def summerAverage(self):
        """"Return average number of monthly riders for the summer"""
        return int(self.summerTotal()/3)

    def displayMonthlyNumRiders(self):
        """Display number of total riders per summer month"""
        print(self.label + " June: " + str(self.jun))
        print(self.label + " July: " + str(self.jul))
        print(self.label + " August: " + str(self.aug))


def unzip_files():
    """Unzip summer files (Jun, Jul, Aug csv) in '../data' folder.

    Saves contents (csv files) into the same directory.
    """
    summer_zips = ['201606-citibike-tripdata.zip',
                   '201607-citibike-tripdata.zip',
                   '201608-citibike-tripdata.zip',
                   ]
    for filename in summer_zips:
        try:
            with ZipFile(DATA_FOLDER + filename, "r") as z:
                print("Unzipping " + filename + "...")
                z.extractall(DATA_FOLDER)
                print("Done.")
        except:
            continue


def get_num_mf(summer_csv):
    """Return number of male/female riders ages 50-90 in specified csv files.

    Keyword arguments:
    summer_csv -- list of filenames corresponding to each summer month.

    Age 50 inclusive, age 90 exclusive; tripduration longer than 60 secs.
    """
    now = datetime.datetime.now()
    with open(DATA_FOLDER + summer_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        csv_keys = ['tripduration', 'birth year', 'gender']
        num_m = 0
        num_f = 0
        for row in reader:
            try:
                duration, birth_year, gender = ([int(row[key])
                                                 for key in csv_keys])
            except ValueError:
                continue
            if duration > 60 and 50 <= now.year - birth_year < 90:
                if gender == 1:
                    num_m += 1
                elif gender == 2:
                    num_f += 1
    return num_m, num_f


def get_total_num_mf():
    """Return total number of summer male/female riders.

    Columns in csv:
    tripduration | starttime | stoptime | start station id |
    start station name | start station latitude | start station longitude |
    end station id | end station name | end station latitude |
    end station longitude | bikeid | usertype | birth year | gender
    """
    summer_csvs = ['201606-citibike-tripdata.csv',
                   '201607-citibike-tripdata.csv',
                   '201608-citibike-tripdata.csv',
                   ]
    return list(map(get_num_mf, summer_csvs))


def unpack_riders(summer_riders):
    """Return monthly quantities for summer male and females riders."""
    jun_riders, jul_riders, aug_riders = ([month_riders
                                           for month_riders in summer_riders])
    jun_m, jun_f = [jun_mf for jun_mf in jun_riders]
    jul_m, jul_f = [jul_mf for jul_mf in jul_riders]
    aug_m, aug_f = [aug_mf for aug_mf in aug_riders]
    m_riders = Riders("males", jun_m, jul_m, aug_m)
    f_riders = Riders("females", jun_f, jul_f, aug_f)
    return m_riders, f_riders


def main():
    # Unzip summer files located in DATA_FOLDER, into same folder
    unzip_files()
    print("Retrieving number males and females over 50 years of age...")
    male_riders, female_riders = unpack_riders(get_total_num_mf())
    avg_summer_m = male_riders.summerAverage()
    avg_summer_f = female_riders.summerAverage()
    percent_m_frac = round((avg_summer_m) / (avg_summer_m+avg_summer_f), 2)
    percent_m_whole = int(percent_m_frac * 100)
    percent_f_whole = 100 - percent_m_whole
    print("Done.")

    print("Plotting...")
    title = {'family': 'sans-serif',
             'color': '#000000',
             'size': 20,
             'weight': 'bold',
             }

    font = {'family': 'sans-serif',
            'color': '#000000',
            'size': 16,
            }

    months = ["June", "July", "August"]
    fig1 = plt.figure(facecolor='#ffffff')
    fig1.suptitle('Citi Bikes Riders Ages 50+ (Summer of 2016)',
                  fontdict=title)
    axes1 = plt.axes(frameon=False)     # create axes w/out a border
    axes1.axes.get_yaxis().set_visible(False)
    spacing = np.arange(len(months))
    plt.xticks(spacing, months)
    monthly_m_riders = [male_riders.jun / 1000,
                        male_riders.jul / 1000,
                        male_riders.aug / 1000,
                        ]
    monthly_f_riders = [female_riders.jun / 1000,
                        female_riders.jul / 1000,
                        female_riders.aug / 1000,
                        ]
    plt.plot(spacing, monthly_m_riders, color='#0099ff',
                      label='Males')
    plt.plot(spacing, monthly_f_riders, color="#ff99cc",
                      label='Females')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="center", ncol=2,
               borderaxespad=0.)
    plt.text(0, (male_riders.jun / 1000),
             str(round(male_riders.jun / 1000, 1)) + " K", ha='left',
             fontdict=font)
    plt.text(1, (male_riders.jul / 1000) - 10,
             str(round(male_riders.jul / 1000, 1)) + " K", ha='center',
             fontdict=font)
    plt.text(2, (male_riders.aug / 1000),
             str(round(male_riders.aug / 1000, 1)) + " K", ha='right',
             fontdict=font)
    plt.text(0, (female_riders.jun / 1000),
             str(round(female_riders.jun / 1000, 1)) + " K", ha='left',
             fontdict=font)
    plt.text(1, (female_riders.jul / 1000) + 5,
             str(round(female_riders.jul / 1000, 1)) + " K", ha='center',
             fontdict=font)
    plt.text(2, (female_riders.aug / 1000),
             str(round(female_riders.aug / 1000, 1)) + " K", ha='right',
             fontdict=font)
    txt = ("Male riders account for " + str(percent_m_whole) + "%,"
            + " while female riders account for " + str(percent_f_whole)
            + "%." + "\nOf the 700 bicycles, " + str(int(700*percent_m_frac))
            + " should be male" + " and " + str(700 - int(700*percent_m_frac))
            + " should be female.")
    fig1.text(.5, .005, txt, ha='center')
    plt.show()
    print("Done.")


if __name__ == "__main__":
    main()
