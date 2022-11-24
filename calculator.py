import streamlit as st

st.sidebar.title("Applications")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Nutrition Advisor','BMI Calculator','Basic Calculator')
)

if user_menu == 'Basic Calculator':
    st.title("Calculator")
    
    first = st.text_input("Enter your first number", "0")
    second = st.text_input("Enter your second number", "0")
    
    operation  = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    
    if st.button("Perform Operation:"):
        if operation == "Addition":
            result = float(first) + float(second)
            st.success(result)
            
        elif operation == "Subtraction":
            result = float(first) - float(second)
            st.success(result)        
        
        elif operation == "Multiplication":
            result = float(first) * float(second)
            st.success(result)
            
        elif operation == "Division":
            result = float(first)/ float(second)
            st.success(result)        
      
if user_menu == "BMI Calculator":
    st.title("BMI Calculator")
    st.write("A BMI score is a rule of thumb measurement for healthy weights. It does not take into account gender, frame or muscle mass so be aware that results are not always perfectly indicative of health.")
    
    firsts = st.text_input("Enter your weight in kg", "80")
    seconds = st.text_input("Enter your height in cm", "180")
    bmi = round(int(firsts)/(int(seconds)/100)**2,1)
    
    if bmi>25 or bmi <18:
        st.success(('Your BMI is:', + bmi, 'which is outside of the healthy range 18-25'))
    else:
        st.success(('Your BMI is:', + bmi, 'which is within the healthy range 18-25'))
        
if user_menu == "Nutrition Advisor":
    st.title("Nutrition Advisor")
    st.write("This section will look at your daily calorie usage to guide you to your goals. Please enter a few metrics below:")  
    genders = st.selectbox("Are you male or female?",["Male","Female"])
    firsts = st.text_input("Enter your weight in kg", "80")
    seconds = st.text_input("Enter your height in cm", "180")
    age = st.text_input("Enter your age", "45")
    
    st.subheader("Your resting calorie burn is:")
    
    if genders == "Male":
        cal = round(88 + (14*float(firsts)) + (4.799*float(seconds)) - (5.677*(float(age))))
        st.success(cal)
    elif genders == "Female":
        cal =  round(447.593 + (11*float(firsts)) + (3.098*float(seconds)) - (4.330*(float(age))))   
        st.success(cal)    
    
    st.write("Now, taking into account your daily activity with how many steps you do a day:")
    step = st.selectbox("Do you know how many steps you take a day roughly?", ["Yes", "No"])
    if step == "No":
        active  = st.selectbox("Daily, how active are you?", ["Low activity (Under 2000 steps)", "British average (2000-5000 steps)", "Active (5000-10000 steps)", "Very Active (10000-15000 steps)"])
        if active == "Low activity (Under 2000 steps)":
            steps = 1500
        elif active == "British average (2000-5000 steps)":
            steps = 4000
        elif active == "Active (5000-10000 steps)":
                steps = 7500
        elif active == "Very Active (10000-15000 steps)":
                    steps = 12500
    elif step == "Yes":
        steps = st.text_input("How many steps do you take on an average day?", "4000")
    
    
                
    calextra = ((float(firsts) *2.2)/3) *(int(steps)/1000)
    total = calextra+cal
    st.subheader("You burned an extra:")
    st.success((round(calextra)))
    st.subheader("Your total daily calorie burn is:")
    st.success((round(calextra+cal)))
    
    goal = st.selectbox("What is your goal?",["To gain muscle","To lose fat"])
    
    st.subheader("To sustainably move towards your goal you should aim to eat this many calories a day:")
    
    if goal == "To lose fat":
        st.success(round((round(total - 500,-2))))
    elif goal == "To gain muscle":
        st.success(round((round(total + 300,-2))))
        
        
        
    
    
    
    
    
         