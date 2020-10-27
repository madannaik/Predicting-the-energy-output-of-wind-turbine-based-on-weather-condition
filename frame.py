import streamlit as slt 
from sklearn.externals import joblib
import random
import time
from PIL import Image
def main():
    model = joblib.load("lasso.pk1")
    day = random.randint(1,30)
    def wind_direction(x):
        if x=='N':
            return 0
        if x=="NNE":
            return 
        if x=="NEE":
            return 60
        if x=="E":
            return 90 
        if x=="SEE":
            return 120
        if x=="SSE":
            return 150 
        if x=="S":
            return 180
        if x=="SSW":
            return 210
        if x=="SWW":
            return 240
        if x=="W":
            return 270
        if x=="NWW":
            return 300
        if x=="NNW":
            return 330

    def find_month(x):
        if "January" in x:
            return 1
        elif "Febrauary" in x:
            return 2
        elif "March" in x:
            return 3    
        elif "April" in x:
            return 4    
        elif "May" in x:
            return 5    
        elif "June" in x:
            return 6    
        elif "July" in x:
            return 7    
        elif "August" in x:
            return 8    
        elif "September" in x:
            return 9 
        elif "October" in x:
            return 10    
        elif "November" in x:
            return 11    
        else:
            return 12  
            
    def draw_graph(x):
        if x=='N':
            image = Image.open('graph/1_N_Powercurve.jpeg')
            return image
        if x=="NNE":
            image = Image.open('graph/1_NNE_Powercurve.jpeg')
            return image
        if x=="NEE":
            image = Image.open('graph/1_NEE_Powercurve.jpeg')
            return image
        if x=="E":
            image = Image.open('graph/1_E_Powercurve.jpeg')
            return image
        if x=="SEE":
            image = Image.open('graph/1_SSE_Powercurve.jpeg')
            return image
        if x=="SSE":
            image = Image.open('graph/1_SSE_Powercurve.jpeg')
            return image
        if x=="S":
            image = Image.open('graph/1_S_Powercurve.jpeg')
            return image
        if x=="SSW":
            image = Image.open('graph/1_SSW_Powercurve.jpeg')
            return image
        if x=="SWW":
            image = Image.open('graph/1_SWW_Powercurve.jpeg')
            return image
        if x=="W":
            image = Image.open('graph/1_W_Powercurve.jpeg')
            return image
        if x=="NWW":
            image = Image.open('graph/1_NWW_Powercurve.jpeg')
            return image
        if x=="NNW":
            image = Image.open('graph/1_NNW_Powercurve.jpeg')
            return image

    slt.title("WIND ENERY PREDICTOR")
    slt.sidebar.title("APP")
    direction = slt.sidebar.selectbox('Select the wind direction',('N','NNE','NEE','E','SEE','SSE','S','SSW','SWW','W','NWW','NNW'),key='direction')
    speed = slt.sidebar.slider('select the wind speed',3.0,25.5,step=1.0,key='speed')
    month = slt.sidebar.selectbox('select the month',('January','Febraury','March','April','May','June','July','August','September','October','November','December'),key='month')
    time_ = slt.sidebar.number_input('Enter the hour',0.0,24.0,step=1.0,key='time_')
    if slt.sidebar.button("Predict"):
        with slt.spinner('Wait for it...'):
            time.sleep(1)
            predict = model.predict([[wind_direction(direction),find_month(month),day,time_,speed]])
            slt.write('predicted energy output(KW/h) ', predict.round(2))
            slt.success('Done!')
            slt.write("This is the graph of data collected across years to {} winds".format(direction))
            slt.image(draw_graph(direction),use_column_width=True)




 
if __name__ == '__main__':
    main()   

    


