from groovy_thing_back.adapter.group.stuff_firestore_repository import StuffFirestoreRepository
from groovy_thing_back.domain.stuff import StuffRepository
from groovy_thing_back.domain.group import GroupRepository
from groovy_thing_back.adapter.group.group_firestore_repository import GroupFirestoreRepository


def create_config(params: dict):
    u""" inject 用の config を生成する
    :param dict params: パラメータの辞書
    :return function: inject 用の config 関数
    """
    def config(binder):
        binder.bind_to_constructor(GroupRepository, GroupFirestoreRepository)
        binder.bind_to_constructor(StuffRepository, StuffFirestoreRepository)
    return config
