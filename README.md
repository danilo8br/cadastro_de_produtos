# cadastro_de_produtos
 Made a product registration system using the Python language, the MySQL database and to make the interface, I used a tool called QT Designer linked with the PYQT library.

## Why?

- Just to practice my Python and SQL skills more.

# First screen


- In this first screen, the user will put the product data and choose the category to register.


![ev 10](https://user-images.githubusercontent.com/51414398/93919634-55c5f080-fce4-11ea-8804-413551eb01c0.PNG)

<summary>Registering and entering the data in the bank</summary>
 
 
 ```
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

```


# Second Screen

- On this second screen, the user will click on the button on the first screen to show the data that has been registered.

![ev 10](https://user-images.githubusercontent.com/51414398/93921396-e56c9e80-fce6-11ea-9384-82ce0aeb3327.PNG)

<summary> Listing the products </summary>

```
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

```


