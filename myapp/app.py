from flask import Flask, render_template, request,redirect,url_for,jsonify
import requests

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/result-page/<result>')
def result_page(result):
    return render_template('result.html', result=result)

@app.route('/')
def home_main():
    return render_template('home.html', result='')

@app.route('/home.html')
def home():
    return render_template('home.html', result='')

@app.route('/about.html')
def aboutus():
    return render_template('about.html',result='')

@app.route('/features.html')
def features():
    return render_template('features.html',result='')

@app.route('/description.html')
def help():
    return render_template('description.html',result='')


@app.route('/check-link', methods=["POST", "GET"])
def check_link():
    link = request.form['link']
    print(link)
    try:
        response = requests.get(link)
        if response.status_code == 200:
            result = "Linkul este funcțional!"
        else:
            result = "Linkul este broken!"
    except requests.ConnectionError:
        result = "A apărut o eroare de conexiune în timpul verificării linkului."
    except requests.Timeout:
        result = "Timeout în timpul verificării linkului."
    except requests.RequestException as e:
        result = f"A apărut o eroare în timpul verificării linkului: {str(e)}"

    print(link)
    print(result)
    return jsonify({'result': result})
    

@app.route('/result.html')
def result():

    result='Linkul este functional'
    return render_template('result.html', result=result)



   

if __name__ == '__main__':
    app.run(debug=True)
