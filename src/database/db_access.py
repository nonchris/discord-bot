"""
Written by:
https://github.com/nonchris/
"""
import datetime
import logging
from typing import Union, List

from sqlalchemy import select, and_, delete

import database.db_models as db

logger = logging.getLogger('my-bot')


def get_settings_for(guild_id: int, setting: str, session=db.open_session()) -> Union[List[db.Settings], None]:
    """!
    Searches db for setting in a guild that matches the setting name

    @param guild_id id of the guild to search for
    @param setting name of the setting to search for e.g. "mod-role"
    @param session session to search with, helpful if object shall be edited, since the same session is needed for this
    @return list of settings that match the given given setting name
    """

    sel_statement = select(db.Settings).where(
        and_(
            db.Settings.guild_id == guild_id,
            db.Settings.setting == setting
        )
    )
    entries = session.execute(sel_statement).all()
    return [entry[0] for entry in entries] if entries else None


def get_setting_by_main_attributes(guild_id: int, setting: str, value: str,
                                   session=db.open_session()) -> Union[db.Settings, None]:
    """!
    Searches db for entry with main fields:\n
     - guild
     - setting
     - value

    @param guild_id id of the guild to search for
    @param setting name of the setting to search for e.g. "mod-role"
    @param value value of the setting to search for e.g. role-id
    @param session session to search with, helpful if object shall be edited, since the same session is needed for this
    @return first matching database entry if exists, else None
    """

    sel_statement = select(db.Settings).where(
        and_(
            db.Settings.guild_id == guild_id,
            db.Settings.setting == setting,
            db.Settings.value == value
        )
    )
    entry = session.execute(sel_statement).first()
    return entry[0] if entry else None


def add_setting(guild_id: int, setting: str, value: str,
                channel_id=0, first_param="", active=True, set_by=0,
                last_changed=datetime.datetime.now(),session=db.open_session(),):
    """!
    Add an entry to the settings database

    @param guild_id id the setting is in
    @param setting setting type to add e.g. "mod-role"
    @param value value of the setting e.g. role-id
    @param channel_id id of the channel this setting shall apply to (optional)
    @param first_param optional addition to setting
    @param active boolean if setting shall be active or not
    @param set_by userid of the member who entered that setting - could be neat for logs
    @param last_changed date when entry was last changed
    @param session session to search with, helpful if object shall be edited, since the same session is needed for this
    """
    entry = db.Settings(guild_id=guild_id, channel_id=channel_id, setting=setting, value=value, first_param=first_param,
                        set_by=set_by, active=active, last_changed=last_changed)
    session.add(entry)
    session.commit()


def del_setting_by_main_attributes(guild_id: int, setting: str, value: str, session=db.open_session()):
    """!
    Delete an entry from the settings table by

    @param guild_id id the setting is in
    @param setting setting type to delete
    @param value value of the setting - probably name of a word-list
    @param session session to search with, helpful if object shall be edited, since the same session is needed for this
    """

    statement = delete(db.Settings).where(
        and_(
            db.Settings.guild_id == guild_id,
            db.Settings.setting == setting,
            db.Settings.value == value
        )
    )
    session.execute(statement)
    session.commit()
