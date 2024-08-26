import numpy as np
import pickle
import joblib
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Rectangle
import shap
shap.initjs()
import time
from flask import Flask, request, jsonify, render_template
import base64
import io

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    gender= request.args.get('gender')
    InternetService= request.args.get('InternetService')
    contract= request.args.get('Contract')
    paymentmethod= request.args.get('PaymentMethod')
    SeniorCitizen = 0
    if 'SeniorCitizen' in request.form:
        SeniorCitizen = 1
    Partner = 0
    if 'Partner' in request.form:
        Partner = 1
    Dependents = 0
    if 'Dependents' in request.form:
        Dependents = 1
    PaperlessBilling = 0
    if 'PaperlessBilling' in request.form:
        PaperlessBilling = 1

    MonthlyCharges = int(request.form["MonthlyCharges"])
    Tenure = int(request.form["Tenure"])
    TotalCharges = MonthlyCharges*Tenure

    PhoneService = 0
    if 'PhoneService' in request.form:
        PhoneService = 1

    MultipleLines = 0
    if 'MultipleLines' in request.form and PhoneService == 1:
        MultipleLines = 1

    

    OnlineSecurity = 0
    if 'OnlineSecurity' in request.form and InternetService!=2:
        OnlineSecurity = 1

    OnlineBackup = 0
    if 'OnlineBackup' in request.form and InternetService!=2:
        OnlineBackup = 1

    DeviceProtection = 0
    if 'DeviceProtection' in request.form and InternetService!=2:
        DeviceProtection = 1

    TechSupport = 0
    if 'TechSupport' in request.form and InternetService!=2:
        TechSupport = 1

    StreamingTV = 0
    if 'StreamingTV' in request.form and InternetService!=2:
        StreamingTV = 1

    StreamingMovies = 0
    if 'StreamingMovies' in request.form and InternetService!=2:
        StreamingMovies = 1




    features = [gender, SeniorCitizen, Partner, Dependents, Tenure, PhoneService, MultipleLines,InternetService, OnlineSecurity, OnlineBackup,
       DeviceProtection, TechSupport, StreamingTV, StreamingMovies,contract,PaperlessBilling,paymentmethod, MonthlyCharges, TotalCharges]

    

    final_features = [np.array(features)]
    prediction = model.predict_proba(final_features)

    output = prediction[0,1]

    def degree_range(n):
        start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
        end = np.linspace(0,180,n+1, endpoint=True)[1::]
        mid_points = start + ((end-start)/2.)
        return np.c_[start, end], mid_points

    def rot_text(ang):
        rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
        return rotation

    def gauge(labels=['LOW','MEDIUM','HIGH','EXTREME'], \
              colors=['#007A00','#0063BF','#FFCC00','#ED1C24'], Probability=1, fname=False):

        N = len(labels)
        colors = colors[::-1]


        """
        begins the plotting
        """

        gauge_img = io.BytesIO()
        fig, ax = plt.subplots()

        ang_range, mid_points = degree_range(4)

        labels = labels[::-1]

        """
        plots the sectors and the arcs
        """
        patches = []
        for ang, c in zip(ang_range, colors):
            # sectors
            patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
            # arcs
            patches.append(Wedge((0.,0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=0.5))

        [ax.add_patch(p) for p in patches]


        """
        set the labels (e.g. 'LOW','MEDIUM',...)
        """

        for mid, lab in zip(mid_points, labels):

            ax.text(0.35 * np.cos(np.radians(mid)), 0.35 * np.sin(np.radians(mid)), lab, \
                horizontalalignment='center', verticalalignment='center', fontsize=14, \
                fontweight='bold', rotation = rot_text(mid))

        """
        set the bottom banner and the title
        """
        r = Rectangle((-0.4,-0.1),0.8,0.1, facecolor='w', lw=2)
        ax.add_patch(r)

        ax.text(0, -0.05, 'Churn Probability ' + np.round(Probability,2).astype(str), horizontalalignment='center', \
             verticalalignment='center', fontsize=22, fontweight='bold')

        """
        plots the arrow now
        """

        pos = (1-Probability)*180
        ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)), \
                     width=0.04, head_width=0.09, head_length=0.1, fc='k', ec='k')

        ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
        ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))

        """
        removes frame and ticks, and makes axis equal and tight
        """

        ax.set_frame_on(False)
        ax.axes.set_xticks([])
        ax.axes.set_yticks([])
        ax.axis('equal')
        plt.tight_layout()

        plt.savefig(gauge_img, format = 'png')
        gauge_img.seek(0)
        url = base64.b64encode(gauge_img.getvalue()).decode()
        return url

    gauge_url = gauge(Probability = output)

    t = time.time()
    return render_template('index.html', prediction_text='Churn probability is {}'.format(round(output, 2)), url_1 = gauge_url)


if __name__ == "__main__":
    app.run(debug=True)
