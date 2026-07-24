from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Form Data Receive karna
        student_name = request.form.get('student_name', '')
        roll_no = request.form.get('roll_no', '')
        semester = request.form.get('semester', '')
        year = request.form.get('year', '')
        
        # ML Input Features (Numbers)
        study_hours = float(request.form.get('study_hours', 0))
        attendance = float(request.form.get('attendance', 0))

        # Dummy Prediction logic (Apne model.predict() se replace karein agar model load kiya hai)
        # prediction = model.predict([[study_hours, attendance]])[0]
        prediction_result = "Pass" if attendance > 40 and study_hours > 2 else "Fail"

        # Correctly closed render_template function
        return render_template(
            'result.html', 
            name=student_name, 
            roll=roll_no, 
            sem=semester, 
            year=year,
            prediction=prediction_result
        )

if __name__ == '__main__':
    app.run(debug=True)