

def cursor_to_dict(results, descriptions):
    """
    Convert django raw sql query into a list of dictionaries, easy to navigate and parse in templates.
    #model manager
    return cursor.execute('''SELECT first AS first_name,
    ...                              last AS last_name,
    ...                              bd AS birth_date,
    ...                              pk AS id,
    ...                       FROM some_other_table''')
    #model
    cursor = Person.objects.get_cursor_data()
    qs = cursor_to_dict(cursor.fetchall(), cursor.description)
    """

    output = []
    for data in results:
        row = {}
        i = 0
        for column in descriptions:
            row[column[0]] = data[i]
            i += 1

        output.append(row)
    return output
