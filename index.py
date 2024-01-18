from flask import Flask, render_template

app = Flask(__name__)

#Primeira página do Site
#Toda página sempre tem um Route e uma Função
#Route é o caminho que vem depois do domínio
#Função é o que eu quero exibir na página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)



#Colocar o Site no ar 
if __name__ == "__main__":
    app.run(debug=True)
    #o

#servidor heroku
    