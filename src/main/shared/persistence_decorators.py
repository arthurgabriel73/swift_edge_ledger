import contextvars
from functools import wraps
from inspect import isfunction
from typing import Any, Callable, Type, TypeVar


from sqlalchemy.orm import Session

from src.main.shared.database_conn import SessionLocal

db_session_context = contextvars.ContextVar[Session | None]('db_session', default=None)

T = TypeVar('T')


def repository_method(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrap_func(*args: Any, **kwargs: Any) -> Any:
        db_session = db_session_context.get()

        if db_session is None:
            db_session = SessionLocal()

        return func(*args, **kwargs, session=db_session)

    return wrap_func


def repository(cls: Type[T]) -> Type[T]:
    for attr_name in dir(cls):
        attr_value = getattr(cls, attr_name)

        if (
            isfunction(attr_value)
            and not attr_name.startswith('_')
            and not attr_name.startswith('__')
        ):
            decorated_method = repository_method(attr_value)
            setattr(cls, attr_name, decorated_method)

    return cls


def transactional(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrap_func(*args: Any, **kwargs: Any) -> Any:
        db_session = db_session_context.get()

        if db_session is not None:
            return func(*args, **kwargs)

        db_session = SessionLocal()
        db_session_context.set(db_session)

        try:
            result = func(*args, **kwargs)
            db_session.commit()
        except Exception as e:
            print('Error in transaction: ', str(e)[:255])
            db_session.rollback()
            raise e

        finally:
            db_session.close()
            db_session_context.set(None)
        return result

    return wrap_func
