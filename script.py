#!/usr/bin/env python
# coding: utf-8

# In[5]:


#! pip install --upgrade google-api-python-client


# In[6]:


#! pip install --upgrade google-api-python-client oauth2client


# In[ ]:





# In[7]:


from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.file import Storage
import httplib2


# In[26]:




SERVICE_NAME = "youtubereporting"
VERSION = 'v1'
SCOPE = 'https://www.googleapis.com/auth/yt-analytics.readonly'
CLIENT_SECRETS_FILE = "client_secrets.json"  # Presuming you made this and in dir w/ it
flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPE, message=' f off ')

# 
credentials_file = 'Capstone-OAuth2.json' # e.g., projectName-oauth2.json
storage = Storage(credentials_file) 
credentials = storage.get()   # Returns None if the file doesn't exist
if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage)  # This creates the credentials_file

get_ipython().run_line_magic('tb', '')


# In[18]:


# build the reporting API
#reporting_api = build(SERVICE_NAME,  VERSION,  http=credentials.authorize(httplib2.Http()))


# In[14]:


# List Available Reports
#reporting_api.reportTypes().list().execute()


# In[15]:


# List Available Reports
#contentId = 'sanghoon1990'  # Pro Tip: Use your own content owner ID!
#reporting_api.reportTypes().list(onBehalfOfContentOwner=contentId).execute()


# In[ ]:




