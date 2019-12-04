
from uperations.library import Library
from .operations.CreateDatabase import Createdatabase
from .operations.Migrate import Migrate

class Admin(Library):

    @staticmethod
    def name():
        return "admin"

    @staticmethod
    def description():
        return "Not description provided"

    def _init_operations(self):
        self._operations = {
            'create:database': Createdatabase(self),
            'migrate': Migrate(self)
            # operation_command: OperationClass(self)
        }
        return

    def operations(self):
        return self._operations