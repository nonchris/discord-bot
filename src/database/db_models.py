"""
From SQLAlchemy quickstart gist by
https://github.com/nonchris/

Link to gist:
https://gist.github.com/nonchris/046f58bcefdcea5606f670b74f375254

discord bot template:
https://github.com/nonchris/discord-bot
"""

# core interface to the database
import os
import logging

import sqlalchemy.orm
from sqlalchemy import create_engine, Boolean
# base contains a metaclass that produces the right table
from sqlalchemy.ext.declarative import declarative_base
# setting up a class that represents our SQL Database
from sqlalchemy import Column, Integer, String, DateTime
# prints if a table was created - neat check for making sure nothing is overwritten
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker

if not os.path.exists('data/'):
    os.mkdir('data/')

# set echo=False to disable prints by SQLAlchemy
engine = create_engine('sqlite:///data/main.db', echo=True)
Base: declarative_base = declarative_base()

logger = logging.getLogger('my-bot')


# TODO: Decide whether this db matches your needs
# This class tries to be as generic and widely usable as possible, you should configure it to your bot before usage
class Settings(Base):
    __tablename__ = 'SETTINGS'

    id = Column(Integer, primary_key=True)  # to make each setting unique
    guild_id = Column(Integer)    # ID of guild setting is for
    channel_id = Column(Integer)  # to make settings per channel possible
    setting = Column(String)  # type of setting - example: mod-role
    value = Column(String)    # setting value - example: id of a role that shall have moderator 
    fist_param = Column(String)  # maybe needed for some extra information about setting
    set_by = Column(Integer)  # user id of person who set entry - good for potential logging
    last_changed = Column(DateTime)
    active = Column(Boolean)  # to not delete unused settings and rather deactivate them -> better logging?

    def __repr__(self):
        return f"<Setting: guild='{self.guild_id}', setting='{self.setting}'," \
               f"value='{self.value}', 'value_param'={self.fist_param}, active='{self.active}' set_by='{self.set_by}'" \
               f"last_changed='{self.last_changed}', id='{self.id}'>"


# TODO: PUT YOUR ADDITIONAL TABLES HERE


@event.listens_for(Base.metadata, 'after_create')
def receive_after_create(target, connection, tables, **kw):
    """!
    listen for the 'after_create' event
    """
    logger.info('A table was created' if tables else 'No table was created')
    print('A table was created' if tables else 'No table was created')


def open_session() -> sqlalchemy.orm.Session:
    """
    @return new active SQLAlchemy session
    """
    return sessionmaker(bind=engine)()


# creating db which doesn't happen when it should?
database = Base.metadata.create_all(bind=engine)
