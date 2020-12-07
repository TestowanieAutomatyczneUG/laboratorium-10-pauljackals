class Note:
    def __init__(self, name, note):
        if type(name) != str:
            raise TypeError('Name must be a string')
        if name == '':
            raise ValueError('Name must not be empty')
        if type(note) != float:
            raise TypeError('Note must be a float')
        if note < 2 or note > 6:
            raise ValueError('Note must be between 2 and 6 (inclusive)')
        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
