from services.observatorio import Observatorio

obs = Observatorio()

# Adicionar projetos (projetos reais do Senac)
obs.adicionar_projeto(
    "Sabor e Tradição Gastronômica",
    "Gastronomia",
    "2025.1",
    "Resgate de memórias afetivas em pratos para comunidades."
)

obs.adicionar_projeto(
    "Culinária Indígena",
    "Gastronomia",
    "2025.1",
    "Exploração da culinária indígena com foco em sustentabilidade."
)

obs.adicionar_projeto(
    "Culinária Árabe",
    "Gastronomia",
    "2025.1",
    "Eventos beneficentes com culinária palestina e marroquina."
)

# Listar todos
print("\n--- Todos os Projetos ---")
for p in obs.listar_projetos():
    print(p)

# Buscar projeto
print("\n--- Buscar por Título ---")
resultado = obs.buscar_projeto("Culinária Árabe")
if resultado:
    print(resultado)
else:
    print("Projeto não encontrado.")

# Filtrar por curso
print("\n--- Filtrar por Curso ---")
filtrados = obs.filtrar_por_curso("Gastronomia")
for p in filtrados:
    print(p)

# Validação
print("\n--- Teste de Validação ---")
try:
    obs.adicionar_projeto("", "Curso Teste", "2026.1")
except ValueError as e:
    print(f"Erro capturado: {e}")

# Encapsulamento
print("\n--- Alterar Descrição ---")
projeto = obs.buscar_projeto("Sabor e Tradição Gastronômica")
if projeto:
    print(f"Antes: {projeto.get_descricao()}")
    projeto.alterar_descricao("Projeto com oficinas abertas à comunidade.")
    print(f"Depois: {projeto.get_descricao()}")

# Listagem como dicionários
print("\n--- Listagem como Dicionários ---")
for p in obs.listar_projetos():
    print(p)

# Status do projeto
print("\n--- Status dos Projetos ---")
projeto = obs.buscar_projeto("Culinária Árabe")
if projeto:
    print(f"Antes: {projeto}")
    projeto.concluir()
    print(f"Depois: {projeto}")
