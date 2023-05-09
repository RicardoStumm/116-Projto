# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Ricardo" # escreva seu nome
    idade = "15" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)     
# defina a rota para a página do pai
@app.route("/p")
def pai():


    nome = "Rubens" # escreva seu nome
    idade = "45" # escreva sua idade
    

    return render_template('pai.html' , nome = nome , idade = idade)   
# defina a rota para a página da mãe
@app.route("/m")
def mae():


    nome = "Carmen" # escreva seu nome
    idade = "44" # escreva sua idade
    

    return render_template('mae.html' , nome = nome , idade = idade)   

# defina a rota para a página do irmao
@app.route("/i")
def irmao():


    nome = "Inácio" # escreva seu nome
    idade = "9" # escreva sua idade
    

    return render_template('irmao.html' , nome = nome , idade = idade)   

# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
