#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask


# In[2]:


pip install Flask_SQLAlchemy


# In[3]:


from flask import Flask


# In[4]:


from flask_sqlalchemy import SQLAlchemy


# In[5]:


# the below code is for flask 
"""
app = Flask("db1")

@app.route("/search")
def search():
    
    return("This is a search page")


@app.route("/name")
def name():
    return(" My Name IS Siddhartha")
    
    
"""
print("Hekllo")


# In[6]:


app = Flask("iiec")


# In[7]:


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data3.sqlite'


# In[8]:


db = SQLAlchemy(app)


# In[9]:


print(db)


# In[10]:


# first we need to create a schema for the database
# for this we can use class and create the structure of the database


# In[11]:


class IIEC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    remarks = db.Column(db.Text)
    
    def __init__(self, name, age , remarks):
        self.name = name
        self.age = age
        self.remarks = remarks


# In[12]:


#  Here we have created  A schema for the database not its time to tell the python code to create a database based on the above 
#  model
db.create_all()


# # Now that we have created our own databse no we need to learn how to manipulate it

# ADDING DATA TO A DATABASE

# In[13]:


tom = IIEC("TOM", 22,"GOOD")      # <-- now we have an object of name tom with their details
sid = IIEC("sid", 20,"V.GOOD")
abc = IIEC("abc", 22,"ok")
cde = IIEC("cde", 24,"Bad")


# In[14]:


db.session.add(tom)
db.session.add(sid)
db.session.add(abc)
db.session.add(cde)


# In[15]:


db.session.commit()


# -->> READING A QUERY

# In[16]:


read = IIEC.query.get(3)    # <--- this query will give us the 2nd row data
print(read)


# In[17]:


print(read.name,  read.age , read.remarks)


# In[18]:


# To print all records

read_all = IIEC.query.all()
print(read_all)


# In[19]:


# this function will help us to print the array data
def print_array(arr):
    for i in arr:
        print( i.name, i.age, i.remarks)

def printALL():
    read_all = IIEC.query.all()
    print_array(read_all)


#  ---->> to get specific/filtered data

# In[20]:


print_array(read_all)


# In[21]:


read_filtered = IIEC.query.filter_by(remarks = "ok")
print_array(read_filtered)
print()
read_filtered = IIEC.query.filter_by(remarks = "GOOD")
print_array(read_filtered)


# In[22]:


read_filtered = IIEC.query.filter_by(age = 22)
print_array(read_filtered)


#  ---->> TO UPDATE A ROW/COLUMN

# In[23]:


#r_update = IIEC.query.filter_by(remarks = "ok")
r_update = IIEC.query.get(1)
r_update.remarks  = "BAD"
print(r_update.remarks)


# In[24]:


db.session.add(r_update)
db.session.commit()


# In[25]:


printALL()


#     ___>DELETING A QUERY

# In[26]:


r_delete = IIEC.query.get(1)
db.session.delete(r_delete)


# In[27]:


printALL()


# In[28]:


db.session.commit()


# In[29]:


printALL()


# In[ ]:





# In[ ]:




