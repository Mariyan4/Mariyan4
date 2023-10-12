def sort_to_do_notes(notes):
    sorted_notes = []

    while notes:
        max_importance = max(note.split('-')[0] for note in notes)
        max_importance_note = notes.pop(notes.index(max_importance + '-' + max_importance_note.split('-')[1]))
        sorted_notes.insert(0, max_importance_note)

        return sorted_notes
notes = []

while True:
    note = input()

    if note == 'End':
        break
    notes.append(note)
sorted_notes = sort_to_do_notes(notes)
for note in sorted_notes:
    print(note)