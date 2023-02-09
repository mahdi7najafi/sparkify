#Drop Tables
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"


#Create Tables
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, \
start_time timestamp NOT NULL, user_id varchar NOT NULL, level, varchar, song_id varchar, artist_id varchar, \
session_id int, location varchar, user_agent varchar);""")



# Complete the rest of create tables

# Insert Records

# Find Songs


#Query Lists

create_table_queries = [songplay_table_create]
drop_table_queries = [songplay_table_create, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

# add other create tb to this later
