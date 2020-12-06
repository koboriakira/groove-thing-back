from groovy_thing_back.domain.love_type import LoveType
from groovy_thing_back.domain.use_cycle import UseCycle
from groovy_thing_back.domain.stuff import Stuff, StuffBuilder, StuffRepository
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import inject
from groovy_thing_back.injector import create_config
from groovy_thing_back.domain.group import Group, GroupRepository
import logging

logging.basicConfig(level=logging.DEBUG)

inject.configure(create_config({}))

app = FastAPI()
# CORSを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)


class StuffBody(BaseModel):
    name: str
    use_cycle: Optional[str]
    love_type: Optional[str]
    label: Optional[list[str]]


@app.get("/groups/")
def all_groups():
    groups: list[Group] = inject.instance(GroupRepository).all_groups()
    return {"groups": groups}


@app.get("/{group_id}")
def get_group(group_id: str):
    group: Group = inject.instance(
        GroupRepository).find_group(doc_id=group_id)
    return group


@app.get("/{group_id}/stuffs")
def get_stuffs(group_id: str):
    stuffs: list[Stuff] = inject.instance(
        StuffRepository).all_stuffs(group=group_id)
    return {"stuffs": stuffs}


@app.get("/{group_id}/stuffs/{stuff_id}")
def get_stuff(group_id: str, stuff_id: str):
    stuff: Stuff = inject.instance(
        StuffRepository).find_stuff(group=group_id, stuff=stuff_id)
    return stuff


@ app.post("/{group}/stuffs")
def add_stuff(group: str, body: StuffBody):
    builder = StuffBuilder()
    builder.name(value=body.name)
    if body.use_cycle is not None:
        use_cycle = UseCycle.to_enum_by_string(string=body.use_cycle)
        builder.use_cycle(use_cycle=use_cycle)
    if body.love_type is not None:
        love_type = LoveType.to_enum_by_string(string=body.love_type)
        builder.use_cycle(use_cycle=UseCycle.NOT_USE, love_type=love_type)
    stuff = builder.build()
    firestore_data = stuff.to_firestore_data()
    inject.instance(StuffRepository).create(
        group=group, doc_id=firestore_data[0], data=firestore_data[1])
    return {"isSuccess": True}
