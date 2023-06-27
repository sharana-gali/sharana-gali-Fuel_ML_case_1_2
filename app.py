
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
    st.image("""data:image/jpeg;base64,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""")

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
