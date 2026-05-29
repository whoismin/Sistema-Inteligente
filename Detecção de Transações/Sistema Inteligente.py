import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

transacoes = [
    {"cliente": "Magazine Luiza S.A.", "destino": "Fornecedor Tecnologia Alpha", "valor": 25000, "data": "2026-04-03"},
    {"cliente": "Magazine Luiza S.A.", "destino": "Fornecedor Tecnologia Alpha", "valor": 27000, "data": "2026-04-10"},
    {"cliente": "Magazine Luiza S.A.", "destino": "Fornecedor Tecnologia Alpha", "valor": 26500, "data": "2026-04-17"},
    {"cliente": "Magazine Luiza S.A.", "destino": "Fornecedor Tecnologia Alpha", "valor": 29000, "data": "2026-04-24"},

    {"cliente": "Banco Inter", "destino": "Cloud Data Services", "valor": 45000, "data": "2026-04-02"},
    {"cliente": "Banco Inter", "destino": "Cloud Data Services", "valor": 46000, "data": "2026-04-09"},
    {"cliente": "Banco Inter", "destino": "Cloud Data Services", "valor": 47000, "data": "2026-04-16"},
    {"cliente": "Banco Inter", "destino": "Cloud Data Services", "valor": 49000, "data": "2026-04-23"},

    {"cliente": "Nubank", "destino": "AWS Brasil", "valor": 18000, "data": "2026-04-05"},

    {"cliente": "iFood", "destino": "Fornecedor Logística Prime", "valor": 32000, "data": "2026-04-01"},
    {"cliente": "iFood", "destino": "Fornecedor Logística Prime", "valor": 33500, "data": "2026-04-08"},
    {"cliente": "iFood", "destino": "Fornecedor Logística Prime", "valor": 34000, "data": "2026-04-15"},
    {"cliente": "iFood", "destino": "Fornecedor Logística Prime", "valor": 35000, "data": "2026-04-22"},

    {"cliente": "Mercado Livre", "destino": "Transportadora Express", "valor": 22000, "data": "2026-04-04"},
    {"cliente": "Mercado Livre", "destino": "Transportadora Express", "valor": 22500, "data": "2026-04-11"},
    {"cliente": "Mercado Livre", "destino": "Transportadora Express", "valor": 24000, "data": "2026-04-18"},
]

df = pd.DataFrame(transacoes)

df["data"] = pd.to_datetime(df["data"])
df["semana"] = df["data"].dt.isocalendar().week

LIMITE_VALOR = 20000

transacoes_altas = df[df["valor"] > LIMITE_VALOR].copy()

basket = []

for semana, grupo in transacoes_altas.groupby("semana"):
    itens = []

    for _, linha in grupo.iterrows():
        itens.append(f"CLIENTE_{linha['cliente']}")
        itens.append(f"DESTINO_{linha['destino']}")
        itens.append("VALOR_ALTO")

    basket.append(itens)

te = TransactionEncoder()
te_data = te.fit(basket).transform(basket)

df_apriori = pd.DataFrame(te_data, columns=te.columns_)

frequentes = apriori(
    df_apriori,
    min_support=0.5,
    use_colnames=True
)

print("\n==============================")
print("PADRÕES FREQUENTES DETECTADOS")
print("==============================\n")

print(frequentes)

print("\n==============================")
print("ALERTAS GERADOS")
print("==============================\n")

for (cliente, destino), grupo in transacoes_altas.groupby(["cliente", "destino"]):

    semanas = sorted(grupo["semana"].unique())

    recorrente = len(semanas) >= 3 and all(
        semanas[i] + 1 == semanas[i + 1]
        for i in range(len(semanas) - 1)
    )

    if recorrente:
        total = grupo["valor"].sum()
        media = grupo["valor"].mean()

        print("🚨 ALERTA FINANCEIRO")
        print(f"Cliente: {cliente}")
        print(f"Destino: {destino}")
        print(f"Semanas consecutivas: {semanas}")
        print(f"Total movimentado: R$ {total:,.2f}")
        print(f"Média semanal: R$ {media:,.2f}")
        print("Classificação: ALTO RISCO")
        print("Motivo: Transações recorrentes acima de R$ 20.000 detectadas semanalmente.")
        print("-" * 60)