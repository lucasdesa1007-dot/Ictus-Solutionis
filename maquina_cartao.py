#dentro do terminal, instala "pip install customtkinter"
#após instalar o customtkinter, Apertar Ctrl + Shift + P e digita Install Missing Imports
#instala ele também e depois fecha e reinicia o visual code
 
import datetime as dt  #importa a biblioteca datetime "as dt" pede para chamar ela de dt
import customtkinter as ctk  #importa a biblioteca customtkinter "as ctk" pede para chamar ela de ctk
 
ctk.set_appearance_mode("dark")
app = ctk.CTk()  #aqui nós chamamos a gaveta principal do customtkinter
app.title("Ictus Solutionis PAY - Maquininha")
app.geometry("200x150")  #aqui dimencionamos o tamanho da nossa tela
 
scroll_frame = ctk.CTkScrollableFrame(app)  #aqui colocamos a ferramenta da barra de scroll no programa
scroll_frame.pack(fill="both", expand=True, padx=2, pady=2)
 
bandeiras = ["visa", "mastercard", "elo", "amex", "hipercard"]
 
# LISTA QUE VAI SALVAR TUDO
vendas = []
 
def fazer_venda():
    try:
        valor = float(entry_valor.get())
        tipo = combo_tipo.get()
        bandeira = combo_bandeira.get()
        parcelas_str = entry_parcelas.get()
        parcelas = int(parcelas_str) if parcelas_str else 1
        if parcelas == 0: parcelas = 1
        valor_parcela = valor / parcelas
        data = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
 
        # salva na lista
        venda = {
            "data": data,
            "bandeira": bandeira,
            "tipo": tipo,
            "valor": valor,
            "parcelas": parcelas
        }
        vendas.append(venda)
 
        label_recibo.configure(text=f"APROVADO!\n {data}\n {bandeira} ---- {tipo}\n R${valor:.2f}\nSalvo! Total hoje: {len(vendas)}")
        entry_valor.delete(0, 'end')
        entry_parcelas.delete(0, 'end')
    except Exception as e:
        label_recibo.configure(text=f"ERRO: {e}")




####   =================================================
####   AQUI COMEÇA A SEGUNDA TELA PARA MOSTRAR AS VENDAS
####   =================================================

def mostrar_vendas():
    # cria uma janela nova
    janela = ctk.CTkToplevel(app)
    janela.title(f"Vendas de Hoje - {len(vendas)} vendas")
    janela.geometry("200x150")
 
    if not vendas:
        ctk.CTkLabel(janela, text="Nenhuma venda hoje").pack(pady=20)
        #CTkLabel vale pelo print, serve apenas para apresentar uma mensagem
        return
 
    scroll = ctk.CTkScrollableFrame(janela)
    scroll.pack(fill="both", expand=True, padx=5, pady=5)
 
    total = 0
    for i, v in enumerate(vendas, 1):
        total += v['valor']
        texto = f"{i}. {v['data']} - R$ {v['valor']:.2f}\n   {v['bandeira']} {v['tipo']} {v['parcelas']}x"
        ctk.CTkLabel(scroll, text=texto, anchor="w", justify="left", font=("Arial", 10)).pack(fill="x", pady=3, padx=5)
   
    ctk.CTkLabel(scroll, text=f"\nTOTAL DO DIA: R$ {total:.2f}", font=("Arial", 12, "bold")).pack(pady=10)

####       =====================================
####       AQUI TERMINA A TELA DE MOSTRAR VENDAS
####       =====================================
 





# UI
#CTkLabel = esse é só para para mostrar a frase, tipo print
#CTkEntry = esse é como se fosse o input
#CTkComboBox= esse gera uma box para selecionar opções pré estabelecidas
#CTkButton= esse é um botão que gera uma reação
 
ctk.CTkLabel(scroll_frame, text="Ictus Solutionis", font=("Arial", 12, "bold")).pack(pady=2)
 
entry_valor = ctk.CTkEntry(scroll_frame, placeholder_text="Valor R$", width=120, height=20, font=("Arial", 10))
entry_valor.pack(pady=2, padx=5)
 
combo_tipo = ctk.CTkComboBox(scroll_frame, values=["debito", "credito"], width=120, height=20, font=("Arial", 10))
combo_tipo.set("credito")
combo_tipo.pack(pady=2, padx=5)
 
combo_bandeira = ctk.CTkComboBox(scroll_frame, values=bandeiras, width=120, height=20, font=("Arial", 10))
combo_bandeira.set("visa")
combo_bandeira.pack(pady=2, padx=5)
 
entry_parcelas = ctk.CTkEntry(scroll_frame, placeholder_text="Parcelas", width=120, height=20, font=("Arial", 10))
entry_parcelas.pack(pady=2, padx=5)
 
btn = ctk.CTkButton(scroll_frame, text="APROVAR", width=120, height=22, font=("Arial", 10, "bold"), command=fazer_venda)
btn.pack(pady=3)
 
btn_lista = ctk.CTkButton(scroll_frame, text="VENDAS DE HOJE", width=120, height=22, fg_color="gray", font=("Arial", 10), command=mostrar_vendas)
btn_lista.pack(pady=3)
 
label_recibo = ctk.CTkLabel(scroll_frame, text="", font=("Arial", 10), justify="left", anchor="w", width=120, height=40)
label_recibo.pack(pady=2, padx=5)
 
app.mainloop()
