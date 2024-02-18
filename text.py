main_menu = '''\nMenu:
		1. Open file • 
		2. Write a file •
		3. Show notes •
		4. Add a note •
		5. Edit a note •
		6. Delete a note  •
		7. Exit •\n '''

input_choice = 'Enter the command: '
notes_file_name = 'note.csv'

load_successful = 'All notes are shown'
save_successful = 'The notes are saved'

cancel_input = 'Canceling the input'

load_error = 'There are no notes'
input_new_note = 'Enter the contact details:'
new_notes = {'title': 'The name of the note: ',
             'note': 'Enter the text of the note: '}


def new_note_successful(title: str):
    return f'Note {title} added.'


cancel_input = 'Canceling the input.'

index_del_note = 'Index of the note to delete: '


def del_note(title: str):
    return f'Notes {title} deleted!'


# input_change = 'Какую заметку хотите изменить? '
input_index = 'Index of the note: '

change_note = 'Enter new data or leave the fields empty so as not to change them: '


def change_successful(title: str | dict) -> str:
    return f'The note{title} has been changed'


input_search = 'Which note to find? '


def empty_search(word) -> str:
    return f'the note with the word{word} was not found'
