
# Global variables used all throughout the code
# ============================================


# For ploting
import pandas as pd
df = pd.read_csv('data/trabajo1.csv')

categorical_columns = ["department", "region", "education",
                       "gender", "recruitment_channel", "is_promoted"]
quantitative_columns = ["no_of_trainings", "age", "previous_year_rating",
                        "length_of_service", "awards_won", "avg_training_score"]
dict_of_column_names = {
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
    "avg_training_score": "Average Training Score"
}

# Colors for text and titles
colors = {
    "text": "#303234",
    "subtitles": "#212223",
    "titles": "#1C77AF"
}


# 0. Explaining the objective and description
# ============================================
markdown_dashboard_title = "# Studying Business Promotion Patterns"

markdown_part_0_title = "## Describing the problem - How to empower employees towards better carreer decisions?"

markdown_part_0_text = """
The aim of this project is to provide feedback on promotion patterns within our client's business. With this information, a tool will be created
to empower employees and assist them in making more impactful career decisions. This study is will provide an exploratory data analysisanalysis (EDA) showing current patterns, a model for promotion prediction and a customizable 
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
