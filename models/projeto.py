class ProjetoIntegrador:
    def __init__(self, titulo, curso, periodo, descricao=""):
        if not titulo or not titulo.strip():
            raise ValueError("O título do projeto não pode ser vazio.")
        if not curso or not curso.strip():
            raise ValueError("O curso do projeto não pode ser vazio.")
        if not periodo or not periodo.strip():
            raise ValueError("O período do projeto não pode ser vazio.")

        self.titulo = titulo.strip()
        self.curso = curso.strip()
        self.periodo = periodo.strip()
        self._descricao = descricao.strip()
        self.status = "Em andamento"

    def get_descricao(self):
        return self._descricao

    def alterar_descricao(self, nova_descricao):
        self._descricao = nova_descricao.strip()

    def concluir(self):
        self.status = "Concluído"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "curso": self.curso,
            "periodo": self.periodo,
            "descricao": self._descricao,
            "status": self.status
        }

    def __str__(self):
        return f"[{self.periodo}] {self.titulo} - {self.curso} ({self.status})"