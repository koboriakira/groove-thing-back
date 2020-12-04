from google.cloud import firestore
from google.cloud.firestore_v1.document import DocumentSnapshot
from groovy_thing_back.domain.stuff import Stuff, StuffRepository

db = firestore.Client()
BASIS_COLLECTION = 'groovy'
COLLECTION = 'stuffs'


class StuffFirestoreRepository(StuffRepository):
    def all_stuffs(self, group: str) -> list[Stuff]:
        docs = db.collection(BASIS_COLLECTION).document(
            group).collection(COLLECTION).stream()
        doc: DocumentSnapshot
        return list(map(lambda doc: _to_model(doc=doc), docs))

    def find_stuff(self, group: str, stuff: str) -> Stuff:
        doc: DocumentSnapshot = db.collection(BASIS_COLLECTION).document(
            group).collection(COLLECTION).document(stuff).get()
        if not doc.exists:
            return None
        return _to_model(doc=doc)

    def create(self, group: str, doc_id: str, data: dict) -> None:
        doc_ref = db.collection(BASIS_COLLECTION).document(
            group).collection(COLLECTION).document(doc_id)
        if doc_ref.get().exists:
            raise ValueError('すでに存在するデータです')
        doc_ref.set(data)


def _to_model(doc: DocumentSnapshot) -> Stuff:
    data = doc.to_dict()
    data["doc_id"] = doc.id
    return Stuff(**data)
