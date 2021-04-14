def convert_bool(cad):
    return cad in ['true', '1', 'True', 1]


def convert_float(cad):
    return float(str(cad).replace(',', ''))


def clean_dataframe(df):
    # replace spaces with underscore in names columns
    df.columns = df.columns.str.replace(' ', '_')

    # lowercase in names columns
    df.columns = df.columns.str.lower()

    # rename - the word 'global' conflicts with the reserved words
    df = df.rename({'global': 'global_oh'}, axis=1)
    df = df.replace(to_replace={'[NULL]': 0})
    df = df.fillna(0)
    return df
