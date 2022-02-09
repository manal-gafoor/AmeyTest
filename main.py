from flask import Flask, render_template, request
import collections

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/answer", methods=["POST"])
def calculate():
    with open(request.form["filename"]) as file:
        contents = file.readlines()
    numbers_list = [int(item.strip()) for item in contents]
    frequency_dict = collections.Counter(numbers_list)
    new_list = [item[0] for item in list(frequency_dict.most_common(5))]
    # return f"<h1>The most frequent numbers are: {new_list}</h1>"
    return render_template("answer.html", list=new_list)


if __name__ == "__main__":
    app.run(debug=True)
