
from joblib import dump, load

grid_search_clf = load('data/resultados_gridsearch_modelos.joblib')


def calcular_si_hay_campos_vacios(no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating):

    lista_campos = [no_of_trainings, age, length_of_service, training_score,
                    award, gender, department, education, recruitment, previous_year_rating]
    hay_campos_vacios = False
    for elemento in lista_campos:
        if elemento is None:
            hay_campos_vacios = True

    return hay_campos_vacios


def calculo_validacion_incorrecta(no_of_trainings, age, length_of_service, training_score):

    frase_error = ""
    validacion_incorrecta = True
    if no_of_trainings < 0:
        frase_error = "The number of trainings cannot be less than zero"
    elif age < 0:
        frase_error = "The age of the employee cannot be less than zero"
    elif length_of_service < 0:
        frase_error = "The length of service cannot be less than zero"
    elif length_of_service > age-18:
        frase_error = "The length of service must be at least 18 years lower than age"
    elif training_score < 0 or training_score > 100:
        frase_error = "Training score must be between 0 and 100 "
    else:
        # Si no ha entrado en ninguna de las anteriores es que la validación es correcta
        validacion_incorrecta = False

    return validacion_incorrecta, frase_error


def mostrar_variables_del_modelo(no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating):

    texto = """The selected profile is: a {0} employee that is {1} years old and has been working at the firm for {2} years.
    The employee has a {3} level of education and was recruited via the {4} channel.
     They currently work in the {5} department and have done {6} trainings with an average training score of {7}.
     They have{8}received awards and last year they had a rating of {9}"
    """.format(gender, age, length_of_service, education, recruitment, department, no_of_trainings, training_score, award, previous_year_rating)

    return texto
