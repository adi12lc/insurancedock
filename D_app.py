import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("rfc3_class.pkl","rb")
rfc_class=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Index Page"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(InsuredAge, InsuredZipCode, InsuredGender,
       InsuredEducationLevel, InsuredOccupation, InsuredHobbies,
       NetCapital, CustomerLoyaltyPeriod, Policy_Month,
       InsurancePolicyState, Policy_CombinedSingleLimit,
       Policy_Deductible, PolicyAnnualPremium, UmbrellaLimit,
       MonthofIncident, DayofIncident, InsuredRelationship,
       TypeOfIncident, TypeOfCollission, SeverityOfIncident,
       AuthoritiesContacted,IncidentState, IncidentCity, Timeofincident, NumberOfVehicles,
       PropertyDamage, BodilyInjuries, Witnesses, PoliceReport,
       AmountOfTotalClaim, AmountOfInjuryClaim, AmountOfPropertyClaim,
       AmountOfVehicleDamage, VehicleMake, VehicleYOM):
    
   
    prediction=rfc_class.predict([[InsuredAge, InsuredZipCode,  InsuredGender,
       InsuredEducationLevel, InsuredOccupation, InsuredHobbies,
       NetCapital, CustomerLoyaltyPeriod, Policy_Month,
       InsurancePolicyState, Policy_CombinedSingleLimit,
       Policy_Deductible, PolicyAnnualPremium, UmbrellaLimit,
       MonthofIncident, DayofIncident, InsuredRelationship,
       TypeOfIncident, TypeOfCollission, SeverityOfIncident,
       AuthoritiesContacted,IncidentState, IncidentCity, Timeofincident, NumberOfVehicles,
       PropertyDamage, BodilyInjuries, Witnesses, PoliceReport,
       AmountOfTotalClaim, AmountOfInjuryClaim, AmountOfPropertyClaim,
       AmountOfVehicleDamage, VehicleMake, VehicleYOM]])
    print(prediction)
    return prediction


def main():
    st.title("")
    html_temp = """
    <div style="background-color:DeepSkyBlue;padding:10px">
    <h2 style="color:white;text-align:center;">Insurance Fraud Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("---")
    CustID = st.text_input("CustomerID")
    age= st.selectbox("InsuredAge",['15-20', '20-30', '30-40','40-50','50-60','60-65'])
    if age=='15-20':
        InsuredAge=0
    elif age=='20-30':
        InsuredAge=1
    elif age=='30-40':
        InsuredAge=2
    elif age=='40-50':
        InsuredAge=3
    elif age=='50-60':
        InsuredAge=4
    elif age=='60-65':
        InsuredAge=5
    InsuredZipCode = st.text_input('InsuredZipCode')
    gen = st.selectbox("InsuredGender",['Male','Female'])
    if gen=='Female':
        InsuredGender=0
    else:
        InsuredGender = 1
    IEL= st.selectbox("InsuredEducationLevel",['Associate', 'College', 'High School','JD','MD','Masters','PhD'])
    if IEL=='Associate':
        InsuredEducationLevel=0
    elif IEL=='College':
        InsuredEducationLevel=1
    elif IEL=='High School':
        InsuredEducationLevel=2
    elif IEL=='JD':
        InsuredEducationLevel=3
    elif IEL=='MD':
        InsuredEducationLevel=4
    elif IEL=='Masters':
        InsuredEducationLevel=5
    elif IEL=='PhD':
        InsuredEducationLevel=6
    IO= st.selectbox("InsuredOccupation",['adm-clerical', 'armed-forces', 'craft-repair','exec-managerial','farming-fishing','handlers-cleaners','machine-op-inspct','other-service','priv-house-serv','prof-specialty','protective-serv','sales','tech-support','transport-moving'])
    if IO=='adm-clerical':
        InsuredOccupation=0
    elif IO=='armed-forces':
        InsuredOccupation=1
    elif IO=='craft-repair':
        InsuredOccupation=2
    elif IO=='exec-managerial':
        InsuredOccupation=3
    elif IO=='farming-fishing':
        InsuredOccupation=4
    elif IO=='handlers-cleaners':
        InsuredOccupation=5
    elif IO=='machine-op-inspct':
        InsuredOccupation=6
    elif IO=='other-service':
        InsuredOccupation=7
    elif IO=='priv-house-serv':
        InsuredOccupation=8
    elif IO=='prof-specialty':
        InsuredOccupation=9
    elif IO=='protective-serv':
        InsuredOccupation=10
    elif IO=='sales':
        InsuredOccupation=11
    elif IO=='tech-support':
        InsuredOccupation=12
    elif IO=='transport-moving':
        InsuredOccupation=13
    IHob= st.selectbox("InsuredHobbies",['Indoor activities', 'Indoor games', 'Outdoor activities','Outdoor games'])
    if IHob=='Indoor activities':
        InsuredHobbies=0
    elif IHob=='Indoor games':
        InsuredHobbies=1
    elif IHob=='Outdoor activities':
        InsuredHobbies=2
    elif IHob=='Outdoor games':
        InsuredHobbies=3
    CapitalGain = st.number_input('CapitalGains')
    Capitalloss = st.number_input('CapitalLoss')
    GL = int(CapitalGain)+int(Capitalloss)
    NetCapital = (GL -(-111100)) / (100500 - (-111100))
    CuLP = st.number_input('CustomerLoyaltyPeriod')
    CuLP = int(CuLP)  
    CustomerLoyaltyPeriod = (CuLP -(1)) / (479 - (1))
    PM= st.selectbox("Policy_Month",['January', 'February', 'March','April','May','June','July','August','September','October','November','December'])
    if PM=='January':
        Policy_Month=1
    elif PM=='February':
        Policy_Month=2
    elif PM=='March':
        Policy_Month=3
    elif PM=='April':
        Policy_Month=4
    elif PM=='May':
        Policy_Month=5
    elif PM=='June':
        Policy_Month=6
    elif PM=='July':
        Policy_Month=7
    elif PM=='August':
        Policy_Month=8
    elif PM=='September':
        Policy_Month=9
    elif PM=='October':
        Policy_Month=10
    elif PM=='November':
        Policy_Month=11
    elif PM=='December':
        Policy_Month=12
    IPS= st.selectbox("InsurancePolicyState",['State1', 'State2', 'State3'])
    if IPS=='State1':
        InsurancePolicyState=1
    elif IPS=='State2':
        InsurancePolicyState=2
    elif IPS=='State3':
        InsurancePolicyState=3
    PCSL= st.selectbox("Policy_CombinedSingleLimit",['100/300' ,'500/1000' ,'250/500', '250/1000' ,'500/300' ,'500/500', '100/500','250/300' ,'100/1000'])
    if PCSL=='100/1000':
        Policy_CombinedSingleLimit=0
    elif PCSL=='100/300':
        Policy_CombinedSingleLimit=1
    elif PCSL=='100/500':
        Policy_CombinedSingleLimit=2
    elif PCSL=='250/1000':
        Policy_CombinedSingleLimit=3
    elif PCSL=='250/300':
        Policy_CombinedSingleLimit=4
    elif PCSL=='250/500':
        Policy_CombinedSingleLimit=5
    elif PCSL=='500/1000':
        Policy_CombinedSingleLimit=6
    elif PCSL=='500/300':
        Policy_CombinedSingleLimit=7
    elif PCSL=='500/500':
        Policy_CombinedSingleLimit=8
    PDe = st.number_input('Policy_Deductible')
    PDe = float(PDe)  
    Policy_Deductible = (PDe -(500)) / (2000 - (500))
    PAPr = st.number_input('PolicyAnnualPremium')
    PAPr = float(PAPr)  
    PolicyAnnualPremium = (PAPr -(436.28)) / (2047.59 - (436.28))
    ULi = st.number_input('UmbrellaLimit')
    ULi = int(ULi)  
    UmbrellaLimit = (ULi -(-1000000)) / (10000000 - (-1000000))
    MOI= st.selectbox("MonthofIncident",['January', 'February', 'March','April','May','June','July','August','September','October','November','December'])
    if MOI=='January':
        MonthofIncident=1
    elif MOI=='February':
        MonthofIncident=2
    elif MOI=='March':
        MonthofIncident=3
    elif MOI=='April':
        MonthofIncident=4
    elif MOI=='May':
        MonthofIncident=5
    elif MOI=='June':
        MonthofIncident=6
    elif MOI=='July':
        MonthofIncident=7
    elif MOI=='August':
        MonthofIncident=8
    elif MOI=='September':
        MonthofIncident=9
    elif MOI=='October':
        MonthofIncident=10
    elif MOI=='November':
        MonthofIncident=11
    elif MOI=='December':
        MonthofIncident=12
    DaI = st.number_input('DayofIncident')
    DaI = int(DaI)
    DayofIncident = DaI-1
    IR= st.selectbox("InsuredRelationship",['not-in-family', 'wife', 'own-child', 'unmarried','husband' ,'other-relative'])
    if IR=='husband':
        InsuredRelationship=0
    elif IR=='not-in-family':
        InsuredRelationship=1
    elif IR=='other-relative':
        InsuredRelationship=2
    elif IR=='own-child':
        InsuredRelationship=3
    elif IR=='unmarried':
        InsuredRelationship=4
    elif IR=='wife':
        InsuredRelationship=5
    TOI= st.selectbox("TypeOfIncident",['Multi-vehicle Collision', 'Single Vehicle Collision' ,'Parked Car','Vehicle Theft'])
    if TOI=='Multi-vehicle Collision':
        TypeOfIncident=0
    elif TOI=='Parked Car':
        TypeOfIncident=1
    elif TOI=='Single Vehicle Collision':
        TypeOfIncident=2
    elif TOI=='Vehicle Theft':
        TypeOfIncident=3
    TOC= st.selectbox("TypeOfCollission",['Side Collision' ,'Rear Collision' ,'Front Collision','Not Damaged'])
    if TOC=='Front Collision':
        TypeOfCollission=0
    elif TOC=='Not Damaged':
        TypeOfCollission=1
    elif TOC=='Rear Collision':
        TypeOfCollission=2
    elif TOC=='Side Collision':
        TypeOfCollission=3
    SOI= st.selectbox("SeverityOfIncident",['Total Loss', 'Minor Damage' ,'Major Damage' ,'Trivial Damage'])
    if SOI=='Major Damage':
        SeverityOfIncident=0
    elif SOI=='Minor Damage':
        SeverityOfIncident=1
    elif SOI=='Total Loss':
        SeverityOfIncident=2
    elif SOI=='Trivial Damage':
        SeverityOfIncident=3
    AC= st.selectbox("AuthoritiesContacted",['Police', 'Other', 'Fire' ,'Ambulance', 'None'])
    if AC=='Ambulance':
        AuthoritiesContacted=0
    elif AC=='Fire':
        AuthoritiesContacted=1
    elif AC=='None':
        AuthoritiesContacted=2
    elif AC=='Other':
        AuthoritiesContacted=3
    elif AC=='Police':
        AuthoritiesContacted=4
    ISTA= st.selectbox("IncidentState",['State7' ,'State8', 'State9', 'State5' ,'State6','State4', 'State3'])
    if ISTA=='State3':
        IncidentState=0
    elif ISTA=='State4':
        IncidentState=1
    elif ISTA=='State5':
        IncidentState=2
    elif ISTA=='State6':
        IncidentState=3
    elif ISTA=='State7':
        IncidentState=4
    elif ISTA=='State8':
        IncidentState=5
    elif ISTA=='State9':
        IncidentState=6
    ICT= st.selectbox("IncidentCity",['City1' ,'City5' ,'City6' ,'City4', 'City3' ,'City2' ,'City7'])
    if ICT=='City1':
        IncidentCity=0
    elif ICT=='City2':
        IncidentCity=1
    elif ICT=='City3':
        IncidentCity=2
    elif ICT=='City4':
        IncidentCity=3
    elif ICT=='City5':
        IncidentCity=4
    elif ICT=='City6':
        IncidentCity=5
    elif ICT=='City7':
        IncidentCity=6
    TOIN= st.selectbox("Timeofincident",['0-6' ,'7-12' ,'13-18' ,'19-23'])
    if TOIN=='13-18':
        Timeofincident=0
    elif TOIN=='19-23':
        Timeofincident=1
    elif TOIN=='0-6':
        Timeofincident=2
    elif TOIN=='7-12':
        Timeofincident=3
    NumberOfVehicles = st.text_input('NumberOfVehicles')
    PDA = st.selectbox("PropertyDamage",['No','Yes'])
    if PDA=='No':
        PropertyDamage=0
    elif PDA=='Yes':
        PropertyDamage = 1
    BodilyInjuries = st.text_input('BodilyInjuries')
    Witnesses = st.text_input('Witnesses')
    PRP= st.selectbox("PoliceReport",['No','Yes'])
    if PRP=='No':
        PoliceReport=0
    elif PRP=='Yes':
        PoliceReport = 1
    ATCl = st.number_input('AmountOfTotalClaim')
    ATCl  = int(ATCl )  
    AmountOfTotalClaim = (ATCl  -(150)) / (114920 - (150))
    AICl = st.number_input('AmountOfInjuryClaim')
    AICl  = int(AICl )  
    AmountOfInjuryClaim = (AICl  -(0)) / (21450 - (0))
    APCl = st.number_input('AmountOfPropertyClaim')
    APCl  = int(APCl )  
    AmountOfPropertyClaim = (APCl  -(0)) / (23670 - (0))
    AVCl = st.number_input('AmountOfVehicleDamage')
    AVCl= int(AVCl )  
    AmountOfVehicleDamage = (AVCl  -(109)) / (79560 - (109))
    MKA= st.selectbox("VehicleMake",['Toyota' ,'Chevrolet' ,'Accura', 'Honda', 'BMW' ,'Saab', 'Suburu', 'Audi','Dodge' ,'Mercedes' ,'Volkswagen', 'Nissan' ,'Jeep', 'Ford'])
    if MKA=='Accura':
        VehicleMake=0
    elif MKA=='Audi':
        VehicleMake=1
    elif MKA=='BMW':
        VehicleMake=2
    elif MKA=='Chevrolet':
        VehicleMake=3
    elif MKA=='Dodge':
        VehicleMake=4
    elif MKA=='Ford':
        VehicleMake=5
    elif MKA=='Honda':
        VehicleMake=6
    elif MKA=='Jeep':
        VehicleMake=7
    elif MKA=='Mercedes':
        VehicleMake=8
    elif MKA=='Nissan':
        VehicleMake=9
    elif MKA=='Saab':
        VehicleMake=10
    elif MKA=='Suburu':
        VehicleMake=11
    elif MKA=='Toyota':
        VehicleMake=12
    elif MKA=='Volkswagen':
        VehicleMake=13
    VehicleYOM = st.text_input('VehicleYOM')

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(InsuredAge, InsuredZipCode,  InsuredGender,
       InsuredEducationLevel, InsuredOccupation, InsuredHobbies,
       NetCapital, CustomerLoyaltyPeriod, Policy_Month,
       InsurancePolicyState, Policy_CombinedSingleLimit,
       Policy_Deductible, PolicyAnnualPremium, UmbrellaLimit,
       MonthofIncident, DayofIncident, InsuredRelationship,
       TypeOfIncident, TypeOfCollission, SeverityOfIncident,
       AuthoritiesContacted,IncidentState, IncidentCity, Timeofincident, NumberOfVehicles,
       PropertyDamage, BodilyInjuries, Witnesses, PoliceReport,
       AmountOfTotalClaim, AmountOfInjuryClaim, AmountOfPropertyClaim,
       AmountOfVehicleDamage, VehicleMake, VehicleYOM)
        if result==0:
            st.success( CustID+ ' may not fraud', icon="✅")
        else:
            st.error(CustID+ ' may fraud', icon="🚨")
    st.markdown("---")
    st.markdown(" >  🙏 Thank you ")

if __name__=='__main__':
    main()
    
    
    
