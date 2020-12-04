from __future__ import annotations
import enum


class LoveType(enum.Enum):
    # valueはID、ラベル、愛している／愛していない
    MEMORY = enum.auto(), '思い出', True
    COLLECTION = enum.auto(), 'コレクション', True
    CONSTRAINTS = enum.auto(), 'しがらみ', False
    EXPENSIVE = enum.auto(), '高値', False
    WASTE = enum.auto(), '意地', False
    HARD_TO_TRASH = enum.auto(), '捨てにくい', False
    NOT_SELECTED = enum.auto(), '未選択', False

    def id(self) -> int:
        return self.value[0]

    def label(self) -> str:
        return self.value[1]

    @classmethod
    def to_enum_by_number(cls, num: int) -> LoveType:
        for love_type in LoveType:
            if love_type.id() == num:
                return love_type
        raise ValueError(f'Not found: {num}')

    @classmethod
    def to_enum_by_string(cls, string: str) -> LoveType:
        for love_type in LoveType:
            if love_type.label().lower() == string.lower():
                return love_type
        raise ValueError(f'Not found: {string}')
