from app_data.helper_functions.helper import prepare_descriptions_for_database


path = "../app_data/database/courses_data/manuel_vs_generated_including_descriptions_fixed.csv"

with open(path, 'r', encoding='utf-8') as f:
    data = f.read()

lines = data.split('\n')[1:]


for line in lines:
    line = line.split(',')
    print(prepare_descriptions_for_database(line))
