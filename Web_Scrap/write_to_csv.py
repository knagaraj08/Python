import pandas as pd
from excersize import final_list_states,population_final
df = pd.DataFrame()

df['States'] = final_list_states
df['Population'] = population_final

# print(df)
df.to_csv("US_states_Population.csv")