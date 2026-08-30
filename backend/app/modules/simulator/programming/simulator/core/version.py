"""
Informações de versão do núcleo do simulador UAP.

Os quatro contratos originais são preservados:

    VERSION
    NAME
    AUTHOR
    STATUS
"""

VERSION = "0.1.0"

NAME = "Universal Automation Platform"

AUTHOR = "Fernando Burger / OpenAI"

STATUS = "Development"


VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0

VERSION_INFO = (
    VERSION_MAJOR,
    VERSION_MINOR,
    VERSION_PATCH,
)


def get_version():
    return VERSION


def get_name():
    return NAME


def get_author():
    return AUTHOR


def get_status():
    return STATUS


def version_tuple():
    return VERSION_INFO


def version_string():
    return (
        f"{NAME} {VERSION}"
    )


def is_development():
    return (
        STATUS.lower()
        == "development"
    )


def info():
    return {
        "name": NAME,
        "version": VERSION,
        "author": AUTHOR,
        "status": STATUS,
        "version_info": (
            VERSION_INFO
        ),
    }
