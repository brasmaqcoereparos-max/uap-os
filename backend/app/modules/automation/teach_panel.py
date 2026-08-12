class TeachPanel:

    def __init__(self):

        self.buttons = [
            "JOG",
            "GRAVAR",
            "APAGAR",
            "EDITAR",
            "REPRODUZIR",
            "PAUSAR",
            "PARAR",
            "SALVAR",
        ]

    def get_buttons(self):

        return list(
            self.buttons
        )

    def has_button(self, name):

        return name in self.buttons


teach_panel = TeachPanel()
