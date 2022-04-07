# -*- coding: utf-8 -*-
"""
Created for capstone

@author: CSB
"""

# -*- coding: utf-8 -*-
"""
Created for capstone

@author: CSB
"""

import numpy as np
import os
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import camelot as cam
import pandas as pd
import PyPDF2
import pikepdf as Pdf
import glob

from PIL import Image


class information:
    
    def __init__(self, pdfpath):
        self.pdfpath=pdfpath
        
    def getEquityShare(self):
        table = cam.read_pdf(self.pdfpath, pages = '1', flavor = 'stream')
        for i in range(0,len(table)):
            df=table[i].df
    #         regex = "EQUITY SHARES"
            regex = "EQUITY"
            for i in range(0,len(df.columns)):
                df1=df[df[i].str.contains(regex, regex= True, na=False)]
                if(len(df1)>0):
    #                 print(df1.values)
                    sl=df1[0].iloc[0].split()
    #                 print(sl)
    #                 def nextword(target, source):
                    for i, w in enumerate(sl):
                        if w == "EQUITY":
                            return(sl[i-1])
                            break
                            
    def getFaceValue(self):
        table = cam.read_pdf(self.pdfpath, pages = '1', flavor = 'stream')
        for i in range(0,len(table)):
            df=table[i].df
            regex = "FACE"
            for i in range(0,len(df.columns)):
                df1=df[df[i].str.contains(regex, regex= True, na=False)]
                if(len(df1)>0):
    #                 print(df1.values)
                    sl=df1[0].iloc[0].split()
    #                 print(sl)
    #                 def nextword(target, source):
                    for i, w in enumerate(sl):
                        if w == "EACH":
                            return (sl[i-1])
    
    
    def getLeadManager(self):
        pdffileobj=open(self.pdfpath,'rb')
        pdfreader=PyPDF2.PdfFileReader(pdffileobj)
        pageobj=pdfreader.getPage(0)
        article=pageobj.extractText()     
        sl=article.split()
        for i, w in enumerate(sl):
            if w == "REGISTRAR":
                LM=(sl[i+4]+" "+sl[i+5]+" "+sl[i+6]+" "+sl[i+7])
                return LM
                
    def getOfficeLocation(self):
        table = cam.read_pdf(self.pdfpath, pages = '1', flavor = 'stream')
        for i in range(0,len(table)):
            df=table[i].df
            regex = "Registered"
            for i in range(0,len(df.columns)):
                df1=df[df[i].str.contains(regex, regex= True, na=False)]
                if(len(df1)>0):
                    return(df1.iloc[0].values[0])



# k=information("1Bhadra_DRHP.pdf")

# # initialize data of lists.
# data = {'Equity Share':k.getEquityShare(),
#         'Face value':k.getFaceValue(),
#         'Office Location':k.getOfficeLocation(),
#         'Lead Manager':k.getLeadManager()}

# # Create DataFrame
# df = pd.DataFrame(data,index=[0])

# st.dataframe(df)



# def file_selector(folder_path='.'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox('Select a file', filenames)
#     return os.path.join(folder_path, selected_filename)

# filename = file_selector()
# st.write('You selected `%s`' % filename)

def main():
    st.title("Capstone Project")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">IPO performance prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    path = st.text_input('Pdf file path','Type Here')
    filenames = os.listdir(path)
    selected_filename = st.selectbox('Select a file', filenames)
    st.write('You selected `%s`' % os.path.join(path, selected_filename))

    # selected_filename = st.file_uploader('Choose a file',type='pdf')
    # print(selected_filename)
    # datafile = st.file_uploader('Choose a file',type='pdf')
    # if datafile is not None:
    #     file_details = {"FileName":datafile.name,"FileType":datafile.type,"FilePath":dat}
    #     filename=file_details.get("FileName")
    #     st.write(filename)
    #     st.write(file_details)
        # df  = pd.read_csv(datafile)
        # st.dataframe(df)
        # # Apply Function here
        # save_uploaded_file(datafile)
        

    k=information(selected_filename)

    # initialize data of lists.
    data = {'Equity Share':k.getEquityShare(),
            'Face value':k.getFaceValue(),
            'Office Location':k.getOfficeLocation(),
            'Lead Manager':k.getLeadManager()}

    # Create DataFrame
    df = pd.DataFrame(data,index=[0])

    st.dataframe(df)


if __name__=='__main__':
    main()
    
    
    