table_name = 'store'

def read_all_query():
    return f"SELECT * FROM {table_name}"

def create_row_query(data_list):
    values_string = ", ".join(map(str, data_list))
    return f"""
    INSERT INTO {table_name}
    VALUES ({values_string});
    """

def update_rows_query(column_value_pair, filter_expression):
    return f"""
    UPDATE {table_name}
    SET {column_value_pair}
    WHERE {filter_expression};
    """

def delete_rows_query(filter_expression):
    return f"""
    DELETE FROM {table_name} 
    WHERE {filter_expression};
    """