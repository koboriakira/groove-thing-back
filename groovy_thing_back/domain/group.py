from __future__ import annotations
from dataclasses import dataclass
from abc import abstractmethod, ABCMeta


@dataclass
class Group:
    id: str
    name: str
    enable_count: bool = False

    def to_firestore_data(self) -> tuple[str, dict]:
        data = {
            "name": self.name, "enable_count": self.enable_count}
        return (self.id, data)


class GroupRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def all_groups(self) -> list[Group]:
        pass

    @abstractmethod
    def find_group(self, doc_id) -> Group:
        pass
