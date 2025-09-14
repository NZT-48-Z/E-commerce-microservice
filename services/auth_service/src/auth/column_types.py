from sqlalchemy import text
from sqlalchemy.orm import mapped_column
from typing import Annotated
import datetime

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('UTC-3', now())"), nullable=False),
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('UTC-3', now())"),
        onupdate=text("TIMEZONE('UTC-3', now())"),
        nullable=False,
    ),
]
