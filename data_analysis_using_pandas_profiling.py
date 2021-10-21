import pandas as pd
from pandas_profiling import ProfileReport

# Paths
try:
    path = 'C://Users//krath//PycharmProjects//input_output_files//'
    filename = 'housing_input.csv'
except Exception as ex:
    print("Error while fetching the file")
    exit()

input_file = path + filename
data_frame = pd.read_csv(input_file)
print(data_frame)

#  Generate HTML report
profile_ = ProfileReport(data_frame)
profile_.to_file(output_file=path+'housing_output.html')
