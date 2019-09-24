## Fundamentals Programming, HW2
import requests
import tarfile
path_to_data_directory = '/Users/student/Documents/fundamentals/programming/data/'

r = requests.get('http://www.rbvi.ucsf.edu/Outreach/PythonBootCamp2019/modules/oop/top500H.tgz')

with open(path_to_data_directory + 'data_day2.tgz','wb') as f:
    f.write(r.content)
    
t = tarfile.open(path_to_data_directory + 'data_day2.tgz')
k = sorted({x.split('/')[1][0:4] for x in t.getnames()[1:]})

print('Number of Unique files ' + str(len(k)))
print('PDB IDs ' + ', '.join(k))


## Oneliner
import io, requests,tarfile; print('PBDIDs '+', '.join(sorted({x.split('/')[1][0:4] for x in tarfile.open(fileobj=io.BytesIO(requests.get('http://www.rbvi.ucsf.edu/Outreach/PythonBootCamp2019/modules/oop/top500H.tgz').content)).getnames()[1:]})))
