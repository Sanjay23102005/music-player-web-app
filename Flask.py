from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def Texture():
     return render_template('Texture.html')

if __name__=='__main__':
     app.run()