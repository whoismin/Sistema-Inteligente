# Sistema Inteligente de Detecção de Transações Recorrentes com Apriori

# Objetivo

Desenvolver um sistema em Python utilizando técnicas de Inteligência Artificial e Mineração de Dados com o algoritmo Apriori para detectar transações financeiras recorrentes de alto valor.

O sistema identifica movimentações acima de R$ 20.000,00 realizadas semanalmente para o mesmo destino e gera alertas automáticos para análise.

# Explicação do Funcionamento

O sistema utiliza técnicas de Inteligência Artificial voltadas para mineração de dados, aplicando o algoritmo Apriori para identificar padrões frequentes em transações financeiras.

Inicialmente, o sistema filtra apenas movimentações acima de R$ 20.000,00. Em seguida, organiza as transações por semanas, clientes e destinos.

O algoritmo Apriori analisa os padrões recorrentes e identifica combinações frequentes entre:

Cliente
Destino da transação
Valores altos

Após a análise, o sistema verifica se as transações ocorreram durante semanas consecutivas.

Quando o mesmo cliente realiza pagamentos elevados para o mesmo destino por três ou mais semanas seguidas, o sistema gera automaticamente um alerta de alto risco.
