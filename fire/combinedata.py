import os
import pandas as pd
import numpy as np

# T-30 Update to work with input/output folders
path = "./fire/data/"

for x in range(10):
    data = np.array([["lat", "lon", "bright"]])
    # for y in range(len(os.listdir(path+str(2012+x)+"/"))):
    #    temp = pd.read_csv(path+str(2012+x)+"/"+os.listdir(path+str(2012+x)+"/")[y]).to_numpy()
    year = path+str(2012+x)+"/"
    for y in os.listdir(year):
        temp = pd.read_csv(year+y).to_numpy()
        temp = temp[np.where(temp[:, 9] == 'h')][:, :3]
        data = np.append(data, temp, axis=0)
    print(data)
    np.savetxt(path+"data_"+str(2012+x)+".csv", data, fmt='%s', delimiter=",")

########################################

# thing = []
# for index, row in data.iterrows():
#     if row['confidence'] == "h":
#         thing.append(index)

# newdata=np.array(data)
# print(newdata[thing])
# x = np.array([0,1,2,4789,4,5,6,7,8,9])

########################################

#print(x[[3, 5, 6]])
