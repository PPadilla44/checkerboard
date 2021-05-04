from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def reg_board():
    return render_template("index.html", rows=4, cols=4, color1="red" ,color2="black")
@app.route("/<rows>")
def rows_board(rows):
    return render_template("index.html", rows=int(int(rows)/2), cols=4, color1="red" ,color2="black")
@app.route("/<rows>/<cols>")
def cols_board(rows,cols):
    return render_template("index.html", rows=int(int(rows)/2), cols=int(int(cols)/2), color1="red" ,color2="black")
@app.route("/<rows>/<cols>/<color1>/<color2>")
def color_board(rows,cols,color1,color2):
    return render_template("index.html", rows=int(int(rows)/2), cols=int(int(cols)/2), color1=str(color1) ,color2=str(color2))
if __name__=="__main__":
    app.run(debug=True)