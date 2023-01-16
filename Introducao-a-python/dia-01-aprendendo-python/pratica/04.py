livros = 60
preco_do_livro = (1 - 0.4) * 24.20
custo = 3 + (livros - 1) * 0.75
custo_total = livros * preco_do_livro + custo
print(f"O custo total das 60 cópias é {round(custo_total, 2)}/n")