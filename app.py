# from flask import Flask, jsonify, render_template
# import pandas as pd
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/data')
# def data():
#     if os.path.exists('data.xlsx'):
#         df = pd.read_excel('data.xlsx', parse_dates=['Time'])
#         # Ensure datetime format includes seconds when converting to string
#         data = {
#             "Time": df['Time'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist(),
#             "A1": df['A1'].tolist(),
#             "B1": df['B1'].tolist(),
#             "C1": df['C1'].tolist(),
#             "D1": df['D1'].tolist()
#         }
#         return jsonify(data)
#     else:
#         return jsonify({"error": "Data file not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    if os.path.exists('data.xlsx'):
        df = pd.read_excel('data.xlsx', parse_dates=['Time'])
        # Calculate the average of the four columns for each row
        df['Average'] = df[['A1', 'B1', 'C1', 'D1']].mean(axis=1)
        data = {
            "Time": df['Time'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist(),
            "Average": df['Average'].tolist()
        }
        return jsonify(data)
    else:
        return jsonify({"error": "Data file not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
