import pandas as pd

# Global variables used all throughout the code
# ============================================


# Dataframes
# =============


df = pd.read_csv('data/trabajo1.csv')
df_raw = df.copy()

# We generate a dataset with filled nans for plotting in EDA step
df["education"].fillna(value="NA", inplace=True)

# The dataset with treated nulls  for the model buiding
df_model = pd.read_pickle('data/df_treated_nulls.pkl')

# A dataset with department-specific information
df_department = pd.read_pickle('data/datos_departamentos.pkl')

# A dataset with age and service-lengths related to promotions
df_ages_service_lengths = pd.read_pickle('data/datos_ages_service_lengths.pkl')


# Other values
# =============

# Lists and dictionaries for easier access and formating
categorical_columns = ["department", "region", "education",
                       "gender", "recruitment_channel", "awards_won", "is_promoted"]
quantitative_columns = ["no_of_trainings", "age", "previous_year_rating",
                        "length_of_service", "avg_training_score"]
dict_of_column_names = {
    "employee_id": "Employee ID",
    "department": "Department",
    "region": "Region",
    "education": "Education",
    "gender": "Gender",
    "recruitment_channel": "Recruitment Channel",
    "is_promoted": "Is Promoted",
    "no_of_trainings": "Number of tranings",
    "age": "Age",
    "previous_year_rating": "Previous Year Rating",
    "length_of_service": "Length of Service",
    "awards_won": "Awards Won",
    "avg_training_score": "Average Training Score",
    "is_promoted": "Is Promoted"
}

dict_of_recruiting_channels = {
    "sourcing": "Sourcing",
    "other": "Other",
    "referred": "Referred"
}

dict_of_categorical_variables = {



}


# Colors for text and titles
colors = {
    "text": "#303234",
    "subtitles": "#212223",
    "titles": "#1C77AF"
}


legend_size = 20

# 0. Explaining the objective and description
# ============================================
markdown_dashboard_title = "# Studying Business Promotion Patterns"

markdown_part_0_title = "## Describing the problem - How to empower employees towards better carreer decisions?"

markdown_part_0_text = """
The aim of this project is to provide feedback on promotion patterns within our client's business. With this information, a tool will be created
to empower employees and assist them in making more impactful career decisions. This study is will provide an exploratory data analysis (EDA) showing current patterns, a model for promotion prediction and a customizable 
tool to suggest actions to employees.

This dashboard is organized with the following structure:

1. Data description - Showing current employee patterns
2. Key variables - How are promotions granted?
3. Model development - Can we predict promotions?
4. Employee tool - What can I do as an individual employee? 
"""

# 1. Data description - Showing current employee patterns
# ====================================================

markdown_part_1_title = "## 1. Data description - Showing current employee patterns"

markdown_part_1_text = """
This is the data table with all the employee information and relevant columns. IDs have been removed for anonymity.
"""

options_categorical_variables = [dict(
    label=dict_of_column_names[variable], value=variable) for variable in categorical_columns]


options_quantitative_variables = [dict(
    label=dict_of_column_names[variable], value=variable) for variable in quantitative_columns]


# 2. Key variables - How are promotions granted?
# ====================================================
markdown_part_2_title = "## 2. Key variables - How are promotions granted?"

markdown_part_2_text = """
In this second part of the analysis, we will study the promotions granted based on each different variable. Afterwards, we will
analyze several key relationships that have been found within the data.
"""


# 3. Model development - Can we predict promotions?
# ====================================================
markdown_part_3_title = "## 3. Model development - Can we predict promotions?"

markdown_part_3_text = """

"""


# 4. Employee tool - What can I do as an individual employee?
# ====================================================
markdown_part_4_title = "## 4. Employee tool - What can I do as an individual employee? "

markdown_part_4_text = """

"""

# Big div containing the components
width_div_components_for_employee_tool = "300px"
# Component (pickers and others)
width_input_components_for_employee_tool = "170px"


# Department options
department_options = [dict(label=department_name, value=department_name)
                      for department_name in df["department"].unique()]


education_options = [dict(label=education_level, value=education_level)
                     for education_level in df_raw["education"].dropna().unique()]  # Se pone raw porque no queremos que aparezca "NA" como opción y df tiene los nan como "NA"


recruitment_options = [dict(label=dict_of_recruiting_channels[channel], value=channel)
                       for channel in df["recruitment_channel"].unique()]
