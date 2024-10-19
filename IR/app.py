from flask import Flask, render_template, request
import os
import math
from main import retrieve_documents

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the free text query from user input
        query = request.form['query']
        # Rank the pre-built documents using the free-text query
        ranked_results = retrieve_documents(query)
        print(ranked_results)
        return render_template('ui.html', results=ranked_results, query=query)

    return render_template('ui.html')

if __name__ == '__main__':
    app.run(debug=True)