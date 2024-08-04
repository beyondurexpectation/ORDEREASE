import streamlit as st
import pandas as pd 
#from matplotlib import pyplot as plt

st.set_page_config(layout="wide",page_title="OrderEase Portal",page_icon="chart_with_upwards_trend")

from streamlit_dynamic_filters import DynamicFilters
# User database
users = {
    "Deepak": {"password": "admin123", "role": "user"},
    "Shyam": {"password": "1568", "role": "user"},
    "KN Gupta": {"password": "Gupta123", "role": "admin"},
    "RipuDaman":{"password":"Ripu@123","role":"admin"},
    "VineetVaid":{"password":"Vineet@123","role":"user"},
    
    "Vijay": {"password": "Vijay@2000", "role": "Party"},
    "Abhishek":{"password":"Abhi1234","role":"user"}
               
}

def login():
    """Simple login form"""
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['role'] = users[username]["role"]
        else:
            st.sidebar.error("Incorrect username or password")

def logout():
    """Simple logout form"""
    st.sidebar.title("Logout")
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.session_state['role'] = None

def admin_section():
    st.sidebar.title("Admin Section")
    if st.sidebar.button("Show Data"):
        st.write("Displaying admin data...")
        # Add your admin functionalities here
        st.write("Admin data goes here...")

def user_section():
    st.header("Please Create new order ")
    
    Col1,Col2,Col3,Col4,Col5=st.columns([3,3,3,3,3])
    with Col1:
         Date_in=st.date_input("Date")
         Ord_No=st.text_input("Order No")
         Appli=st.text_input("Application")
         Desti=st.text_input("Destination")
        
    with Col2:
         Cust=st.text_input('Cust. Name')
         Grade=st.multiselect("Grade",{'201RS','204CU','316','316L','409M','321H','410S','201DD','201SDM','409S','304','304L'})
         OrderQty=st.number_input("Order Qty     (MT)")
         Condition=st.multiselect('Condition',{'HRAPCOIL-2DT','PATTA-BACOIL','CR-SHEET','BACOIL','HRAP-SHEET','HRAP PLATE','HRAPCOIL','HRAPCOIL-NBT','PATTA-HRAPCOIL','CRAPCOIL'})
    with Col3:
        Ship_To=st.text_input("Ship To")
        Thickness=st.text_input("Thickness")
        DispatchQty=st.number_input("Dispatch Qty     (MT)")
        Status=st.text_input("Status")
        

        st.write(" ")
        st.write( "     ")
        save=st.button("Save Order")
        
    with Col4:
        Order_By=st.multiselect("OrderBy",{"Ripu Daman","Deepak","Rakesh Dubey","KN Gupta","Shyam","Vineet Vaid "})
        Tolerence=st.text_input("Tolerence")
        BalanceQty=st.number_input("Balance Qty     (MT)")
        Total_width=st.text_input("Total Width")
    with Col5:
        PO_NO=st.text_input("PO NO")
        Width=st.text_input("Width")
        Remark=st.text_input("Remarks")
        Length=st.text_input("Length")
    
    if "mb" not in  st.session_state:
        st.session_state.mb=pd.DataFrame(columns=['Date','Customer Name','ShipTo','OrderBy','Po Noo','Order No','Grade','Thicknesss','Tolerence','Width','Application','Order Qty','Dispatch Qty','Balance Qty','Remarks'])
    
    
    new_df=pd.DataFrame({'Date':Date_in,'Customer Name':Cust,'ShipTo':Ship_To,'OrderBy':Order_By,'Po Noo':PO_NO,'Order No':Ord_No,'Grade':Grade,'Thicknesss':Thickness,'Tolerence':Tolerence,'Width':Width,'Application':Appli,'Order Qty':OrderQty,'Dispatch Qty':DispatchQty,'Balance Qty':BalanceQty,'Remarks':Remark,'Length':Length,'Condition':Condition,'status':Status,'Totalwidth':Total_width})
    if save:
        st.session_state.mb=pd.concat([st.session_state.mb,new_df],axis=0)
        st.success("Order Save Successfully")   
        
def plot_sec():
    if rr=="report":
        data_1=pd.DataFrame(st.session_state.mb)
        col1,Col2,Col3=st.columns(3)
        with  col1:
            st.write("Total Order Qty")
            st.write(data_1['Order Qty'].sum())
        with Col2:
            st.write("Total Dispatch Qty ")
            st.write(data_1['Dispatch Qty'].sum())
        with Col3:
            st.write("Total Balance Qty ")
            st.write(data_1['Balance Qty'].sum())
        #da=data_1.groupby(['Grade'])['Order Qty'].sum()
        #st.bar_chart(data_1,x="Grade",y="Order Qty",color='Thicknesss')

def view_user():
    new1=st.session_state.mb
    if st.session_state['role']=='user':
        new1=new1[new1['OrderBy']==st.session_state['username']]
    st.write(f"Order Sheet Summary Report for , {st.session_state['username']}")
    zz=new1.groupby(['Grade','Customer Name','Thicknesss'])[['Balance Qty','Order Qty']].sum()
    st.write(zz)
 
 
  

  

    


    

        
        




    
def view():
    if rr=="View":
        st.markdown("OrderEase Order Viewing Section ,Here  you can view order")
        new=pd.DataFrame(st.session_state.mb)
        if st.session_state['role']=='admin':
         new=st.session_state.mb
         new['Balance Qty']=new['Order Qty']-new['Dispatch Qty']
        if st.session_state['role']=='user':
         new=new[new['OrderBy']==st.session_state['username']]
         new['Balance Qty']=new['Order Qty']-new['Dispatch Qty']
      
    dyy=DynamicFilters(new,filters=['OrderBy','Grade','Condition','Customer Name','Thicknesss'])
    dyy.display_filters(location='columns',num_columns=5)
    dyy.display_df()
   
    
          
        


        
    

           
        

           
           
    
           
    


        
        
        
        #st.session_state.mb=new    
       # st.write(st.session_state.mb)
def Edit():
    if rr=="Edit":
        
        new_data=st.data_editor(st.session_state.mb)
        new_data=new_data[(new_data['status']!='Dispatch')&(new_data['status']!='Cancel')]
        st.session_state.mb=new_data
def Report():
    if rr=="report":
        new_1=st.session_state.mb
        
        dyy=DynamicFilters(new_1,filters=['OrderBy','Customer Name','Grade','Condition'])
        
        
        dyy.display_filters(num_columns=5,location='columns')
       
        
        x=pd.DataFrame(dyy.display_df())
       
        
def Stock():
    st.title('OrderEase Stock Section')
    Col1,Col2,Coll3=st.columns(3)
    with Col2:
        daa=st.file_uploader('Please Upload File',type='xlsx')
    if daa:
        data=pd.read_excel(daa)
        st.write(data)

        



        
    
    
   
    


       

 

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = None
    st.session_state['role'] = None
    



if not st.session_state['logged_in']:
    login()
else:
    logout()
st.sidebar.header((f"OrderEase  User Menu for , {st.session_state['username']}"))
    #st.header(f"OrderEase  User Menu for , {st.session_state['username']}")
if st.session_state['role']=="user" or st.session_state['role']=="admin":
  rr=st.sidebar.radio("Order Section",{'Edit','View','report'})
if st.session_state['role'] == "admin" or st.session_state['role']=="user":
    if rr=="View":
        view()
        view_user()
if st.session_state['role']=="admin":

    if rr=="report":
       plot_sec()
    if rr=="Edit":
        Edit()


    
if st.session_state['role']=="Party":
    user_section()
        
    
#st.markdown("<b>This is bold text using HTML in st.markdown.</b>", unsafe_allow_html=True)
