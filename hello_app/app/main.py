from flask import Flask

app = Falsk (__name__)

@app.route('/')
def msg():
    return "Hello using ARGOCD"

if __name__== "__main__":
    app.run(host='0.0.0.0')
