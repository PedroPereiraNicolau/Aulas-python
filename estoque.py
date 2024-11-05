else:
                estoque[nome_produto] = quantidade
                atualizar_lista_estoque()
                limpar_campos()
                messagebox.showinfo("Sucesso", f'Produto "{nome_produto}" adicionado com sucess