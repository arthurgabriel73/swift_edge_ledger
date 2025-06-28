from src.main.shared.environment_settings import get_env_filename, get_environment_variables


class TestGetEnvironmentVariables:
    def test_get_environment_variables(self):
        get_env_filename.cache_clear()
        env = get_environment_variables()
        assert env.APP_NAME == 'swift_edge_ledger'
        assert env.APP_HOST == '0.0.0.0'
        assert env.APP_PORT == 3000
        assert env.DATABASE_DIALECT == 'postgresql+psycopg'
        assert env.DATABASE_HOST == 'localhost'
        assert env.DATABASE_NAME == 'swift_edge_ledger_db'
        assert env.DATABASE_PASSWORD == 'password'
        assert env.DATABASE_PORT == 5432
        assert env.DATABASE_USER == 'postgres'