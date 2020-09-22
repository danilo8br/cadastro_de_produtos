# IMPORTANDO BIBLIOTECAS
from PyQt5 import uic, QtWidgets
import MySQLdb

# CONECTANDO AO BANCO DE DADOS
try:
    banco = MySQLdb.connect(
        db='lojinha',
        host='localhost',
        user='root',
        passwd='root')
except:
    print('Não foi possível se-conectar com o banco de dados')

# TELA DE CADASTRO
def cadastrar():
    codigo = str(primeira_tela.lineEdit.text())
    preco = float(primeira_tela.lineEdit_2.text())
    descricao = str(primeira_tela.lineEdit_3.text())
    
    categoria = ''

    if primeira_tela.radioButton.isChecked():
        categoria = 'Brinquedos'
    elif primeira_tela.radioButton_2.isChecked():
        categoria = 'Alimentos'
    else:
        categoria = 'Eletronicos'

# INSERINDO OS DADOS NO BANCO
    try:
        cursor = banco.cursor()
        comando_sql = (f"INSERT INTO produtos (codigo, preco, descricao) VALUES ('{codigo}', '{preco}', '{descricao}');")
        comando_sql2 = (f"INSERT INTO categoria (tipo_categoria) VALUES ('{categoria}');")
        cursor.execute(comando_sql)
        cursor.execute(comando_sql2)
        banco.commit()
        primeira_tela.close()
        segunda_tela.show()
    except:
        print('Não foi possivel inserir os dados')

# VOLTAR PARA TELA INICIAL
def logout():
    segunda_tela.close()
    terceira_tela.close()
    quarta_tela.close()
    quinta_tela.close()
    sexta_tela.close()
    setima_tela.close()
    primeira_tela.show()

# LISTANDO OS PRODUTOS
def listar():
    primeira_tela.close()
    terceira_tela.show()
    cursor = banco.cursor()
    comando_sql = (f"SELECT id, codigo, preco, descricao, tipo_categoria FROM produtos INNER JOIN categoria ON produtos.id = categoria.id_categoria;")
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    # MOSTRANDO OS DADOS CADASTRADOS
    terceira_tela.tableWidget.setRowCount(len(dados_lidos))
    terceira_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            terceira_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

# REDIRECIONANDO PARA A PAGINA DE ALTERAR OS PRODUTOS
def redirecionar_para_alterar():
    primeira_tela.close()
    quarta_tela.show()

def alterar():
    codigo = str(quarta_tela.lineEdit.text())
    descricao = str(quarta_tela.lineEdit_2.text())
    preco = str(quarta_tela.lineEdit_3.text())
    try:
        cursor = banco.cursor()
        comando_sql = (f"UPDATE produtos SET descricao = '{descricao}', preco = '{preco}' WHERE codigo = '{codigo}';")
        cursor.execute(comando_sql)
        banco.commit()
        quarta_tela.close()
        quinta_tela.show()
    except:
        print('Não foi possivel atualizar os dados')

# REDIRECIONANDO PARA A PAGINA DE DELETAR PRODUTOS
def redirecionar_para_deletar():
    primeira_tela.close()
    sexta_tela.show()

# DELETANDO OS PRODUTOS
def deletar():
    codigo = str(sexta_tela.lineEdit.text())
    try:
        cursor = banco.cursor()
        comando_sql = (f"DELETE FROM produtos WHERE codigo = '{codigo}';")
        cursor.execute(comando_sql)
        banco.commit()
        sexta_tela.close()
        setima_tela.show()
    except:
        print('Não foi possivel deletar o produto')

# CONECTANDO A APLICAÇÃO
app=QtWidgets.QApplication([])
# CARREGANDO OS ARQUIVOS
primeira_tela=uic.loadUi('primeira_tela.ui')
segunda_tela=uic.loadUi('segunda_tela.ui')
terceira_tela=uic.loadUi('terceira_tela.ui')
quarta_tela=uic.loadUi('quarta_tela.ui')
quinta_tela=uic.loadUi('quinta_tela.ui')
sexta_tela=uic.loadUi('sexta_tela.ui')
setima_tela=uic.loadUi('setima_tela.ui')
# BOTÕES
primeira_tela.pushButton.clicked.connect(cadastrar)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.pushButton_2.clicked.connect(listar)
primeira_tela.pushButton_4.clicked.connect(redirecionar_para_alterar)
quarta_tela.pushButton.clicked.connect(alterar)
quinta_tela.pushButton.clicked.connect(logout)
terceira_tela.pushButton.clicked.connect(logout)
sexta_tela.pushButton.clicked.connect(deletar)
primeira_tela.pushButton_3.clicked.connect(redirecionar_para_deletar)
setima_tela.pushButton.clicked.connect(logout)
# MOSTRANDO A TELA INICIAL
primeira_tela.show()
# EXECUTANDO A APLICAÇÃO
app.exec()