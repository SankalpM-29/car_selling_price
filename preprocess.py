
from sklearn.preprocessing import OneHotEncoder
import numpy as np

fuel = ['Diesel', 'Petrol', 'LPG', 'CNG']
seller_type = ['Individual', 'Dealer', 'Trustmark Dealer']
transmission = ['Manual', 'Automatic']
owner = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car']


enc1 = OneHotEncoder(handle_unknown='ignore')
enc1.fit(np.array(fuel).reshape(-1,1))

enc2 = OneHotEncoder(handle_unknown='ignore')
enc2.fit(np.array(seller_type).reshape(-1,1))

enc3 = OneHotEncoder(handle_unknown='ignore')
enc3.fit(np.array(transmission).reshape(-1,1))

enc4 = OneHotEncoder(handle_unknown='ignore')
enc4.fit(np.array(owner).reshape(-1,1))



def get_input(values):
    a1 = enc1.transform([[values[1]]]).toarray()
    a2 = enc2.transform([[values[2]]]).toarray()
    a3 = enc3.transform([[values[3]]]).toarray()
    a4 = enc4.transform([[values[4]]]).toarray()

    array1 = np.append(a1, a2)
    array2 = np.append(array1, a3)
    array3 = np.append(array2, a4)
    last_five = values[5:]
    last_five.insert(0, values[0])
    final_array = np.append(array3, np.array(last_five).astype('float'))
    return final_array.reshape(1,-1)
