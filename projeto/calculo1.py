from tkinter import Tk
import mysql.connector
from tkinter import *

# Função para calcular a ingestão calórica diária e inserir os dados na tabela
def calcular_ingestao_calorica():
    # Obter as informações do usuário
    peso_atual = float(entrada_peso_atual.get())
    peso_desejado = float(entrada_peso_desejado.get())
    sexo = var_sexo.get()
    idade = int(entrada_idade.get())
    altura = float(entrada_altura.get())
    tipo_emprego = var_tipo_emprego.get()
    exercicio_semanal = int(var_exercicio_semanal.get())
    tempo_resultados = var_tempo_resultados.get()

    # Calcular o gasto energético basal
    if sexo == 'Mulher':
        if idade <= 3:
            geb = int((58.317 * peso_atual) - 31.1)
        elif idade <= 10:
            geb = int((20.315 * peso_atual) + 485.9)
        elif idade <= 18:
            geb = int((13.384 * peso_atual) + 692.6)
        elif idade <= 30:
            geb = int((14.818 * peso_atual) + 486.6)
        elif idade <= 60:
            geb = int((8.126 * peso_atual) + 845.6)
        else:
            geb = int((9.082 * peso_atual) + 658.5)
    else:
        if idade <= 3:
            geb = int((59.512 * peso_atual) - 30.4)
        elif idade <= 10:
            geb = int((22.706 * peso_atual) + 504.3)
        elif idade <= 18:
            geb = int((17.686 * peso_atual) + 658.2)
        elif idade <= 30:
            geb = int((15.057 * peso_atual) + 692.2)
        elif idade <= 60:
            geb = int((11.472 * peso_atual) + 873.1)
        else:
            geb = int((11.711 * peso_atual) + 587.7)

    # Calcular o gasto calórico total
    if tipo_emprego == 'Leve':
        fator_atividade = 1.55
    elif tipo_emprego == 'Moderado':
        fator_atividade = 1.84
    else:
        fator_atividade = 2.2

    ingestao_calorica = int(geb * fator_atividade)

    # Ajustar a ingestão calórica para perder ou ganhar peso
    if peso_desejado < peso_atual:
        ingestao_calorica -= 500
    elif peso_desejado > peso_atual:
        ingestao_calorica += 500

    # Calcular o tempo necessário para alcançar os resultados
    if tempo_resultados == "Curto prazo":
        tempo_para_resultados = int((peso_atual - peso_desejado) * 2)
    else:
        tempo_para_resultados = int((peso_atual - peso_desejado) * 4)

    # Exibir os resultados na interface
    label_resultado.config(text="Sua ingestão calórica diária recomendada é: {} calorias.".format(ingestao_calorica))
    label_tempo.config(text="Tempo necessário para alcançar os resultados: {} semanas.".format(abs(tempo_para_resultados)))
    label_faixa_etaria_resultado.config(text="Faixa Etária: {}".format(var_faixa_etaria.get()))

    # Inserir os dados na tabela do banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="acesso123",
        database="calculo"
    )

    cursor = conexao.cursor()

    sql = "INSERT INTO usuarios (objetivo, peso_atual, peso_desejado, sexo, idade, altura, tipo_emprego, exercicio_semanal, tempo_resultados, ingestao_calorica, tempo_para_resultados, faixa_etaria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (var_objetivo.get(), peso_atual, peso_desejado, sexo, idade, altura, tipo_emprego, exercicio_semanal,
           tempo_resultados, ingestao_calorica, tempo_para_resultados, var_faixa_etaria.get())
    cursor.execute(sql, val)

    conexao.commit()
    cursor.close()
    conexao.close()


# Configurações da janela
root = Tk()
root.title("Assistente de Composição de Dieta")
root.geometry("1080x1920")

# Labels e entradas para as informações do usuário
label_peso_atual = Label(root, text="Peso atual (kg):")
label_peso_atual.pack()
entrada_peso_atual = Entry(root)
entrada_peso_atual.pack()

label_objetivo = Label(root, text="Objetivo:")
label_objetivo.pack()
var_objetivo = StringVar(root)
var_objetivo.set("Perder peso")
opcoes_objetivo = OptionMenu(root, var_objetivo, "Perder peso", "Ganhar peso", "Manter")
opcoes_objetivo.pack()

label_peso_desejado = Label(root, text="Peso desejado (kg):")
label_peso_desejado.pack()
entrada_peso_desejado = Entry(root)
entrada_peso_desejado.pack()

label_sexo = Label(root, text="Sexo:")
label_sexo.pack()
var_sexo = StringVar(root)
var_sexo.set("Mulher")
opcoes_sexo = OptionMenu(root, var_sexo, "Mulher", "Homem")
opcoes_sexo.pack()

label_idade = Label(root, text="Idade:")
label_idade.pack()
entrada_idade = Entry(root)
entrada_idade.pack()

label_altura = Label(root, text="Altura (cm):")
label_altura.pack()
entrada_altura = Entry(root)
entrada_altura.pack()

label_tipo_emprego = Label(root, text="Tipo de emprego:")
label_tipo_emprego.pack()
var_tipo_emprego = StringVar(root)
var_tipo_emprego.set("Leve")
opcoes_tipo_emprego = OptionMenu(root, var_tipo_emprego, "Leve", "Moderado", "Ativo")
opcoes_tipo_emprego.pack()

label_exercicio_semanal = Label(root, text="Exercício físico semanal (horas):")
label_exercicio_semanal.pack()
var_exercicio_semanal = StringVar(root)
var_exercicio_semanal.set("0")
opcoes_exercicio_semanal = OptionMenu(root, var_exercicio_semanal, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                      "10", "11", "12", "13", "14", "15")
opcoes_exercicio_semanal.pack()

label_tempo_resultados = Label(root, text="Tempo para alcançar os resultados:")
label_tempo_resultados.pack()
var_tempo_resultados = StringVar(root)
var_tempo_resultados.set("Curto prazo")
opcoes_tempo_resultados = OptionMenu(root, var_tempo_resultados, "Curto prazo", "Longo prazo")
opcoes_tempo_resultados.pack()

label_faixa_etaria = Label(root, text="Faixa etária:")
label_faixa_etaria.pack()
var_faixa_etaria = StringVar(root)
var_faixa_etaria.set("18-30")
opcoes_faixa_etaria = OptionMenu(root, var_faixa_etaria, "18-30", "31-50", "51+")
opcoes_faixa_etaria.pack()

# Botão para calcular a ingestão calórica
botao_calcular = Button(root, text="Calcular", command=calcular_ingestao_calorica)
botao_calcular.pack()

# Labels para exibir os resultados
label_resultado = Label(root, text="")
label_resultado.pack()

label_tempo = Label(root, text="")
label_tempo.pack()

label_faixa_etaria_resultado = Label(root, text="")
label_faixa_etaria_resultado.pack()

root.mainloop()