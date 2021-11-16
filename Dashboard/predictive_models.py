from variables import *
from joblib import dump, load
import numpy as np

grid_search_clf = load('data/resultados_gridsearch_modelos.joblib')
sc = load('data/standard_scaler_modelos.joblib')
encoder_department = load('data/encoder_variable_department.joblib')
encoder_education = load('data/encoder_variable_education.joblib')
encoder_gender = load('data/encoder_variable_gender.joblib')
encoder_recruitment_channel = load(
    'data/encoder_variable_recruitment_channel.joblib')


def generate_user_text(submit_button_value, no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating):
    # Primero se calcula si hay campos vacíos
    hay_campos_vacios = calcular_si_hay_campos_vacios(
        no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating)

    # En caso de que no haya campos vacíos, hacemos el cálculo de la validación
    if hay_campos_vacios == False:
        validacion_incorrecta, frase_error = calculo_validacion_incorrecta(
            no_of_trainings, age, length_of_service, training_score)

    # Ahora obtenemos la frase a mostrar por pantalla
    # Además, antes de comenzar, asumimos que el modelo no está ok. Cuando esté ok se correrá la predicción
    modelo_ok = False
    if submit_button_value == 0:
        texto = "No employee profile has been submited to the model yet."
    elif hay_campos_vacios:
        texto = "There is at least one empty field in the employee profile."
    elif validacion_incorrecta:
        texto = "Some employee fields do not make sense: " + frase_error
    else:
        texto = mostrar_variables_del_modelo(no_of_trainings, age, length_of_service, training_score,
                                             award, gender, department, education, recruitment, previous_year_rating)
        # Como todo ha ido bien, damos el ok para que corra la predicción del modelo
        modelo_ok = True  # Se podría haber metido el código aquí, pero por simplificar, dividir y dejarlo ordenado se hace a continuación

    return texto, modelo_ok


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

    if award == 1:
        text_award = " "
    else:
        text_award = " not "

    texto = """The selected profile is: a {0} employee that is {1} years old and has been working at the firm for {2} years.
    The employee has a {3} level of education and was recruited via the {4} channel.
     They currently work in the {5} department and have done {6} trainings with an average training score of {7}.
     They have{8}received awards and last year they had a rating of {9}
    """.format(str.lower(dict_of_categorical_variables[gender]), age, length_of_service, str.lower(dict_of_categorical_variables[education]), str.lower(dict_of_categorical_variables[recruitment]), str.lower(dict_of_categorical_variables[department]), no_of_trainings, training_score, text_award, previous_year_rating)

    return texto


def generate_promotion_prediction(no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating):

    # First, we encode the necessary variables to fit the model as it was generated
    department_encoded = encoder_department.transform([department])
    education_encoded = encoder_education.transform([education])
    gender_encoded = encoder_gender.transform([gender])
    recruitment_encoded = encoder_recruitment_channel.transform([recruitment])

    # We now combine all data into a single array
    encoded_entry = np.concatenate(([no_of_trainings, age, previous_year_rating, length_of_service, award, training_score],
                                   department_encoded.flatten(), education_encoded.flatten(), gender_encoded.flatten(), recruitment_encoded.flatten()))

    # And scale it using the training scaler
    scaled_entry = sc.transform(encoded_entry.reshape(1, -1))

    # And we now predict the outcome
    prediction = grid_search_clf.predict(scaled_entry)
    # Tanto lío de corchetes para poder acceder al dato correcto
    probability_of_prediction = grid_search_clf.predict_proba(scaled_entry)[
        0][prediction]
    probability_of_prediction_float = float(probability_of_prediction)

    if prediction == 1:
        prediction_text = "The employee will be promoted with probability {0}%".format(
            round(probability_of_prediction_float*100, 2))
    else:
        prediction_text = "The employee will not be promoted with probability {0}%".format(
            round(probability_of_prediction_float*100, 2))

    return prediction_text
