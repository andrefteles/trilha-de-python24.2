# a) Utilize este csv para obter uma representação clara dos dados,
# por meio de gráficos ou outras funcionalidades do Pandas.

# b) Representar, por meio do uso das classes, algo do dia-a-dia de vocês,
# como a Padaria feita anteriormente.


import pandas as pd
import matplotlib.pyplot as plt
import os

column_names = [
'mpg', 'cyl', 'disp', 'hp', 'drat',
'wt', 'qsec', 'vs', 'am', 'gear', 'carb'
]

# Corrects the file path
base_dir = r'C:\Users\andrefelipe\Desktop\for_code_github\trilha_de_python-24.2\data'
file_path = os.path.join(base_dir, 'mt_cars.csv') # Specify the full directory name

data = pd.read_csv(file_path)
# print(data)

data_stats = data.describe() # Summarize key statistics of the dataset
# print(data_stats)

# This code display different types of plots.
# data.plot(kind='hist', y='hp')

# Bloxplot. 
# Adjust the column index index in the list.
# boxplot_image = data_stats.boxplot(column=column_names[5] )

# Bar Plot
# data.groupby('cyl')['mpg'].mean().plot(kind='bar')
# plt.title("Average MPG by Cylinder Count")
# plt.xlabel("Cylinder Count")
# plt.ylabel("Average MPG")

# Box Plot by group
# data.boxplot(column='mpg', by='cyl')
# plt.title("MPG Distribution by Cylinder Count")
# plt.suptitle("")
# plt.xlabel("Cylinder Count")
# plt.ylabel("MPG")

# Histogram for Data Distribution
# data[['mpg', 'hp', 'wt']].hist(bins=10, layout=(2,2), figsize=(10, 8))
# plt.suptitle('Histograms of Selected Variables')

plt.show()
