#!/bin/bash

# Check if the table force_name already exists
if [[ $(mysql -u your_username -p -e "USE $1; DESCRIBE force_name;" 2>/dev/null) ]]; then
  echo "The table force_name already exists in the database $1."
else
  # Create the table if it doesn't exist
  mysql -u your_username -p $1 <<EOF
  CREATE TABLE force_name (
    id INT,
    name VARCHAR(256) NOT NULL
  );
EOF
  echo "Table force_name has been created in the database $1."
fi
