import json
import os


DEFAULT_SETTINGS = {
    "bot_name": "YuiBot",
    "personality": "Friendly",
    "fuzzy_matching": True,
    "memory_enabled": True,
    "context_enabled": True,
    "show_statistics": True
}


class Settings:

    def __init__(self, base_dir=None):

        if base_dir is None:
            base_dir = os.path.dirname(
                os.path.abspath(__file__)
            )

        self.base_dir = base_dir

        self.data_dir = os.path.join(
            self.base_dir,
            "data"
        )

        os.makedirs(
            self.data_dir,
            exist_ok=True
        )

        self.file = os.path.join(
            self.data_dir,
            "settings.json"
        )

        self.data = {}

        self.load()

    # ==========================================================
    # LOAD
    # ==========================================================

    def load(self):

        if not os.path.exists(self.file):

            self.data = dict(
                DEFAULT_SETTINGS
            )

            self.save()

            return

        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as file:

                self.data = json.load(file)

        except Exception:

            self.data = dict(
                DEFAULT_SETTINGS
            )

        changed = False

        for key, value in DEFAULT_SETTINGS.items():

            if key not in self.data:

                self.data[key] = value
                changed = True

        if changed:
            self.save()

    # ==========================================================
    # SAVE
    # ==========================================================

    def save(self):

        try:

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except Exception:

            return False

    # ==========================================================
    # GET
    # ==========================================================

    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )

    # ==========================================================
    # SET
    # ==========================================================

    def set(
        self,
        key,
        value
    ):

        self.data[key] = value

        self.save()

    # ==========================================================
    # RESET
    # ==========================================================

    def reset(self):

        self.data = dict(
            DEFAULT_SETTINGS
        )

        self.save()

    # ==========================================================
    # ALL
    # ==========================================================

    def all(self):

        return dict(
            self.data
        )