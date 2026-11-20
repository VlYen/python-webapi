from typing import Any, Callable, cast

from repositories.ProtocolRepository import ProtocolRepository

class RepositoryFactory:

    def __init__(self):
        self._registry: dict[type[Any], Callable[[], Any]] = {}

    def register[T](
        self,
        entity_type: type[T],
        creator: Callable[[], ProtocolRepository[T]]
    ) -> None:
        self._registry[entity_type] = creator

    def get_repository[T](
        self,
        entity_type: type[T]
    ) -> ProtocolRepository[T]:

        creator = self._registry.get(entity_type)

        if creator is None:
            raise ValueError(
                f"No repository registered for {entity_type.__name__}"
            )

        return cast(ProtocolRepository[T], creator())