#!/usr/bin/env python
# coding: utf-8

# # Homeowork 2
# - There is a "tar" archive located at http://www.rbvi.ucsf.edu/Outreach/PythonBootCamp2019/modules/oop/top500H.tgz. The contents of archive is a list of files whose names look like top500H/7rsaH, where they all start with top500H/, followed by a four-letter Protein Data Bank (PDB) code, followed by some capital letters.
#     - These files are the protein chains used to compute the Ramachandran maps (commonly observed protein conformations) that can help highlight unusual (typically poorly solved) structural features.
#     - A single protein structure may contribute multiple chains.
# - Print the PDB codes in sorted order with duplicates removed, followed by the number of unique PDB codes found.

# ### Homework hint

# - Install and use requests to fetch and save the file.
# - Use the tarfile module from the Python standard library to get the list of file names.
# - Extract the PDB codes into a Python set to remove duplicates.
# - Print the PDB codes in sorted order.
# - This exercise is more about finding packages and reading their documentation than clever programming

# Import necessary packages
# tarfile: for handling the .tgz file
# urllib.request: for downloading the file from the internet

# In[1]:


import tarfile
import urllib.request


# download the file from the url and save it to a file in my current directory

# In[2]:


url = 'http://www.rbvi.ucsf.edu/Outreach/PythonBootCamp2019/modules/oop/top500H.tgz'
urllib.request.urlretrieve(url, './top500H.tgz')


# Open the .tgz file and get the names of every file within it
#     use [1:] so I don't get the name of the original .tgz file in my list

# In[3]:


files=tarfile.open("top500H.tgz")
names = files.getnames()[1:]


# Check the how many file names are in the list and print the first 5 to look at the formatting

# In[4]:


print(len(names))
print(names[:5])
for name in range(len(names)):
    names[name] = names[name].split('/')[1][:4]
print(names[:5])


# Covert the list to a set to get rid of duplicates and check the length of the set, which should give us the number of unique values in the list
#
# It appears that there are no duplicate values

# In[5]:


names_set = set(names)
len(names_set)


# Sort the set

# In[6]:


sorted_names = sorted(names_set)


# Print the name of all of the pdb codes from file names in the original .tgz file in sorted order

# In[7]:


for name in sorted_names:
    print(name)
