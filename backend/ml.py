
import shap
#import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing


def predict(algo,rooms,year,area):
    print('reading_csv')
    apt = pd.read_csv("https://raw.githubusercontent.com/noghte/datasets/main/apartments.csv",nrows=1000)
    apt.dropna(subset = ['resale_price'], axis = 0, inplace = True)

    normalizer = preprocessing.Normalizer()
    X = apt.drop('resale_price', axis=1)
    X = pd.DataFrame(normalizer.fit_transform(X), columns=X.columns, index=X.index)

# normalizer = preprocessing.Normalizer().fit(X)
# x = normalizer.fit_transform(x)

    y = apt['resale_price']
    print('train_test_split')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1144)

    pred = -1
    #print('default value of pred:-',pred)
    #print("user inputs:",rooms,year,area,algo)
    if algo == "lr":
        model_reg = LinearRegression()  
        model_reg.fit(X_train, y_train)
        test = np.array([rooms,area,year]).reshape(1,3)
        test = normalizer.transform(test)
        reg_pred = model_reg.predict(test)
        pred=reg_pred[0]

    elif algo == "rf":
        rf_model = RandomForestRegressor(n_estimators=10, max_features=2)
        rf_model.fit(X_train, y_train)
        test = np.array([rooms,area,year]).reshape(1,3)
        test = normalizer.transform(test)
        rf_pred = rf_model.predict(test)
        pred = rf_pred[0]

    return pred # return the first prediction
def interpret_instance(algo,rooms,year,area):
    #df = pd.DataFrame(data=[[rooms,area,year]])
    #print(df)
    apt = pd.read_csv("https://raw.githubusercontent.com/noghte/datasets/main/apartments.csv",nrows=1000)
    apt.dropna(subset = ['resale_price'], axis = 0, inplace = True)

    normalizer = preprocessing.Normalizer()
    X = apt.drop('resale_price', axis=1)
    X = pd.DataFrame(normalizer.fit_transform(X), columns=X.columns, index=X.index)

# normalizer = preprocessing.Normalizer().fit(X)
# x = normalizer.fit_transform(x)

    y = apt['resale_price']
    print("*"*50)
    #print(df)
    print('train_test_split')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1144)

    pred = -1
    if algo == "lr":
        print("Entered lr")
        model_reg = LinearRegression()  
        model_reg.fit(X_train, y_train)
        test = np.array([rooms,area,year]).reshape(1,3)
        print(test)
        test = normalizer.transform(test)
        explainer = shap.Explainer(model_reg.predict,X_train) 
        X_test = np.vstack([X_test,test])
        shap_values = explainer(X_test)
        shap.plots.waterfall(shap_values[-1],max_display=6,show=False)
        plot.savefig('./images/img.jpg')
        #plot.clf()
        plot.close()


       
    elif algo == "rf":
        rf_model = RandomForestRegressor(n_estimators=10, max_features=2)
        rf_model.fit(X_train, y_train)
        test = np.array([rooms,area,year]).reshape(1,3)
        print(test)
        test = normalizer.transform(test)
        explainer = shap.Explainer(rf_model.predict,X_train) 
        X_test = np.vstack([X_test,test])
        shap_values = explainer(X_test)
        shap.plots.waterfall(shap_values[-1],max_display=6,show=False)
        plot.savefig('./images/img.jpg')
        #plot.clf()
        plot.close()

def interpret_model(algo,rooms,year,area,plt):
    
    #df = pd.DataFrame(data=[[rooms,area,year]])
    #print(df)
    apt = pd.read_csv("https://raw.githubusercontent.com/noghte/datasets/main/apartments.csv",nrows=1000)
    apt.dropna(subset = ['resale_price'], axis = 0, inplace = True)

    normalizer = preprocessing.Normalizer()
    X = apt.drop('resale_price', axis=1)
    X = pd.DataFrame(normalizer.fit_transform(X), columns=X.columns, index=X.index)

# normalizer = preprocessing.Normalizer().fit(X)
# x = normalizer.fit_transform(x)

    y = apt['resale_price']
    print("*"*50)
    #print(df)
    print('train_test_split')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1144)

    pred = -1
    if algo == "lr":
        print("Entered lr")
        model_reg = LinearRegression()  
        model_reg.fit(X_train, y_train)
        print("shape values success")
        explainer = shap.Explainer(model_reg.predict,X_train)
        shap_values = explainer(X_test)
        shap.summary_plot(shap_values.values, X_test, plot_type=plt,show=False)
        plot.savefig('./images/img1.jpg')
        #plot.write_image(file='static/images/staff_plot.png', format='.png')
        #plot.clf()
        plot.close()

        #shap.plots.waterfall(shap_values[df.index[0]],max_display=6,show=False)
        #plot.savefig('img.jpg')

       
    elif algo == "rf":
        rf_model = RandomForestRegressor(n_estimators=10, max_features=2)
        rf_model.fit(X_train, y_train)
        explainer = shap.Explainer(rf_model.predict,X_train)
        shap_values = explainer(X_test)
        shap.summary_plot(shap_values.values, X_test, plot_type=plt,show=False)
        plot.savefig('./images/img1.jpg')
        #plot.write_image(file='static/images/staff_plot.png', format='.png')
        #plot.clf()
        plot.close()

    

    