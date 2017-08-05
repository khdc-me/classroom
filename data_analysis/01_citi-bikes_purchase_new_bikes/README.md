# Citi Bikes Needs to Purchase New Bicycles  
**Situation:** City Bikes would like to purchase 700 bicycles, primarily to service riders who are 50 years of age or older.
The bicycles being considered for purchase are gender-specific (male/female).  
  
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
