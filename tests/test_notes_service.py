import unittest
from unittest.mock import *
from src.note.notes_storage import NotesStorage
from src.note.notes_service import NotesService
from src.note.note import Note


class TestNotesService(unittest.TestCase):
    def test_average_of(self):
        notes_storage = NotesStorage()
        notes_storage.get_all_notes_of = Mock(
            name='get_all_notes_of',
            side_effect=(
                lambda name: name == 'Jack'
                and [Note('Jack', 5.0), Note('Jack', 3.0), Note('Jack', 5.5)]
            )
        )

        notes_service = NotesService(notes_storage)
        self.assertEqual(notes_service.average_of('Jack'), 4.5)

    def test_average_of_no_notes(self):
        notes_storage = NotesStorage()
        notes_storage.get_all_notes_of = Mock(name='get_all_notes_of')
        notes_storage.get_all_notes_of.return_value = []

        notes_service = NotesService(notes_storage)
        with self.assertRaisesRegex(ZeroDivisionError, '^No notes for this name$'):
            notes_service.average_of('John')

    def test_add(self):
        notes_storage = NotesStorage()
        notes_storage.add = Mock(
            name='add',
            side_effect=(lambda note: note)
        )

        notes_service = NotesService(notes_storage)
        self.assertIsInstance(notes_service.add(Note('George', 6.0)), Note)

    def test_add_wrong_type(self):
        def check_note(note):
            if not isinstance(note, Note):
                raise TypeError('Note must be a Note object')

        notes_storage = NotesStorage()
        notes_storage.add = Mock(
            name='add',
            side_effect=check_note
        )

        notes_service = NotesService(notes_storage)
        with self.assertRaisesRegex(TypeError, '^Note must be a Note object$'):
            notes_service.add(6.0)

    def test_clear(self):
        notes = [Note('Jack', 5.0), Note('George', 3.0), Note('Jack', 5.5)]

        notes_storage = NotesStorage()
        notes_storage.clear = Mock(name='clear')
        notes_storage.clear.return_value = notes

        notes_service = NotesService(notes_storage)
        self.assertListEqual(notes_service.clear(), notes)


if __name__ == '__main__':
    unittest.main()
