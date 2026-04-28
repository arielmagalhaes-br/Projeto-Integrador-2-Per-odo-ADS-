from models.projeto import ProjetoIntegrador


class Observatorio:
    def __init__(self):
        self.projetos = []

    def adicionar_projeto(self, titulo, curso, periodo, descricao=""):
        projeto = ProjetoIntegrador(titulo, curso, periodo, descricao)
        self.projetos.append(projeto)
        return projeto

    def listar_projetos(self):
        lista = []
        for p in self.projetos:
            lista.append(p.to_dict())
        return lista

    def buscar_projeto(self, titulo):
        for p in self.projetos:
            if p.titulo.lower() == titulo.strip().lower():
                return p
        return None

    def filtrar_por_curso(self, curso):
        resultado = []
        for p in self.projetos:
            if p.curso.lower() == curso.strip().lower():
                resultado.append(p)
        return resultado
