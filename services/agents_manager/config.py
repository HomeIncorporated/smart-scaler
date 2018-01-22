"""
Configurations for service AgentsManager
"""


class Default:
    """
    Default configuration.
    """
    DEBUG = True

    LOG_LEVEL = "INFO"

    API_GATEWAY_HOST = "localhost"
    API_GATEWAY_PORT = 18001

    AGENTS_MANAGER_HOST = "localhost"
    AGENTS_MANAGER_PORT = 18002

    REPO_MANAGER_HOST = "localhost"
    REPO_MANAGER_PORT = 18003

    KUBERNETES_HOST = "localhost"
    KUBERNETES_PORT = 18008
    KUBERNETES_PULL = 20  # seconds

    REDIS_HOST = "localhost"
    REDIS_PORT = 18009


class Debug(Default):
    """
    Debug configuration.
    """
    DEBUG = True

    LOG_LEVEL = "DEBUG"


class Production(Default):
    """
    Production configuration.
    """
    DEBUG = False