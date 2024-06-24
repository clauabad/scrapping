import sqlite3

from models.mood_classes import Institution, Situation


def create_db_and_table():
    conn = get_connexion()
    cursor = conn.cursor()

    ##Allow foreign key
    cursor.execute('PRAGMA foreign_keys = ON;')

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
                         UNIQUE (institution_id, last_update) ON CONFLICT REPLACE
                       )'''
                   )
    conn.commit()
    conn.close()

def insert_or_update_into_db(institution: Institution, situation: Situation):
    conn = get_connexion()
    cursor = conn.cursor()

    cursor.execute('''INSERT OR REPLACE INTO institutions (institution_id, name, street, city, postal_code, region) 
                      VALUES (?, ?, ?, ?, ?, ?)''', (institution.institution_id,  institution.name , institution.street,
                                                     institution.city, institution.postal_code, institution.region))

    conn.commit()

    cursor.execute(''' INSERT OR REPLACE INTO situations (institution_id, wait_non_priority, waiting_to_see_doctor, total_people, 
                            occupancy_rate, avg_wait_room, avg_wait_stretcher, last_update) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (situation.institution_id,  situation.wait_non_priority , situation.waiting_to_see_doctor,
                                                     situation.total_people, situation.occupancy_rate, situation.avg_wait_room, situation.avg_wait_stretcher,
                                                     situation.last_update))
    conn.commit()
    conn.close()

def get_connexion():
    conn = sqlite3.connect('EmergencyRooms.db')
    return conn
