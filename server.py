from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "password1234"



@app.route( '/', methods=['GET'] )
def display_student_form():
    return render_template( "student_form.html" )

@app.route( '/process', methods=['POST','GET'] )
def create_student():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route( '/results' )
def get_results():
        return render_template( "results.html")




if __name__ == "__main__":
    app.run( debug = True, port=5001 )