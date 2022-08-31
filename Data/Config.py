class Config:
    config_file: dict = None

    def __init__(self):
        main_config: dict = self.get_env_data_as_dict("Config/main.env")
        selected_env: str = main_config["SELECTED_ENVIRONMENT"]
        self.config_file: dict = self.get_env_data_as_dict("Config/" + selected_env + ".env")

    def get_db_name(self) -> str:
        return self.config_file["DATABASE"]

    def get_db_user(self) -> str:
        return self.config_file["USER"]

    def get_db_host(self) -> str:
        return self.config_file["HOST"]

    def get_db_port(self) -> str:
        return self.config_file["PORT"]

    def get_db_password(self) -> str:
        return self.config_file["PASSWORD"]

    def get_redis_host(self) -> str:
        return self.config_file["REDIS_HOST"]

    def get_redis_port(self) -> str:
        return self.config_file["REDIS_PORT"]

    def get_reset_table_on_init(self) -> bool:
        case = self.config_file["RESET_TABLES_ON_INIT"]
        if case != "1":
            return False
        return True

    def get_env_data_as_dict(self, path: str) -> dict:
        with open(path, 'r') as f:
            return dict(tuple(line.replace('\n', '').split('=')) for line in f.readlines() if len(line.strip()) != 0 and not line.startswith('#'))