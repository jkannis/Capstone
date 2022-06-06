# Capstone

## Presentation

### Selected topic
Coffee Characteristics

### Reason why they selected their topic 
We chose this topic after considering suggestions from each team member. We were interested in finding a dataset with enough data to allow us to utilize the skills we have learned over the course of this class, but that was also interesting to the team. After reviewing the data in this dataset we were curious to see how the region and altitude of the grower affected the qualities of the coffee produced.

### Description of their source of data
The dataset used in this project is based on the Coffee Quality Institute (CQI) Coffee Quality Database published in 2018. This data shows ratings for several quality standards for coffee. The criteria used to identify the beans are species, region of farm, producer, altitude of farm, and harvest year.

The data for this analysis was taken from https://github.com/jldbc/coffee-quality-database/tree/master/data.

The datasets being used are arabica_ratings_raw.csv and robusta_ratings_raw.csv.

### Questions they hope to answer with the data
- How does the growing region affect the quality ratings of the coffee produced?
- How does the altitude of the farm affect the quality ratings of the coffee produced?
- Do different coffee bean species qualify differently based on the region or altitude?

## Machine Learning - Sarah
We approached the third deliverable by expanding on our initial unsupervised ML models (KMeans & Hierarchical). As a group, we were interested in seeing how the descriptives of our coffee dataset (aroma, flavor, aftertaste, acidity, etc) grouped with the geographical components of our dataset (region, country of origin, etc). 

## KMeans Clustering
We continued our analysis by applying KMeans to several potential groupings as exhibited below:

### [Country of Origin & Coffee Demos](https://github.com/jkannis/Capstone/blob/machine_learning/ML%20D3%20June%201.ipynb)
<img width="853" alt="Screen Shot 2022-06-05 at 10 23 13 AM" src="https://user-images.githubusercontent.com/95551195/172062553-bffb1ee3-ccca-4588-bc98-78b6568fb38d.png">

### [Region & Coffee Demos](https://github.com/jkannis/Capstone/blob/machine_learning/ML%20D3%20(KMeans%20Region))
<img width="873" alt="Screen Shot 2022-06-05 at 10 24 21 AM" src="https://user-images.githubusercontent.com/95551195/172062580-a4f19056-e39e-456b-b630-923e55a0108c.png">

### [Country, Region, & Coffee Demos](https://github.com/jkannis/Capstone/blob/machine_learning/ML%20D3%20(KMeans%20Country%2C%20Region%2C%20%26%20More).ipynb)
<img width="729" alt="Screen Shot 2022-06-05 at 10 26 02 AM" src="https://user-images.githubusercontent.com/95551195/172062632-439154d7-5cd3-4106-b187-51478690a053.png">

## Hierarchical Clustering

### [Country of Origin & Coffee Demos](https://github.com/jkannis/Capstone/blob/machine_learning/ML%20D3%20(Hierarchical%20Country%20of%20Origin).ipynb)
<img width="871" alt="Screen Shot 2022-06-05 at 10 29 20 AM" src="https://user-images.githubusercontent.com/95551195/172062785-b79f6690-e811-4c2b-a4be-6eb44574d759.png">

### [Region & Coffee Demos](https://github.com/jkannis/Capstone/blob/machine_learning/ML%20D3%20(Hierarchical%20Region).ipynb)
<img width="860" alt="Screen Shot 2022-06-05 at 10 28 10 AM" src="https://user-images.githubusercontent.com/95551195/172062724-46fdf674-96a1-4320-83ed-cf465f5fba6f.png">

## What model & why?
After our analysis of the dataset using both KMeans & Hierarhical ML approaches, we decided to move forward with KMeans clustering for the purposes of this project for a variety of reasons. It is evident that given the size and type of dataset we are working with that Hierarhical ML provided an overwhelming output (as exhibited by the massive hierarhical trees created). Additional time would be required to prune the trees to the level needed for the model to be informative/useful for our dataset. In addition, the dataset we are working with has a variety of datatypes which can make inputting the data into the model a challenge. We have decided to move forward with KMeans ML as the model was easy to implement and was easily scaled to our large datasets.

## Deliverable 3 Prelimnary Results & Takeaways
We were able to successfully cluster our dataset in the unsupervised KMeans Learning for Region & Country. For Region, it appears that the clusters across region/aroma/flavor are largely categorized in cluster 4. It also appears the region of 'Oriente' & 'Veracruz' have additional cluster representations in the model than the other regions.

<img width="875" alt="Screen Shot 2022-06-05 at 1 40 39 PM" src="https://user-images.githubusercontent.com/95551195/172069686-1cd62262-657d-4321-a649-ee2bc576d24b.png">

<img width="881" alt="Screen Shot 2022-06-05 at 1 38 36 PM" src="https://user-images.githubusercontent.com/95551195/172069613-83309672-9395-4a5e-b5ad-b30693c02a35.png">

For Country, it appears Country of origin/aroma/flavor fall into 3 cluters (largely represented in cluster 3). Brazil & Taiwan appear to have more datapoints across cluster than the other Countries of Origin.
<img width="841" alt="Screen Shot 2022-06-05 at 1 45 40 PM" src="https://user-images.githubusercontent.com/95551195/172069852-bff6139b-7c73-47d5-b23d-08c2df83fab2.png">

<img width="884" alt="Screen Shot 2022-06-05 at 1 45 54 PM" src="https://user-images.githubusercontent.com/95551195/172069857-b21909ef-c33f-438b-97cf-539ed63004e1.png">

For future consideration we would look into how to determine the optimal number of classes. We could do this by completing an ANOVA analysis to compare inter/intra-class variability. In addition, we were only able to look into a few features of the dataset, and additional exploration into data type/columns could yield interesting results from the model. Lastly, prior to completeing the fourth deliverable, we will connect our ML model to our PostGres database.

## Data Cleaning - Chinky

### The Dataset
The dataset used in this project is based on the Coffee Quality Institute (CQI) Coffee Quality Database published in 2018.

The data for this analysis was taken from https://github.com/jldbc/coffee-quality-database/tree/master/data.
The datasets being used are arabica_ratings_raw.csv and robusta_ratings_raw.csv.

### Analysis Method
Our analysis plan will be undergoing following steps :

- Perform Exploratory Data Analysis to gain insights about the raw data, identify potential data problems, features and target variables, as well as metrics.
- Preprocess the data to make it suitable for machine learning. This will be done in two steps :
- Cleaning the data to remove the identified issues
- Feature Engineering to allow and prepare for use of machine learning algorithms
- Select and validate a suitable predictive Machine Learning model
- The code in this project will be written in Python. 

## Exploratory Data Analysis (EDA)
In this section, an initial exploratory analysis of the dataset was done. The dataset was evaluated for any data quality issues that need to be resolved. 
These data contain reviews of 1312 arabica and 28 robusta coffee beans from the Coffee Quality Institute's trained reviewers.

### Data Types:
The variables in the dataset are mix of numeric and non-numeric variables.
The numeric values contain dates as well as scalar values
The non-numeric variables contain categorical data, free text and hexadecimal-encoded data.

### Missing Values:
- There are a lot of missing values in this dataset.Columns 'Unnamed: 0','NA.3','NA.2','view_certificate_1','view_certificate_2','Cupping Protocol and Descriptors','View Green Analysis Details','Request a Sample','Unnamed: 51','Notes','Lot Number','Certification Address','Certification Contact','Owner.1','Bag Weight','Mill','ICO Number','NA','Quakers','NA.1','Farm Name','Mill' were removed with 32 columns.
- In order to analyze the dataset better,dataset was splitted in measures, beans and origin.
  measures = ['Aroma', 'Flavor','Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity', 'Clean Cup', 'Sweetness', 
             'Cupper Points','Total Cup Points']

  beans = ['Species', 'Harvest Year', 'Grading Date','Variety', 'Processing Method', 'Moisture', 'Category One Defects' 
        ,'Color', 'Category Two Defects','Expiration']

  origin = ['Country of Origin','Region','Altitude']

- Checked the distribution of each coffee characteristics with histogram/histplot.
-  ![image](https://user-images.githubusercontent.com/95595378/170875895-7ff03c8b-fb19-42d6-97b9-f3fa28240ba4.png)

- Checked the correlation among coffee characteristics and Cupper point through Scatterplots.
![image](https://user-images.githubusercontent.com/95595378/170876077-27aa2653-f1f4-4a94-9990-3cedd607c398.png).
- The variable "Total Cup Points" was not considered since it is the result of adding all measure values.

## EDA Summary
During our exploration of the Coffee Quality dataset, several issues were encountered with the data:
- Many variables with missing values.
- Columns with zero variance or strongly correlated to others.
- Columns with inconsistent format that will either have to be preprocessed, or dropped.
-The coffee quality can be measured with by professional according to serval factors such as:Acidity,Aroma,Flavor,Balance,Sweetness among  others.They also grade each one of these factor to get final score.which indicates the quality of coffee.
There are some factors that influence the taste of coffee,for example,species,roasting and grinding.Another one is altitude,which is related to two important variables, weather and temperature. 

## Dashboard - Vileam
### Visualizations
Visualizations will be presented showing the characteristics of the coffee that are affected by region, altitude and producer, as well as maps to show delineations of coffee production regions.

### Google Slide Presentation
A Google slide presentation is being finalized by each team member. 
[Google Presentation](https://docs.google.com/presentation/d/145j3lfdzGyylFtMaBlVn-_ZCiShIyszpF6u9ChYgUYs/edit?usp=sharing)

### Tableau
![Capture](https://user-images.githubusercontent.com/96033992/170884923-a8f22d2c-5e4e-444f-a36e-4852fc6c3963.PNG)
As you can see this images show the aroma from country of origin.
We also have origin as filter for easier interative.

## Database - Julie

This project uses a PostgreSQL database to store the data from the Arabica and Robusta coffee datasets. The database has been designed to hold the cleaned data as well as some reference tables to allow label creation from the normalized data for the final dashboard. 

The cleaned datasets were further modified before writing to the database as follows:
- Several columns were removed as it was discovered they were not needed for accurate modeling.
- Some columns contained symbols and text in addition to the numerical data, so the no-numerical data was removed.
- Some columns were renamed to remove spaces to make SQL cleaner.

The Python geopy API was used to collect the latitude and longitude coordinates for each country in the datasets and store this information in a regions table. A join has been written to combine the region details with each row of the coffee data to allow for providing maps of coffee-growing regions in the final dashboard.

![Database ERD](https://github.com/jkannis/Capstone/blob/main/database/CoffeeDB_ERD.png)

[Database Schema](https://github.com/jkannis/Capstone/blob/main/database/CoffeeDB_Schema.sql)

[Python File](https://github.com/jkannis/Capstone/blob/main/database/CSV_toPostgres.ipynb)