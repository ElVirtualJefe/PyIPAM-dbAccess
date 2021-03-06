from configparser import ConfigParser
from urllib.parse import quote_plus as urlquote

configDB = ConfigParser()
configDB.read("config.ini")
username = configDB.get("postgres","DB_USERNAME")
password = urlquote(configDB.get("postgres","DB_PASSWORD"))
dbname = configDB.get("postgres","DB_NAME")
dbserver = configDB.get("postgres","DB_SERVER")
dbport = configDB.getint("postgres","DB_PORT")

SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{dbserver}:{dbport}/{dbname}"
SQLALCHEMY_TRACK_MODIFICATIONS = False


from logging.config import fileConfig

#from sqlalchemy import engine_from_config
from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from app.models import db
target_metadata = db

compare_type = True
compare_server_default = True

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    #url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=SQLALCHEMY_DATABASE_URI,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type = compare_type,
        compare_server_default = compare_server_default,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    """
    connectable = create_engine(SQLALCHEMY_DATABASE_URI)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            compare_type = compare_type,
            compare_server_default = compare_server_default,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
