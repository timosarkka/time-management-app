# Import needed libraries and functions

from configparser import ConfigParser

# Define the function config to read the database.ini file and return the parameters of the PostgreSQL database

def config(filename='src\\data\\database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db= {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db