# Esta función añade características a los layouts para que tengan todos algunas características comunes y fáciles de cambiar
from variables import *


def layout_additions(fig):

    fig.update_layout(paper_bgcolor="#FAF9F9")
    fig.update_layout(legend=dict(font=dict(size=legend_size)))

    return fig


def layout_additions_for_employee_profile_plots(fig):
    fig.update_layout(paper_bgcolor="#F3F3F3")
    fig.update_layout(legend=dict(font=dict(size=18)))

    return fig


def generate_user_profile(no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating, modelo_ok):

    if modelo_ok == True:
        USER_PROFILE = {"department": department, "education": education, "gender": gender, "recruitment_channel": recruitment, "awards_won": award,
                        "no_of_trainings": no_of_trainings, "age": age, "previous_year_rating": previous_year_rating, "length_of_service": length_of_service, "avg_training_score": training_score}
