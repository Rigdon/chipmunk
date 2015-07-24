from __future__ import unicode_literals
from contextlib import contextmanager
from threading import local

_thread_locals = local()


class _Chipmunk(object):
    """
    This is a global storage utility class with a very silly name. It uses a thread local object for storage in order
    to isolate data. It avoids the issue of global namespace conflicts by not allowing you to assign a value to an
    attribute that already exists. Also implements the `in` operator to test for inclusion and the bool() method to
    test whether the Chipmunk is holding anything.
    """
    __locals = _thread_locals

    def __repr__(self):
        return "Chipmunk"

    def __str__(self):
        return str("Global Chipmunk Object")

    def __unicode__(self):
        return "Global Chipmunk Object"

    def __contains__(self, item):
        """
        Test whether a value with the given name has been stored already.
        """
        return hasattr(self.__class__.__locals, item)

    def __nonzero__(self):
        return bool(self.__class__.__locals.__dict__)

    def __getattribute__(self, name):
        """
        Provide access to the stored attributes with the simple attribute access method (Chipmunk.attr)
        """
        accessible_attributes = {
            'store_data', 'get_data', 'delete_data', 'hold_this',
            'empty', '_Chipmunk__locals', '__class__'
        }
        if name in accessible_attributes:
            return object.__getattribute__(self, name)
        return self.get_data(name)

    def __setattr__(self, name, value):
        """
        Store all assigned attributes in the thread local object.
        """
        return self.store_data(name, value)

    def __delattr__(self, name):
        """
        Remove deleted attributes from the thread local object.
        """
        return self.delete_data(name)

    @classmethod
    def store_data(cls, name, data):
        """
        Store the attribute in the thread local object if none witht he same name exist.
        """
        if hasattr(cls.__locals, name):
            raise AttributeError("Chipmunk can't store attribute \"%s\", it's already holding one." % name)

        setattr(cls.__locals, name, data)

    @classmethod
    def get_data(cls, name, default=None):
        """
        Retrieve the desired attribute from the thread local object or the given default value
        """
        data = getattr(cls.__locals, name, default)
        return data

    @classmethod
    def delete_data(cls, name):
        """
        Deletes the attribute with the given name from the thread local object
        """
        try:
            return delattr(cls.__locals, name)
        except AttributeError:
            return None

    @classmethod
    def empty(cls):
        cls.__locals.__dict__.clear()

    @contextmanager
    def hold_this(self, name, data):
        """
        Tell the Chipmunk to hold some data. If it is already holding something with the same name it will pop that
        object off on entry, store the new data, and then replace the data when the context manager is done.
        """
        if name in self:
            old_value = self.get_data(name)
            self.delete_data(name)

        self.store_data(name, data)
        try:
            yield
        finally:
            self.delete_data(name)
            try:
                self.store_data(name, old_value)
            except NameError:
                pass


Chipmunk = _Chipmunk()
