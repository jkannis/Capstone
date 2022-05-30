#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initial imports
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from path import Path
from matplotlib import pyplot as plt
import plotly.express as px
import hvplot.pandas


# In[2]:


# Load the crypto_data.csv dataset.
file_path = "/Users/sarahhill/Desktop/MasterFolder/SH Cap/merged_data_cleaned.csv"
coffee_df = pd.read_csv(file_path, index_col=0)
coffee_df


# In[3]:


coffee_df.drop(columns=['Owner'], inplace=True)
coffee_df.head()


# In[4]:


coffee_df.drop(columns=['Farm.Name', 'Lot.Number', 'Mill', 'ICO.Number', 'Company'], inplace=True)
coffee_df.head()


# In[5]:


coffee_df.drop(columns=['Producer', 'Number.of.Bags', 'Bag.Weight', 'In.Country.Partner', 'Grading.Date'], inplace=True)
coffee_df.head()


# In[6]:


coffee_df.drop(columns=['Owner.1', 'Variety', 'Processing.Method', 'Category.Two.Defects', 'Expiration'], inplace=True)
coffee_df.head()


# In[7]:


coffee_df.drop(columns=['Category.One.Defects', 'Quakers', 'Color', 'Certification.Body', 'Certification.Address'], inplace=True)
coffee_df.head()


# In[8]:


coffee_df.drop(columns=['Certification.Contact', 'unit_of_measurement'], inplace=True)
coffee_df.head()


# In[9]:


#Transform Species Column
def change_string(Species):
    if Species == "Arabica":
        return 1
    else: 
        return 0
    
coffee_df["Species"] = coffee_df["Species"].apply(change_string)
coffee_df.head()


# In[10]:


coffee_df.drop(columns=['Region', 'Country.of.Origin'], inplace=True)
coffee_df.head()


# In[11]:


coffee_df.drop(columns=['Altitude'], inplace=True)
coffee_df.head()


# In[12]:


coffee_df.drop(columns=['Harvest.Year'], inplace=True)
coffee_df.head()


# In[13]:


# Drop null rows
coffee_df = coffee_df.dropna()


# In[14]:


X = coffee_df[['Aroma', 'Flavor','Acidity', 'Body']].copy()
X


# In[15]:


X_scaled = MinMaxScaler().fit_transform(X)
X_scaled


# In[16]:


sse = {}
k = range(1, 11)
for i in k:
    km = KMeans(n_clusters=i).fit(X_scaled)
    sse[i] = km.inertia_
    
#plot
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel('k')
plt.ylabel('SSE')
plt.title('Elbow Method')
plt.show()


# In[17]:


model = KMeans(n_clusters=3, random_state = 42).fit(X_scaled)


# In[18]:


y_pred = model.predict(X_scaled)


# In[19]:


df_y = pd.DataFrame(y_pred, columns = ['Cluster'])
combined = coffee_df.join(df_y, how ='inner')
combined.head()


# In[20]:


combined.boxplot(['Aroma'], by= ['Cluster'])


# In[27]:


# Create a scatterplot of df_coffee
combined.hvplot.scatter(x="altitude_low_meters", y="Flavor", by="Cluster")


# In[30]:


# Create a scatterplot of df_coffee
combined.hvplot.scatter(x="Moisture", y="Flavor", by="Cluster")


# In[31]:


# Create a scatterplot of df_coffee
combined.hvplot.scatter(x="Body", y="Flavor", by="Cluster")


# In[34]:


# Create a scatterplot of df_coffee
combined.hvplot.scatter(x="altitude_mean_meters", y= "Flavor", by="Cluster")


# In[ ]:




