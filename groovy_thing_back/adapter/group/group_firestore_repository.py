from google.cloud import firestore
from google.cloud.firestore_v1.document import DocumentSnapshot
from groovy_thing_back.domain.group import Group, GroupRepository

db = firestore.Client()
COLLECTION = 'groovy'


class GroupFirestoreRepository(GroupRepository):
    def all_groups(self) -> list[Group]:
        docs = db.collection(COLLECTION).stream()
        doc: DocumentSnapshot
        return list(map(lambda doc: _to_model(doc=doc), docs))

    def find_group(self, doc_id: str):
        doc: DocumentSnapshot = db.collection(
            COLLECTION).document(doc_id).get()
        if not doc.exists:
            return None
        return _to_model(doc=doc)


def _to_model(doc: DocumentSnapshot) -> Group:
    data: dict = doc.to_dict()
    data["id"] = doc.id
    return Group(**data)
