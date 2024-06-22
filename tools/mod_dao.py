import sqlite3
def create_db_and_table():
    conn = sqlite3.connect('EmergencyRooms.db')
    cursor = conn.cursor()
    ##institution_id is the 'fichenro' coming from website
    cursor.execute('''CREATE TABLE IF NOT EXISTS institutions (
                      institution_id INTEGER PRIMARY KEY, 
                      name TEXT,
                      street TEXT,
                      city TEXT,
                      postal_code TEXT,
                      region TEXT
                    )'''
                    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS situations (
                         id INTEGER PRIMARY KEY autoincrement unique,
                         institution_id INTEGER NOT NULL,
                         wait_non_priority TEXT,
                         waiting_to_see_doctor TEXT,
                         total_people TEXT,
                         occupancy_rate TEXT,
                         avg_wait_room TEXT,
                         avg_wait_stretcher TEXT,
                         last_update TEXT,
                         FOREIGN KEY (institution_id) REFERENCES institutions(institution_id)
                       )'''
                   )
    conn.commit()
    conn.close()

def insert_into_db(data):
    conn = sqlite3.connect('EmergencyRooms.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT OR REPLACE INTO institutions (institution_id, name, street, city, postal_code, region) 
                      VALUES (?, ?, ?, ?, ?, ?)''', (data['id'],  data['name'] , data['street'], data['city'], data['postal_code'], data['region']))
    conn.commit()
    conn.close()

    # , wait_non_priority, waiting_to_see_doctor, total_people, occupancy_rate, avg_wait_room, avg_wait_stretcher, last_update