
import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs
def prediction(Gender, Married, ApplicantIncome, CoapplicantIncome, Dependent, LoanAmount, Loan_Amount_Term, Credit_History,Self_Employed,Property_Area,Education):

    # Pre-processing user input
    if Gender == "Male":
        Female = 0
        Male = 1
    else:
        Female = 1
        Male = 0

    if Married == "Unmarried":
        UnMarried = 1
        MarriedStatus = 0
    else:
        UnMarried = 0
        MarriedStatus = 1

    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    if Self_Employed == "Business":
        Employed = 0 
        Business = 1
    else:
        Employed = 1
        Business = 0

    if Property_Area =='Urban':
        Property_Area = 2
    elif Property_Area =='Rural':
        Property_Area = 0
    else:
        Property_Area = 1
     
    if Education == "Graduate":
        Education = 0
    else:
        Education = 1

    LoanAmount = LoanAmount / 1000

    # Making predictions
    prediction = classifier.predict(
        [[Dependent,Education, ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term,Credit_History,Property_Area,  Employed,	Business , UnMarried, MarriedStatus, Female, Male]])
    
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married"))
    Self_Employed = st.selectbox('Self Employed',("Business","Employed"))
    ApplicantIncome = st.number_input("Applicants monthly income")
    CoapplicantIncome = st.number_input("Coapplicant monthly income")
    Dependent = st.number_input("EnterNumber of Dependent")
    LoanAmount = st.number_input("Total loan amount")
    Loan_Amount_Term  = st.number_input("Loan amount Term")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    Property_Area =  st.selectbox('Property_Area',('Urban', 'Rural', 'Semiurban'))
    Education =  st.selectbox('Education',('Graduate', 'Not Graduate'))
    result =""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Gender, Married, ApplicantIncome, CoapplicantIncome, Dependent, LoanAmount, Loan_Amount_Term, Credit_History,Self_Employed,Property_Area,Education)
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)

if __name__=='__main__':
    main()
