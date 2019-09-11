from mongoengine import *

class Todo(Document):
    _id = StringField
    uuid = UUIDField()
    label = StringField(max_length=400, required=True)
    description = StringField(required=True)
    done = BooleanField()

    def __repr__(self):
        return '{} {} {} {} {}'.format(self._id, self.uuid, self.label, self.description, self.done)