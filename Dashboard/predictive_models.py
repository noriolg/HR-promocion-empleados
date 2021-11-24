from variables import *
from joblib import dump, load
import numpy as np
import plotly.graph_objects as go
from utils import *

grid_search_clf = load('data/resultados_gridsearch_modelos.joblib')
sc = load('data/standard_scaler_modelos.joblib')
encoder_department = load('data/encoder_variable_department.joblib')
encoder_education = load('data/encoder_variable_education.joblib')
encoder_gender = load('data/encoder_variable_gender.joblib')
encoder_recruitment_channel = load(
    'data/encoder_variable_recruitment_channel.joblib')


# FUNCIONES PARA USER PROFILE GENERATOR
# =======================================


def generate_user_text(submit_button_value, no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating):
    '''Generates the text that the user sees after creating an employee profile. It also validates user input in order to decide the returned text

        Parameters:
                submit_button_value (int): number of times the sumbit button has been clicked. Generated automatically by program. Used to determine default text when value is zero
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

        Returns:
                texto (string): text to display in html div to give feedback to user regarding the inputted employee profile
                modelo_ok (boolean): if employee profile is valid, it will return True. If not, False will be returned. This is used in order to recalculate promotion predictions and employee comparison charts
    '''

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
    '''Checks if there are any empy values in the provided variables. Returns True if there are any empty variables

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


        Returns:
                hay_campos_vacios (boolean): True if any of the received fields is empty. False if all of them have values
    '''

    lista_campos = [no_of_trainings, age, length_of_service, training_score,
                    award, gender, department, education, recruitment, previous_year_rating]
    hay_campos_vacios = False
    for elemento in lista_campos:
        if elemento is None:
            hay_campos_vacios = True

    return hay_campos_vacios


def calculo_validacion_incorrecta(no_of_trainings, age, length_of_service, training_score):
    '''Calculates whether there are any incorrect fields that have been intoduced by the user. The only possibility is with numerics, because categorical variables have been chosen from dropdown (or radiobutton/slider)

        Parameters:
                no_of_trainings (int): value introduced by user. A characteristic of employee profile. 
                age (int): value introduced by user. A characteristic of employee profile. 
                length_of_service (int): value introduced by user. A characteristic of employee profile. 
                training_score (float): value introduced by user. A characteristic of employee profile. 

        Returns:
                validacion_incorrecta (boolean): True if any field is not valid. False if all fields are validated and ok
                frase_error (string): String with error description to show to user
    '''

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
    '''Constructs the text to show user when the employee profile has been succesfully created

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

        Returns:
                text (string): String with profile description to show user
    '''

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


# FUNCIONES PARA TAB 1
# =======================================

def generate_promotion_prediction(no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating):
    '''Predicts if the employee will be promoted or not using the pre-trained model. Sets PERCENTAJE_EMPLOYEE_PROMOTION which is later used by the promotion lever

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

        Returns:
                prediction_text (string): text to show user answering whether a promotion has been predicted or not
    '''

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

    # We will use the probability of promoting as a "score"
    score = grid_search_clf.predict_proba(scaled_entry)[0][1]
    score_float = round(float(score), 2)
    setPorcentajePromocionEmpleado(score)

    if prediction == 1:
        prediction_text = "## A Promotion Is Likely to Occur"
        # prediction_text = "## The employee will be promoted with probability {0}%".format(
        # round(probability_of_prediction_float*100, 2))
    else:
        prediction_text = "## No Promotion Is Predicted"
        # prediction_text = "The employee will not be promoted with probability {0}%".format(
        #    round(probability_of_prediction_float*100, 2))
    # prediction, probability_of_prediction_float
    return prediction_text


def plot_promotion_lever(porcentaje_promocion_empleado):
    '''Creates a lever plot showing the employees promotion status

        Parameters:
                porcentaje_promocion_empleado (float):  probability of being classified as a "1" (promoting)

        Returns:
                fig (go.Figure): figure with the described plot showing the employee promotion probability
    '''

    #print("In Plot promotion: {0}".format(porcentaje_promocion_empleado))
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=porcentaje_promocion_empleado,
        mode="gauge+number+delta",
        title={'text': "Promotion Lever"},
        delta={'reference': 0.5, 'increasing': {
            'color': "mediumspringgreen"}, 'decreasing': {'color': "salmon"}},
        gauge={'axis': {'range': [None, 1]},
               'bar': {'color': "steelblue"},
               'steps': [
            {'range': [0, 0.5], 'color': "lightgray"},
            {'range': [0.5, 1], 'color': "gray"}],
            'threshold': {'line': {'color': "salmon", 'width': 4}, 'thickness': 0.75, 'value': 0.5}}))
    fig = layout_additions_for_employee_profile_plots(fig)
    return fig


# FUNCIONES PARA TAB 2
# =======================================


def plot_employee_profile_categorical_promotion_percentages(employee_profile):
    '''Creates a bar plot showing the promotion percentages in each of the individual employee categories

        Parameters:
                employee_profile (dict):  structure with all the employee information and model variables

        Returns:
                fig (go.Figure): figure with the described plot showing promotion percentage in each of the employee's categorical variables
    '''

    # Primero generamos los nombres de las columnas particulares para el perfil de empleado introducido
    personalized_bar_names_for_employee = []
    for clave, valor in employee_profile.items():
        try:
            nombre = dict_of_column_names[clave] + " = " + \
                str(dict_of_categorical_variables[valor])
        except:
            nombre = dict_of_column_names[clave] + " = "+str(valor)
        personalized_bar_names_for_employee.append(nombre)

    # Ahora conseguimos los porcentajes de promoción para las características personales del empleado
    employee_profile_categorical_columns = [
        "department", "education", "gender", "recruitment_channel", "awards_won"]
    percentages = {}
    for column_name in employee_profile_categorical_columns:
        # Array with number of non promoted and promoted
        promoted_non_promoted = list(df_model[(
            df_model[column_name] == employee_profile[column_name])]["is_promoted"].value_counts())
        print(promoted_non_promoted)
        percentage_promoted = promoted_non_promoted[1] / \
            sum(promoted_non_promoted)

        # We include it in the percentages dictionary
        percentages[column_name] = percentage_promoted

    # Ahora hacemos el plot
    trace = go.Bar(x=personalized_bar_names_for_employee,
                   y=list(percentages.values()),
                   name="Promoted",
                   marker_color="mediumspringgreen",
                   text=["{0}%".format(round(value*100, 1))
                         for value in list(percentages.values())],
                   textposition="auto",
                   textangle=0,
                   textfont_size=20,
                   textfont_color="black",
                   hovertemplate='% Promoted in employee category'
                   )

    data = [trace]
    layout = go.Layout(title="% Promotions for similar people",
                       xaxis_title="Employee Data", yaxis_title="% of workers promoted")
    fig = go.Figure(data=data, layout=layout)
    fig = layout_additions_for_employee_profile_plots(fig)

    return fig


def plot_employee_profile_quantitative_comparison(employee_profile):
    '''Creates a polar plot showing the employees relative performance against mean promoted, mean non promoted and similar employees

        Parameters:
                employee_profile (dict):  structure with all the employee information and model variables

        Returns:
                fig (go.Figure): figure with the described plot showing employee position agains other categories
    '''

    # Creamos las Categorias
    categories = [dict_of_column_names[column_name]
                  for column_name in quantitative_columns]

    # Conseguimos la media de empleados con su mismo perfil de variables categoricas
    df_similar_people = df_model[(df_model["department"] == employee_profile["department"]) &
                                 (df_model["education"] == employee_profile["education"]) &
                                 (df_model["gender"] == employee_profile["gender"]) &
                                 (df_model["recruitment_channel"] == employee_profile["recruitment_channel"]) &
                                 (df_model["awards_won"] ==
                                  employee_profile["awards_won"])
                                 ].loc[:, quantitative_columns]
    means_similar_people = [np.mean(df_similar_people[quantitative_column].values)
                            for quantitative_column in quantitative_columns]

    # Los normalizamos
    means_similiar_people_normalized = normalize_quantitative_employee_entries(
        means_similar_people)

    # Obtenemos los datos numéricos del empleado
    employee_numeric_data = [employee_profile[column_name]
                             for column_name in quantitative_columns]

    # Los normalizamos
    employee_numeric_data_normalized = normalize_quantitative_employee_entries(
        employee_numeric_data)

    trace0 = go.Scatterpolar(
        r=means_promoted_normalized,
        theta=categories,
        fill="toself",
        name="Promoted",
        marker_color="mediumspringgreen",
        opacity=0.6
    )

    trace1 = go.Scatterpolar(
        r=means_non_promoted_normalized,
        theta=categories,
        fill="toself",
        name="Non Promoted",
        marker_color="salmon",
        opacity=0.6
    )

    trace2 = go.Scatterpolar(
        r=means_similiar_people_normalized,
        theta=categories,
        fill="toself",
        name="Similar employees",
        marker_color="yellow",
        opacity=0.4
    )

    trace3 = go.Scatterpolar(
        r=employee_numeric_data_normalized,
        theta=categories,
        fill="toself",
        name="Employee",
        marker_color="steelblue",
        opacity=0.6
    )

    data = [trace0, trace1, trace2, trace3]
    layout = go.Layout(title="Comparison against similar people and overall promotions",
                       polar=dict(
                           radialaxis=dict(
                               visible=True,
                               range=[0, 1]
                           )),
                       showlegend=True)

    fig = go.Figure(data=data, layout=layout)
    fig = layout_additions_for_employee_profile_plots(fig)
    return fig


def normalize_quantitative_employee_entries(employee_quantitative_variables):
    '''Normalizes the values of the employee to show them correctly in the ploar plot

        Parameters:
                employee_quantitative_variables (array):  ordered list with all information regarding employee quantitative variables to be normalized

        Returns:
                normalized_employee_quantitative_variables (array): list with all variables normalized
    '''

    # Se deja hardcodeado esto. Algunos mínimos cambian para que quede mejor el radar chart
    trainings_nomralized = normalize_max_min(
        employee_quantitative_variables[0], 10, 0)  # Max 10, min_real 1
    age_normalized = normalize_max_min(
        employee_quantitative_variables[1], 60, 18)  # Max 60, min_real 20
    prev_year_rating_normalized = normalize_max_min(
        employee_quantitative_variables[2], 5, 0)  # Max 5, min_real 1
    length_of_service_normalized = normalize_max_min(
        employee_quantitative_variables[3], 40, 0)  # Max 37, min_real 1
    avg_training_score_normalized = normalize_max_min(
        employee_quantitative_variables[4], 100, 0)  # Max 99, min_real 39

    normalized_employee_quantitative_variables = [trainings_nomralized, age_normalized,
                                                  prev_year_rating_normalized, length_of_service_normalized, avg_training_score_normalized]

    return normalized_employee_quantitative_variables


def normalize_max_min(x, maximo, minimo):
    '''Normalization function (maxmin nomralization)

        Parameters:
                x (float):  value to normalize
                maximo (float): maximum value for normalization
                minimo (float): minimim value for normalization

        Returns:
                normalized_x (float): nomralized value
    '''

    normalized_x = (x - minimo)/(maximo-minimo)

    return normalized_x
