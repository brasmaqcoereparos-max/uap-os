from app.modules.automation.user_level import (
    user_level,
)


class AutomationWizard:

    def __init__(self):
        self.steps = []
        self.current_step = 0
        self.answers = {}
        self.completed = False

    def add_step(
        self,
        title,
        description,
        key=None,
        options=None,
        required=False,
        icon=None,
    ):
        step = {
            "key": (
                key
                or f"step_{len(self.steps)}"
            ),
            "title": str(title),
            "description": str(
                description
            ),
            "options": list(
                options or []
            ),
            "required": bool(
                required
            ),
            "icon": icon,
        }

        self.steps.append(step)

        return step

    def configure_default_steps(
        self,
        level=None,
    ):
        self.steps.clear()
        self.current_step = 0
        self.answers.clear()
        self.completed = False

        selected = (
            user_level.normalize(level)
            if level is not None
            else user_level.get()
        )

        self.add_step(
            title="O que deseja criar?",
            description=(
                "Escolha o tipo de "
                "automação ou sistema."
            ),
            key="project_type",
            options=[
                "automation",
                "machine",
                "totem",
                "robot",
                "simulation",
                "app",
            ],
            required=True,
            icon="category",
        )

        self.add_step(
            title="Escolha os componentes",
            description=(
                "Selecione sensores, "
                "atuadores, placas e "
                "serviços."
            ),
            key="components",
            required=True,
            icon="components",
        )

        self.add_step(
            title="Monte o funcionamento",
            description=(
                "Conecte os componentes "
                "graficamente."
            ),
            key="flow",
            required=True,
            icon="flow",
        )

        self.add_step(
            title="Simulação",
            description=(
                "Teste graficamente antes "
                "de usar hardware real."
            ),
            key="simulation",
            icon="simulation",
        )

        if (
            selected.value
            != "beginner"
        ):
            self.add_step(
                title="Configurações",
                description=(
                    "Configure parâmetros "
                    "avançados."
                ),
                key="advanced",
                icon="settings",
            )

        if (
            selected.value
            == "professional"
        ):
            self.add_step(
                title="Compilação",
                description=(
                    "Selecione plataforma, "
                    "backend e opções de "
                    "compilação."
                ),
                key="compiler",
                icon="compiler",
            )

        self.add_step(
            title="Validar e executar",
            description=(
                "Valide o projeto e "
                "prepare a execução."
            ),
            key="finish",
            icon="check",
        )

        return self.steps

    def answer(
        self,
        value,
        key=None,
    ):
        step = self.current()

        if step is None:
            return False

        selected_key = (
            key
            or step["key"]
        )

        self.answers[
            selected_key
        ] = value

        return True

    def can_advance(self):
        step = self.current()

        if step is None:
            return False

        if not step.get(
            "required",
            False,
        ):
            return True

        return step["key"] in (
            self.answers
        )

    def next(self):
        if not self.steps:
            return None

        if not self.can_advance():
            return self.current()

        if (
            self.current_step
            < len(self.steps) - 1
        ):
            self.current_step += 1
        else:
            self.completed = True

        return self.current()

    def previous(self):
        if self.current_step > 0:
            self.current_step -= 1

        self.completed = False

        return self.current()

    def go_to(
        self,
        index,
    ):
        if not self.steps:
            return None

        index = max(
            0,
            min(
                int(index),
                len(self.steps) - 1,
            ),
        )

        self.current_step = index
        self.completed = False

        return self.current()

    def current(self):
        if not self.steps:
            return None

        return dict(
            self.steps[
                self.current_step
            ]
        )

    def progress(self):
        if not self.steps:
            return 0.0

        if self.completed:
            return 100.0

        return round(
            (
                self.current_step
                / max(
                    1,
                    len(self.steps) - 1,
                )
            )
            * 100,
            2,
        )

    def result(self):
        return {
            "completed": self.completed,
            "current_step": (
                self.current_step
            ),
            "total_steps": (
                len(self.steps)
            ),
            "progress": self.progress(),
            "answers": dict(
                self.answers
            ),
        }

    def reset(self):
        self.current_step = 0
        self.answers.clear()
        self.completed = False


automation_wizard = AutomationWizard()
