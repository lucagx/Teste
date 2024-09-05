import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

menor_faturamento = min(d["valor"] for d in dados if d["valor"]> 0)
maior_faturamento = max(d["valor"] for d in dados)

dias_faturamento = [d["valor"] for d in dados if d["valor"]> 0]
media_faturamento = sum(dias_faturamento) / len (dias_faturamento)

acima_media = len([d for d in dados if d["valor"] > media_faturamento])
dias_acima_media = [d["dia"] for d in dados if d["valor"] > media_faturamento]

print("O menor faturamento foi de R$", menor_faturamento)
print("O maior faturamento foi de R$", maior_faturamento)
print("A média mensal foi superada em", acima_media, "dias neste mês, nos dias:", dias_acima_media)

