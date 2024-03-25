class File:
    def __init__(self, file_name):
        self.fileName = file_name
        self.marked_for_deletion = False

    def __str__(self):
        return ("file_name: " + self.fileName + ", marked_for_deletion: " +
                ('true' if self.marked_for_deletion else 'false'))

    def __repr__(self):
        return ("file_name: " + self.fileName + ", marked_for_deletion: " +
                ('true' if self.marked_for_deletion else 'false'))
