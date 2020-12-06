from __future__ import annotations
from dataclasses import dataclass
from groovy_thing_back.domain.use_cycle import UseCycle
from groovy_thing_back.domain.love_type import LoveType
from uuid import uuid1
from abc import ABCMeta, abstractmethod


@dataclass
class Stuff:
    doc_id: str
    name: str
    use_cycle: UseCycle
    love_type: LoveType
    label: list[str]

    def to_firestore_data(self) -> tuple[str, dict]:
        data = {}
        data['name'] = self.name
        data['label'] = self.label
        data['use_cycle'] = self.use_cycle.label()
        data['love_type'] = self.love_type.label()
        return [self.doc_id, data]


class StuffBuilder:
    _doc_id: str = ''
    _name: str = ''
    _use_cycle: UseCycle = UseCycle.NOT_SELECTED
    _love_type: LoveType = LoveType.NOT_SELECTED
    # TODO: labelを実装
    _label: list[str] = []

    def doc_id(self, value: str) -> None:
        self._doc_id = value

    def name(self, value: str) -> None:
        self._name = value

    def use_cycle(
            self,
            use_cycle: UseCycle,
            love_type: LoveType = None) -> None:
        self._use_cycle = use_cycle
        if use_cycle.is_not_use():
            self._love_type = love_type

    def build(self) -> Stuff:
        data = {}
        data['doc_id'] = self._doc_id if self._doc_id != '' else str(uuid1())
        data['name'] = self._name
        data['label'] = self._label
        data['use_cycle'] = self._use_cycle
        data['love_type'] = self._love_type
        return Stuff(**data)


class StuffRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def all_stuffs(self, group: str) -> list[Stuff]:
        pass

    @abstractmethod
    def find_stuff(self, group: str, stuff: str) -> Stuff:
        pass

    @abstractmethod
    def create(self, group_id: str, stuff: Stuff) -> None:
        pass
