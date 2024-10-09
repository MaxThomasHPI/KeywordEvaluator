import pandas as pd

path = "../app_data/database/courses_data/manuel_vs_generated_including_descriptions_fixed_en.csv"

data = pd.read_csv(path, encoding='utf-8')

#print(data)

for i, row in data.iterrows():
    if i > 257:
        original = row["description"]
        translation = row["description_en"]

        if type(original) is str and original != translation:
            print(i)
            print(original)
            print('##########################')
            print(translation)
            input()
