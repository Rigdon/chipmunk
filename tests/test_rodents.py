import threading
from unittest import TestCase
from chipmunk import Chipmunk


class ChipmunkTestCase(TestCase):

    def setUp(self):
        Chipmunk._Chipmunk__locals.__dict__.clear()
        super(ChipmunkTestCase, self).setUp()

    def tearDown(self):
        super(ChipmunkTestCase, self).tearDown()

    def test_that_chipmunk_can_hold_nut(self):
        Chipmunk.a = "acorn"
        self.assertEqual("acorn", Chipmunk.a)
        Chipmunk.store_data('b', "walnut")
        self.assertEqual("walnut", Chipmunk.b)

    def test_that_chipmunk_empty_clears_all_data(self):
        Chipmunk.a = "acorn"
        Chipmunk.b = "walnut"
        self.assertEqual("acorn", Chipmunk.a)
        self.assertEqual("walnut", Chipmunk.b)
        Chipmunk.empty()
        self.assertIsNone(Chipmunk.a)
        self.assertIsNone(Chipmunk.b)

    def test_chipmunk_values_are_local_to_thread(self):
        def thread_func():
            self.assertIsNone(Chipmunk.a)
            Chipmunk.b = "walnut"

        t = threading.Thread(target=thread_func)
        t.start()
        self.assertIsNone(Chipmunk.b)
        Chipmunk.a = "acorn"
        self.assertEqual("acorn", Chipmunk.a)
        t2 = threading.Thread(target=thread_func)
        t2.start()

    def test_chipmunk_will_not_replace_existing_attribute(self):
        Chipmunk.a = "acorn"
        with self.assertRaises(AttributeError):
            Chipmunk.a = "walnut"
        with self.assertRaises(AttributeError):
            Chipmunk.store_data('a', "acorn")

    def test_chipmunk_in_operator(self):
        self.assertFalse('a' in Chipmunk)
        self.assertFalse(hasattr(Chipmunk._Chipmunk__locals, 'a'))
        Chipmunk.a = 5
        self.assertTrue('a' in Chipmunk)
        self.assertTrue(hasattr(Chipmunk._Chipmunk__locals, 'a'))

    def test_chipmunk_delete_attributes(self):
        Chipmunk.a = 5
        self.assertIn('a', Chipmunk)
        del Chipmunk.a
        self.assertNotIn('a', Chipmunk)
        Chipmunk.a = 5
        self.assertIn('a', Chipmunk)
        Chipmunk.delete_data('a')
        self.assertNotIn('a', Chipmunk)
        # This is to make sure it doesn't throw any errors when trying to delete a nonexistent attribute
        self.assertIsNone(Chipmunk.delete_data('a'))
        self.assertIsNone(Chipmunk.delete_data('a'))

    def test_chipmunk_boolean_method(self):
        self.assertFalse(Chipmunk)
        Chipmunk.a = "acorn"
        self.assertTrue(Chipmunk)

    def test_chipmunk_context_manager_no_prior_value(self):
        self.assertIsNone(Chipmunk.a)
        with Chipmunk.hold_this('a', "acorn"):
            self.assertEqual("acorn", Chipmunk.a)
        self.assertIsNone(Chipmunk.a)

    def test_chipmunk_context_manager_with_prior_value(self):
        self.assertIsNone(Chipmunk.a)
        Chipmunk.a = "walnut"
        self.assertEqual("walnut", Chipmunk.a)
        with Chipmunk.hold_this('a', "acorn"):
            self.assertEqual("acorn", Chipmunk.a)
        self.assertEqual("walnut", Chipmunk.a)

