# Capstone

## Communication Protocols

Our team will meet via Zoom during Office Hours as well as once per week through the first two weeks. Team members will check in via Slack daily with updates regarding project progress, as well as any issues or questions so as not to delay the project progress.

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
We approached the second deliverable using two different types of unsupervised ML models: KMeans Clustering & Hierarchical Clustering.  
- KMeans clustering allows us to quickly cluster our larger dataset into groupings to identify groupings/trends. We will be able to predetermine the number of clusters in this process. 
- Hierarhical clustering generates a series of models with various cluster solutions from 1 (all points in a single cluster) to n (each case is an individual cluster). 
We chose to move forward with KMeans & Hierarchical in order to identify groupings within the coffee dataset not previously seen. We are curious to know if KMeans clustering or Hierarhical clustering will provide more insight.

## KMeans
In our continued preliminary analysis, it appears the models yield different accuracy results. We began with KMeans clustering by taking our previously cleanded dataset we applied MinMaxScaler to transform the dataset. We used the elbow method to determine an appropriate number of clusters and applied our model to assign/predict the datapoints to a cluster. We then began to plot the data points based on a variety of paradigms to see what our clustering column produced.
<img width="616" alt="Screen Shot 2022-05-29 at 8 16 45 AM" src="https://user-images.githubusercontent.com/95551195/170873744-423892e7-1052-4cb5-82a2-e087c0c62265.png">

<img width="878" alt="Screen Shot 2022-05-29 at 8 17 22 AM" src="https://user-images.githubusercontent.com/95551195/170873776-480f9e80-6b4d-4181-9ac1-bb5d5dcba5f4.png">

<img width="847" alt="Screen Shot 2022-05-29 at 8 17 45 AM" src="https://user-images.githubusercontent.com/95551195/170873800-abe44bc3-bce7-4a61-b1f2-d00c77cc668b.png">

Following this process we applied PCA to the datatset to determine if we wanted to reduce the number of input features. Here was the result of that process:
We began by inputing 2 features. We then applied our explained variance ratio and determined 64% of the data was retained from the original dataset.
We then tried 3 features. We then applied our explained variance ratio and determined 74% of the data was retained from the original dataset.
We then tried 4 features. We then applied our explained variance ratio and determined 80% of the data was retained from the original dataset.

We then plotted the results of our clustering.

<img width="609" alt="Screen Shot 2022-05-29 at 8 44 22 AM" src="https://user-images.githubusercontent.com/95551195/170875336-a663e57c-254a-4c5d-b597-6a6ce4ed6fce.png">

## Hierarchical Clustering 
After completing the KMeans clustering, we pivoted and looked to apply hierarchical clustering to the dataset. We first began by taking our previously cleaned dataset and normalized the data. We created the linkage to plot the datapoints together and called the dendrograms library to plot our newly created linkages. We then used euclidean distance to determine clustering. 

<img width="894" alt="Screen Shot 2022-05-29 at 9 08 14 AM" src="https://user-images.githubusercontent.com/95551195/170876504-2739f92f-b22a-4dab-bf13-bdb2c681daf5.png">

<img width="563" alt="Screen Shot 2022-05-29 at 9 08 31 AM" src="https://user-images.githubusercontent.com/95551195/170876517-6f006357-13e5-45e8-bb60-0bbc7b8a1e9d.png">

It is evident that there appears to be an issue/potential outlier in the dataset that is making the dendogram a challenge to read. In an attempt to alleviate this issue, we completed the same hierarchical clustering process on 4 features of the dataset (Aroma, Flavor, Acidity, Body). The results of that process can be seen below:

<img width="867" alt="Screen Shot 2022-05-29 at 9 10 35 AM" src="https://user-images.githubusercontent.com/95551195/170876600-90ca742a-f996-4504-b3fd-6fee4bf396ff.png">

## Deliverable 2 Prelimnary Results & Takeaways

In sum, out team was able to successfully create 2 different unsupervised machine learning models using KMeans & Hierarhical Clustering. We chose this method of ML in an attempt to find patterns/groupings amongst our coffee dataset as we do not have an anticipated/expected outcome/variable. We did not have to split out data into training/testing sets as we are using clustering in ML. 

In our experience with the ML, both KMeans & Hierarhical clustering have limitations and benefits. 

- KMeans Benefits: Easy to implement, guranteed convergence, easily scaled to large datasets.

- KMeans Limitations: Having to choose k naturally, challenge clustering data based on size & density, clustering outliers (as exhibited in our current working code).

- Hierarhical Benefits: Easy to implement, provides a visually appealing dendogram.

- Hierarhical Limitations: May not find the best solution, works poorly with missing data, challenge with outputs based on data types.

Thus far, we have continued to apply and test out our KMeans/Hierarhical models. The 3 jupyter notebook uploads contain code of our efforts. Over the next week, we will continue to perfect and improve our model to discover insight on our Coffee Dataset.

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
Visualizations will be created to show the characteristics of the coffee that are affected by region, altitude and producer, as well as maps to show delineations of coffee production regions.

### Google Slide
Google slide draft is made. Everyone have access to google slide. We will update the google slide as we go on with the project.

### Tableau
![Capture](https://user-images.githubusercontent.com/96033992/170884923-a8f22d2c-5e4e-444f-a36e-4852fc6c3963.PNG)
As you can see this images show the aroma from country of origin.
We also have origin as filter for easier interative.
Dashboard: https://public.tableau.com/views/Capstone_16538416430700/Sheet3?:language=en-US&:display_count=n&:origin=viz_share_link

## Database - Julie

The data generated from the machine learning model is stored in a Python DataFrame. Once the modeling is complete, SQLAlchemy is used to connect to our PostgreSQL coffee_data database to insert the modeled data into coffeeQualities table. To allow for machine learning some of the data was normalized and converted to numbers. To make this data more meaningful in visualizations and additional table was created in the database as a reference for the species code numbers. This Species table is joined with the coffee_data table to provide a descriptive species name rather than a numeric code. As the data modeling is finalized more tables and relationships may be added to the database.

[SQL File](https://github.com/jkannis/Capstone/blob/main/QuickDBD-coffeeQualities.sql)

[Python File](https://github.com/jkannis/Capstone/blob/main/DatabaseLoad.ipynb)

![Database ERD](https://github.com/jkannis/Capstone/blob/main/Resources/Hierarchical4_ERD.png)

