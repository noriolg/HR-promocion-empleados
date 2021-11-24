# Esta función añade características a los layouts para que tengan todos algunas características comunes y fáciles de cambiar
from variables import *


def layout_additions(fig):
    '''Adds background color and sets legend fond size for  plots

        Parameters:
                fig (go.Figure):  figure that needs its layout changed

        Returns:
                fig (go.Figure): updated figure
    '''

    fig.update_layout(paper_bgcolor="#FAF9F9")
    fig.update_layout(legend=dict(font=dict(size=legend_size)))

    return fig


def layout_additions_for_employee_profile_plots(fig):
    '''Adds background color and sets legend fond size for  plots. This is special for plots in employee_profile section as they have different characteristics

        Parameters:
                fig (go.Figure):  figure that needs its layout changed

        Returns:
                fig (go.Figure): updated figure
    '''

    fig.update_layout(paper_bgcolor="#F3F3F3")
    fig.update_layout(legend=dict(font=dict(size=18)))

    return fig


def generate_user_profile(no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating, modelo_ok):
    '''Generates a user profile with user data - only if introduced data is ok. This profile is saved into a global variable in variables.py

        Parameters:
                no_of_trainings (int): value introduced by user. A characteristic of employee profile. 
                age (int): value introduced by user. A characteristic of employee profile. 
                length_of_service (int): value introduced by user. A characteristic of employee profile. 
                training_score (float): value introduced by user. A characteristic of employee profile. 
                award (int): value introduced by user. A characteristic of employee profile. 
                gender (string): value introduced by user. A characteristic of employee profile. 
                department (string): value introduced by user. A characteristic of employee profile. 
                education (string): value introduced by user. A characteristic of employee profile. 
                recruitment (string): value introduced by user. A characteristic of employee profile. 
                previous_year_rating (float): value introduced by user. A characteristic of employee profile. 
                modelo_ok (boolean): indicated whether all fields are correct. If they are not correct the user profile is not changed
    '''

    if modelo_ok == True:
        user_profile = {"department": department, "education": education, "gender": gender, "recruitment_channel": recruitment, "awards_won": int(award),
                        "no_of_trainings": no_of_trainings, "age": age, "previous_year_rating": previous_year_rating, "length_of_service": length_of_service, "avg_training_score": training_score}

        setUserProfile(user_profile)
