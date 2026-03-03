from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton
from src.domain.services.qfieldcloud import QFieldCloudService


class Container(DeclarativeContainer):
    wiring_modules = [
        "src.api.routes.project",
        "src.api.routes.auth",
        "src.api.routes.user",
    ]
    wiring_config = WiringConfiguration(modules=wiring_modules, warn_unresolved=True)

    # Services
    qfieldcloud_service = Singleton(QFieldCloudService)
