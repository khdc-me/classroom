#
# Program uses Citi Bikes trip data from 2016 for the following scenario:
#
# Citi Bikes wants to acquire an additional 700 bicycles. The new bicycles are
# gender-specific (M/F) and will be reserved for its subscribers who are 50yrs
# of age or older, how many bicycles should it purchase for each gender?
#

import os
import os.path

from zipfile import ZipFile
import csv

import datetime

import matplotlib.pyplot as plt
import numpy as np

DATA_FOLDER = '../data/'


def unzip_files():
    """Unzips the 12 files in '../data' folder.

    Saves contents (csv files) into the same directory.
    """
    for filename in os.listdir(DATA_FOLDER):
        try:
            with ZipFile(DATA_FOLDER + filename, "r") as z:
                print("Unzipping " + filename + "...")
                z.extractall(DATA_FOLDER)
                print("Done.")
        except:
            continue


def get_num_mf(fn, kt):
    """Return number of male/female riders ages 50 - 90 in specified csv file.

    Keyword arguments:
    fn -- filename (csv file)
    kt -- key text (are keys capitalized? T/F)

    Age 50 inclusive, age 90 exclusive; tripduration longer than 60 secs.
    """
    now = datetime.datetime.now()
    with open(DATA_FOLDER + fn) as csvfile:
        reader = csv.DictReader(csvfile)
        if kt:
            csv_keys = ['Trip Duration', 'Birth Year', 'Gender']
        else:
            csv_keys = ['tripduration', 'birth year', 'gender']
        num_m = 0
        num_f = 0
        for row in reader:
            try:
                duration, birth_year, gender = ([int(row[key])
                                                 for key in csv_keys])
                print("duration: " + str(duration))
                print("birth year: " + str(birth_year))
                print("gender: " + str(gender))
            except ValueError:
                continue
            if duration > 60 and 50 <= now.year - birth_year < 90:
                if gender == 1:
                    num_m += 1
                elif gender == 2:
                    num_f += 1
    return num_m, num_f


def get_total_num_mf():
    """Return total number of male/female riders.

    Calls function get_num_mf().

    Columns in csv:
    tripduration | starttime | stoptime | start station id |
    start station name | start station latitude | start station longitude |
    end station id | end station name | end station latitude |
    end station longitude | bikeid | usertype | birth year | gender
    """
    total_num_m = 0
    total_num_f = 0
    for filename in os.listdir(DATA_FOLDER):
        _, filename_ext = os.path.splitext(DATA_FOLDER + filename)
        if filename_ext == '.csv':
            print("Starting to count from " + filename)
            if (filename == '201612-citibike-tripdata.csv'
                or filename == '201611-citibike-tripdata.csv'
                or filename == '201610-citibike-tripdata.csv'):
                # capitalizes first letters in keys (ie: 'Birth Year')
                is_cap_key_text = True
            else:
                # does not capitalize first letters in keys (ie: 'birth year')
                is_cap_key_text = False
            num_m, num_f = get_num_mf(filename, is_cap_key_text)
            total_num_m += num_m
            total_num_f += num_f
    return total_num_m, total_num_f


def main():
    # Unzip 12 files located in DATA_FOLDER, into same folder
    unzip_files()
    print("Retrieving number males and females over 50 years of age...")
    total_num_males, total_num_females = get_total_num_mf()
    percent_males_frac = round(total_num_males /
                               (total_num_males + total_num_females), 2)
    percent_males_whole = int(percent_males_frac * 100)
    percent_females_whole = 100 - percent_males_whole
    print("Done.")

    print("Plotting...")
    title = {'family': 'sans-serif',
             'color': '#000000',
             'size': 20,
             'weight': 'bold'
             }

    font = {'family': 'sans-serif',
            'color': '#000000',
            'size': 16,
            }

    recommendation = {'family': 'sans-serif',
                      'color': '#000000',
                      'size': 12,
                      }

    genders = ['Male', 'Female']
    qty_per_gender = [total_num_males, total_num_females]
    plt.figure(facecolor='#ffffff')
    axes1 = plt.axes(frameon=False)     # create axes w/out a square border
    spacing = np.arange(len(genders))
    bars = plt.bar(spacing, qty_per_gender, align='center', alpha=1)

    plt.title('Citi Bikes Riders Ages 50+ (2016)', fontdict=title)
    plt.xticks(spacing, genders)
    axes1.axes.get_yaxis().set_visible(False)
    bars[0].set_color('#0099ff')
    bars[1].set_color('#ff99cc')
    males_label = (str(round(total_num_males/1000000, 2))
                   + "M | " + str(percent_males_whole) + "%")
    male_y_offset = total_num_males + 25000
    plt.text(0, male_y_offset, males_label, ha='center', fontdict=font)
    females_label = (str(round(total_num_females/1000000, 2))
                     + "M | " + str(percent_females_whole) + "%")
    female_y_offset = total_num_females + 25000
    plt.text(1, female_y_offset, females_label, ha='center', fontdict=font)
    plt.text(1, 1000000, "Of the 700 bicycles,\n "
             + str(int(700*percent_males_frac))
             + "(" + str(percent_males_whole)
             + "%) should be male and\n"
             + str(700 - int(700*percent_males_frac))
             + "(" + str(percent_females_whole)
             + "%) should be female", ha="center", fontdict=recommendation)
    plt.show()
    print("Done.")
    plt.close()


if __name__ == "__main__":
    main()
