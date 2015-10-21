import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('/opt/wfp/config.conf'))

g = {
    # DATABASE INFO
    'POSTGRES_HOST': config.get('warehouse', 'POSTGRES_HOST'),
    'POSTGRES_USER': config.get('warehouse', 'POSTGRES_USER'),
    'POSTGRES_PWD': config.get('warehouse', 'POSTGRES_PWD'),
    'POSTGRES_DB': config.get('warehouse', 'POSTGRES_DB'),
}