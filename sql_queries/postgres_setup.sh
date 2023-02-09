#!/usr/bin/bash

# connect to the PostgreSQL server using the default postgres user
psql -h 127.0.0.1 -U postgres << EOF

# Create a new user 'mahdi'
CREATE USER mahdi;

#Set the password for the user 'mahdi' to 'test1234'
ALTER USER mahdi WITH PASSWORD 'test1234';

EOF
echo "User 'mahdi' created successfully with password 'test1234'"
