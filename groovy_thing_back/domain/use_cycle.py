from __future__ import annotations
import enum


class UseCycle(enum.Enum):
    TRUST = enum.auto(), '預かり'
    SEASON = enum.auto(), '季節'
    YEARLY = enum.auto(), '年数回'
    MONTHLY = enum.auto(), '月1回'
    WEEKLY = enum.auto(), '週1回'
    DAILY = enum.auto(), '毎日'
    NOT_USE = enum.auto(), '使わない'
    NOT_SELECTED = enum.auto(), '未選択'

    def is_not_use(self) -> bool:
        return self is UseCycle.NOT_USE

    def is_use(self) -> bool:
        return self not in [UseCycle.NOT_USE, UseCycle.NOT_SELECTED]

    def id(self) -> int:
        return self.value[0]

    def label(self) -> str:
        return self.value[1]

    @classmethod
    def to_enum_by_number(cls, num: int) -> UseCycle:
        for use_cycle in UseCycle:
            if use_cycle.id() == num:
                return use_cycle
        raise ValueError(f'Not found: {num}')

    @classmethod
    def to_enum_by_string(cls, string: str) -> UseCycle:
        for use_cycle in UseCycle:
            if use_cycle.label().lower() == string.lower():
                return use_cycle
        raise ValueError(f'Not found: {string}')
