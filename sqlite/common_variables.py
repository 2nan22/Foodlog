STR_CREATE_TABLE_PLACE = '''
CREATE TABLE IF NOT EXISTS Places
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_name TEXT NOT NULL,
    place_nickname TEXT,
    address TEXT NOT NULL,
    memo TEXT,
    place_type_id TEXT,
    place_type TEXT,
    latitude TEXT,
    longitude TEXT,
    create_time TEXT,
    last_update_time TEXT,
    folder_id INTEGER NOT NULL,
    folder_name TEXT NOT NULL
)
'''
STR_CREATE_TABLE_EVALUATE = '''
CREATE TABLE IF NOT EXISTS Evaluate
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    folder_id INTEGER NOT NULL,
    folder_name TEXT NOT NULL,
    count INTEGER NOT NULL
)
'''
STR_INSERT_PLACE = """
INSERT INTO Places 
(
    place_name, 
    place_nickname, 
    address, 
    memo, 
    place_type_id, 
    place_type, 
    latitude, 
    longitude, 
    create_time, 
    last_update_time,
    folder_id,
    folder_name
) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
STR_INSERT_EVALUATE = """
INSERT INTO Evaluate
(   
    folder_id,
    folder_name,
    count
)
    VALUES (?, ?, ?)
"""