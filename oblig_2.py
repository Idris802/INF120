# -*- coding: utf-8 -*-


__author__ = "Idris Omar"

__email__ = "mohammed.idris.omar@nmbu.no"



# Del 1
import pandas as pd
import numpy as np


def csv_til_liste(filnavn):
    df = pd.read_csv(open(filnavn, "r"))
    occuList = df.to_numpy().tolist()
    return occuList, df
    

import matplotlib.pyplot as plt

if __name__ == "__main__":
    occuList, df = csv_til_liste('occupancy (4).csv')
    boxplot = df.boxplot(column='Temperature', by='Occupancy')
    plt.suptitle('')
    
    
    
    
# Del 2
def tid_siden_midnatt(liste):
    timer_e_midnatt = []
    minutter_e_midnatt = []
    
    for i in liste:
        
        
        tid = i[1]
        tid_splitted = tid.split(" ")
        tiden = tid_splitted[1]
        tiden_splitted = tiden.split(":")
        tiden2 = [int(i) for i in tiden_splitted]
        timer = tiden2[0]
        min_per_time = tiden2[0] * 60
        minutter = min_per_time + tiden2[1]
        timer_e_midnatt.append(timer)
        minutter_e_midnatt.append(minutter)
    

    return timer_e_midnatt, minutter_e_midnatt
        
if __name__ == "__main__":
    timer_e_midnatt, minutter_e_midnatt = tid_siden_midnatt(occuList)
    verdi, counts = np.unique(timer_e_midnatt, return_counts=True)
    """ De to laveste registrerte tidspunktene er 
    klokken 11 og 14. Der hvor antallet på regisrerte
    er 295.
    """

# Del 3
def hent_kolonner(dataframe, kolonne1, kolonne2, lagPlott=True):
    df_til_array = np.array(dataframe[[kolonne1, kolonne2]])
    plt.clf()
    plt.scatter(df_til_array[:,0], df_til_array[:,1], c=list(range(len(df_til_array))))
    plt.colorbar()
    plt.axis() 
    plt.show()
    print(df_til_array)
    
    
if __name__ == "__main__":
    hent_kolonner(df, 'Humidity', 'CO2')
 
    
    
    
