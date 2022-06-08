#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.preprocessing import normalize
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.decomposition import PCA
from path import Path
from matplotlib import pyplot as plt
import plotly.express as px
import hvplot.pandas


# In[2]:


# Load the crypto_data.csv dataset.
file_path = "Capstone/data/arabica_cleaned_data.csv""
coffee_df = pd.read_csv(file_path, index_col=0)
coffee_df


# In[3]:


coffee_df.drop(columns=['Farm.Name', 'Lot.Number', 'Mill', 'ICO.Number', 'Company'], inplace=True)
coffee_df.head()


# In[4]:


coffee_df.drop(columns=['Producer', 'Bag.Weight', 'In.Country.Partner', 'Harvest.Year'], inplace=True)
coffee_df.head()


# In[5]:


coffee_df.drop(columns=['Owner.1', 'Variety', 'Processing.Method', 'Color'], inplace=True)
coffee_df.head()


# In[6]:


coffee_df.drop(columns=['Number.of.Bags', 'Grading.Date', 'Category.Two.Defects', 'Expiration', 'Certification.Address'], inplace=True)
coffee_df.head()


# In[7]:


coffee_df.drop(columns=['Category.One.Defects', 'Quakers', 'Certification.Body', 'Certification.Contact'], inplace=True)
coffee_df.head()


# In[8]:


coffee_df


# In[9]:


coffee_df['Region'].value_counts().head(20)


# In[10]:


coffee_df['Region'] = coffee_df['Region'].apply(lambda x: x if x in ('huila', 'oriente', 'south of minas', 'kona', 'veracruz', 'tarrazu') else 'Other')


# In[11]:


coffee_df


# In[12]:


coffee_df['Country.of.Origin'].value_counts().head(20)


# In[13]:


coffee_df['Country.of.Origin'] = coffee_df['Country.of.Origin'].apply(lambda x: x if x in ('Mexico', 'Colombia', 'Guatemala', 'Brazil', 'Taiwan', 'United States (Hawaii)') else 'Other')


# In[14]:


X = coffee_df [['Region', 'Country.of.Origin', 'Aroma', 'Flavor', 'Acidity']].copy()
X['Region'] = LabelEncoder().fit_transform(X['Region'])
X['Country.of.Origin'] = LabelEncoder().fit_transform(X['Country.of.Origin'])
X = X.dropna()
X.head()


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


coffee_scaled = StandardScaler().fit_transform(X)
print(coffee_scaled[0:5])


# In[21]:


# Using PCA to reduce dimension to 
pca = PCA(n_components=3)
Coffee_pca = pca.fit_transform(coffee_scaled)
Coffee_pca


# In[22]:


# Create a DataFrame with the three principal components.
pcs_df = pd.DataFrame(Coffee_pca, columns= ['PC 1', 'PC 2', 'PC 3'], index =coffee_df.index)
pcs_df.head(10)


# In[23]:


# 88% of data covered
pca.explained_variance_ratio_


# In[24]:


# Find the best value for K
inertia = []
k = list(range(1, 11))

# Calculate the inertia for the range of K values
for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(Coffee_pca)
    inertia.append(km.inertia_)

# Create the elbow curve
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)
df_elbow.hvplot.line(x="k", y="inertia", xticks=k, title="Elbow Curve")


# In[25]:


# Initialize the K-means model
model = KMeans(n_clusters=3, random_state=0)

# Fit the model
model.fit(Coffee_pca)

# Predict clusters
predictions = model.predict(Coffee_pca)

# Add the predicted class columns
pcs_df["class"] = model.labels_
pcs_df.head()


# In[26]:


import plotly.express as px
fig = px.scatter_3d(
    pcs_df,
    x="PC 1",
    y="PC 2",
    z="PC 3",
    color='class',
    symbol='class',
    width=800,
)
fig.update_layout(legend=dict(x=0,y=1))
fig.show()


# In[ ]:




