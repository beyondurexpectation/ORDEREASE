import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.header("               Order Feeding Web Application")
with st.sidebar:
    add_radio=st.radio("User Section",("Home","View","Edit"))
if "mb" not in st.session_state:
    st.session_state.mb=pd.DataFrame(columns=['SR No','Sales Man','Grade','Thickness','Ship To Name','Bill to Name','Ship City','Tolerence','Order Qty','Dispatch Qty','Balance Qty','Ready Qty','Process Qty','Application','Remarks','PO.NO'])


    
Col1,Col2,Col3,Col4,Col5,Col6,Col7,=st.columns([.5,1,1,1,1,1,1])

if add_radio=="Home":
   with Col1:
     s=st.text_input("SR.No") 
     Ship_City=st.text_input("Ship City")


    


   with Col2:
     Date=st.date_input("Date")
     Tolerence=st.text_input("Tolerence")
     Application=st.text_input("Application")
   with Col3:
     Team_leader=st.multiselect("Sales Man",('Team Ripu Daman','Deepak','Rakesh'))
    
     Order_Qty=st.number_input("Order Qty (MT)")
     Remarks=st.text_input("Remarks")
   with Col4:
     Grade=st.multiselect("Grade",('204CU','201SDM','201RS','201DD','309','304L','316L','409M','321','310S','409L','409',))

     Dispatch=st.number_input("Dispatch Qty(MT)")
     PO_NO=st.text_input("PO.NO")
     st.write(" ")
     st.write(" ")
     st.write(" ")
    
     Submit=st.button("Save Order ")
   with Col5:
     Thickness=st.multiselect("Thickness",('.40','.48','.50','.60','.70','.80','.90','1','1.20','1.80','1.40','.38'))
     Pending_Qty=st.number_input("Balance Qty (MT)")

   with Col6:
     Ship_to_Name=st.multiselect("Ship To Name",("Raghuvir Stainless Limited","Shah Foils"))
     Ready_Qty=st.number_input("Ready Qty(MT)")
   with Col7:
     Bill_to_Name=st.multiselect("Bill To Name",('Patel Steel','Ambaji Inox'))
     Process_Qty=st.number_input("Process Qty")
   df_new=pd.DataFrame({'SR No':s,'Sales Man':Team_leader,'Grade':Grade,'Thickness':Thickness,'Ship To Name':Ship_to_Name,'Bill to Name':Bill_to_Name,'Ship City':Ship_City,'Tolerence':Tolerence,'Order Qty':Order_Qty,'Dispatch Qty':Dispatch,'Ready Qty':Ready_Qty,'Process Qty':Process_Qty,'Application':Application,'Remarks':Remarks,'PO.NO':PO_NO,'Balance Qty':Pending_Qty})

   if Submit:
     st.session_state.mb=pd.concat([st.session_state.mb,df_new],axis=0)
     st.balloons()
if add_radio=="View":
    data=pd.DataFrame(st.session_state.mb)
    data['Balance Qty']=data['Order Qty']-data['Dispatch Qty']
    st.session_state.mb=data
    st.write(st.session_state.mb)
    Col_1,Col_2=st.columns(2)
    with Col_1:
        st.write("hello")
    with Col_2:
      st.write("How are You")
    

    
    
if add_radio=="Edit":
    new_df=pd.DataFrame(st.session_state.mb)

    new_df=st.data_editor(new_df)

    st.session_state.mb=new_df
    

    