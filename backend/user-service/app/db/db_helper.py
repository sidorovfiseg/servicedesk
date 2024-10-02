from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.config import db_config


class DatabaseHelper():
    def __init__(self, url: str, echo: bool = False) -> None:
        
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
        
    async def get_async_session(self) -> AsyncSession: # type: ignore
        async with self.session_factory() as session:
            yield session
            
db_helper = DatabaseHelper(db_config.url, True)