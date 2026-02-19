from dependency_injector.containers import DeclarativeContainer, WiringConfiguration


class Dependency(DeclarativeContainer):
    wiring_modules = []
    wiring_config = WiringConfiguration(modules=wiring_modules, warn_unresolved=True)
