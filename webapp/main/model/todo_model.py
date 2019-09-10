from mongoengine import *

class Todo(Document):
    _id = StringField
    uuid = UUIDField()
    todo = StringField(max_length=400, required=True)
    done = BooleanField()

    def __repr__(self):
        return '{} {} {} {}'.format(self._id, self.uuid, self.todo, self.done)