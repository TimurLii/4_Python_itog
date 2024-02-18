import text
import view
import model
import os

my_notes = model.Notes(os.path.dirname(__file__) + "\\" + text.notes_file_name)


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                my_notes.load_notes()
                view.print_message(text.load_successful)
            case 2:
                my_notes.save_notes()
                view.print_message(text.save_successful)
            case 3:
                notes = my_notes.get_notes()
                view.print_notes(notes, text.load_error)
            case 4:
                note = view.input_notes(my_notes.get_max_id(),
                                        text.input_new_note, text.cancel_input)
                title = my_notes.add_note(note)
                view.print_message(text.new_note_successful(title))  # type: ignore
            case 5:
                notes = my_notes.get_notes()
                index = view.input_index(text.input_index, notes, text.load_error)
                note = view.input_notes(index,
                                        text.input_new_note, text.cancel_input)
                result = my_notes.change_notes(note, index)
            case 6:
                notes = my_notes.get_notes()
                index = view.input_index(
                    text.index_del_note, notes, text.load_error)
                title = my_notes.del_note(index)
                view.print_message(text.del_note(title))  # type: ignore
            case 7:
                break
