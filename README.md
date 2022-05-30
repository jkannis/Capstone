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

## Machine Learning - Sara
Unsupervised machine learning will be used to cluster data for identifying characteristics of coffee based on things such as region grown, altitude of farm, species of coffee bean, and production company.

## Module Questions: 

### Which model did you choose and why?

Clustering - Unsupervised learning is the best way forward for our dataset because we are looking for any groupings, trends, or other information that could help us provide informative coffee data to customers/consumers/interested parties alike. We want to investigate the dataset and look for patterns to help address numerous questions we have as a group. Such as:

- How are region/quality of coffee related?
- How is altitude/quality of coffee related?
- Comparing Robusta & Arabica coffee bean species - any differences in outcomes amongst these two datasets?

### How are you training your model?

We want to add K-Means Clustering to create a compatible clustering model - We will take our Coffee Dataset and select columns from our dataset to build our clusters. Better yet, we want to discover any trends in our clusters - What is the outcome based on Year? Country? Aroma & Flavor? We hope to explore the possibilities wihtin our dataset. 

We are actively looking at dimensionality reduction as well in an attempt to not overwhelm the machine with features. If we want to look at removing features, we will use PCA. In this approach, we will standardize our data with StandardScaler, take in argument of n_components, & apply dimensionality reduction on scaled dataset. We will also look to at explained variance ratio & apply elbow curve & plot.  We are also entertaining the idea of comparing hierarchical clustering vs K-Means clustering. 

Thus far, I have lightly applied several of the components above in the two python file uploads found in this Machine Learning Branch. As a team, we will continue to explore possibilities of continuing to build our model and identify additional trends & findings. Below, find several visuzaliations created within the model:


### What is the model's accuracy?

Accuracy by K-Means clustering method is the calculated Square Error Value (SE) of each data in cluster.

### How does his model work?

Clustering will allow us to discover natural groupings in the coffee dataset through means of viewing centroid clusters. 

As a group, we will continue to discover and improve the workings of the clustering model. 

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
-Feature Engineering to allow and prepare for use of machine learning algorithms
- Select and validate a suitable predictive Machine Learning model
- The code in this project will be written in Python. 

## Webpage - Vileam
### Overview
  This part of analytic will be focusing on creating a webpage that overview the data and the results. There will be image, decription that descript the data set and the visualization part of the project.
  
### Result

### summary

## Database - Julie

The data generated from the machine learning model is stored in a Python DataFrame. Once the modeling is complete, SQLAlchemy is used to connect to our PostgreSQL coffee_data database to insert the modeled data into coffeeQualities table. To allow for machine learning some of the data was normalized and converted to numbers. To make this data more meaningful in visualizations and additional table was created in the database as a reference for the species code numbers. This Species table is joined with the coffee_data table to provide a descriptive species name rather than a numeric code. As the data modeling is finalized more tables and relationships may be added to the database.

[SQL File](https://github.com/jkannis/Capstone/blob/main/QuickDBD-coffeeQualities.sql)

[Python File](https://github.com/jkannis/Capstone/blob/main/toDatabase.ipynb)

![Database ERD](https://github.com/jkannis/Capstone/blob/main/Resources/Hierarchical4_ERD.png)
