def serialize_data(mapping: dict, data: dict) -> dict:
    """ Serialize a record data to model object dict based
    on given transformation mapping.

    Parameters
    ----------
    `mapping` : <dict>
        A dict object which keeps mapping of model column to
        parameter passed in the `data`
    `data` : <dict>
        A data to be transformed in model dict based on
        given `mapping`

    Return
    ------
    <dict>
        A dict of model object
    """
    serialized_data = dict()
    nullable = ['', None, [], {}, ()]

    for field, f_tuple in mapping.items():
        getter = lambda *a, **k: a and a[0] or None
        key = f_tuple[0]
        evaluated = None
        value = None

        if(len(f_tuple)==2):
            getter = callable(f_tuple[1]) and f_tuple[1] or getter
            value = f_tuple[1] if not callable(f_tuple[1]) else None
        else:
            value = isinstance(key,str) and data.get(key)

        if isinstance(key,(list,tuple)):
            getter_params = [data.get(i) for i in key]
            evaluated = getter(*getter_params)
        elif key != '':
            getter_params = data.get(key)
            evaluated = getter(getter_params)
        elif key == '':
            evaluated = value or getter()

        value = evaluated if (evaluated is not None) else value
        serialized_data.update({field:value})

    return serialized_data
