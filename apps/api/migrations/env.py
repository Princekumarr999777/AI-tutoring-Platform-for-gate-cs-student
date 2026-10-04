import asyncio
from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from src.core.config import settings
from src.models.base import Base
from src.models.profile import Profile
from src.models.user import User
config = context.config
config.set_main_option("sqlalchemy.url", settings.database_url)
target_metadata = Base.metadata
def run(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction(): context.run_migrations()
async def online():
    engine = async_engine_from_config(config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)
    async with engine.connect() as conn: await conn.run_sync(run)
    await engine.dispose()
if context.is_offline_mode():
    context.configure(url=settings.database_url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction(): context.run_migrations()
else: asyncio.run(online())
