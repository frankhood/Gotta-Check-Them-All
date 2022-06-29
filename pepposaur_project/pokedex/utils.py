import pandas as pd
import math


def euclidean_distance(p,q):
    return  math.dist(p,q)

def df_normalizer(df):
    normalized_df=(df-df.min())/(df.max()-df.min())
    return normalized_df

def df_get_k_neighbors(dataset, element, k=5):
    COLUMNS= ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    df_pokemon_values=dataset[COLUMNS]
    pokemon_index=df_pokemon_values.index.max()+1
    pokemon=pd.Series(element,COLUMNS,name=pokemon_index)
    complete_dataset = pd.concat([df_pokemon_values, pd.DataFrame([pokemon,])])
    normalized_dataset = df_normalizer(complete_dataset)
    normalized_element = normalized_dataset.loc[pokemon_index]
    normalized_dataset = normalized_dataset[normalized_dataset.index!=pokemon_index]
    normalized_dataset['distance'] = normalized_dataset.apply(lambda row: euclidean_distance(row, normalized_element),axis=1)
    normalized_dataset.sort_values('distance',inplace=True)
    return normalized_dataset.head(k)[['distance']]