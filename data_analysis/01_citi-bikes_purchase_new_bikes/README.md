# Citi Bikes Needs to Purchase New Bicycles  
## About Citi Bike  
According to the [Citi Bike web site](https://www.citibikenyc.com/), they are "the nation's largest
bike share program." They have "10,000 bikes and 600 stations across Manhattan, Brooklyn, Queens and
Jersey City."  
  
The Citi Bike organization provides [trip history data](https://www.citibikenyc.com/system-data) to
the public.

**About the Data:** Data for this program is from 2016 and From Citi Bike's [Index of bucket "tripdata"](https://s3.amazonaws.com/tripdata/index.html), MANUALLY downloaded all 2016 zip files, as site prohibits automated fetching.
Each zip file contains a single csv file that, in turn, contains anywhere between ~1/2M amd 2M records.

**Situation:** City Bikes would like to purchase 700 bicycles, primarily to service riders who are
50 years of age or older. The bicycles being considered for purchase are gender-specific (male/female).  
  
**Task:** Suggest the number of bicycles that Citi Bike should purchase for each gender.  
  
## num_bikes_per_gender.py  
**Modules used:** os, os.path, ZipFile, csv, datetime  
**Packages used:** matplotlib.pyplot, numpy  
**Source Code Checker:** flake8  
  
Program unzips 12 zip files onto same directory where zip files are stored (../data/).
Program then find the number of male and female riders whose records:
* indicate an age between 50 (inclusive) and 90 (exclusive) - determined by the rider's 'birth year'  
* have a ride that lasted longer than 60 seconds - determined by 'tripduration'  
* assign male or female values to 'gender' | data users 1 for males and 2 for females  
* are exactly as we expect them (ie: excludes records where 'gender' or 'birth year' fields are blank)  

### matplotlib  
After gathering counts and calculating percentages, matplotlib is called to display the results.
![Number of Male and Female Bicycles to Purchase](https://github.com/khdc-me/classroom/blob/master/data_analysis/01_citi-bikes_purchase_new_bikes/01_citi-bikes-mf.png)
