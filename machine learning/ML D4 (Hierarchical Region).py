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


X = coffee_df [['Region', 'Aroma', 'Flavor', 'Aftertaste', 'Acidity']].copy()
X['Region'] = LabelEncoder().fit_transform(X['Region'])
X = X.dropna()
X.head()


# In[13]:


normalized = normalize(X)


# In[14]:


mergings = linkage(normalized, method ='ward')


# In[15]:


plt.figure(figsize=(20,8))

dendrogram(mergings, 
          leaf_rotation=90,
          leaf_font_size=5)

plt.show()


# In[17]:


cluster = AgglomerativeClustering(n_clusters=2,
                                 affinity = 'euclidean',
                                 linkage = 'ward')
labels = cluster.fit_predict(X)


# In[18]:


labels


# In[21]:


import plotly.express as px
fig = px.scatter_3d(
    X,
    x="Region",
    y="Aroma",
    z="Flavor",
    width=800,
)
fig.update_layout(legend=dict(x=0,y=1))
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




