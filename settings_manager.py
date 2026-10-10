import tkinter as tk
from tkinter import messagebox

from settings import DEFAULT_SETTINGS


class SettingsManager:

    def __init__(
        self,
        parent,
        settings,
        on_save=None
    ):

        self.parent = parent
        self.settings = settings
        self.on_save = on_save

        self.window = tk.Toplevel(
            parent
        )

        self.window.title(
            "YuiBot Settings"
        )

        self.window.geometry(
            "650x600"
        )

        self.window.minsize(
            550,
            500
        )

        self.window.configure(
            bg="#171717"
        )

        self.build_ui()

    # ==========================================================
    # UI
    # ==========================================================

    def build_ui(self):

        tk.Label(
            self.window,
            text="YuiBot Settings",
            font=(
                "Segoe UI",
                20,
                "bold"
            ),
            fg="white",
            bg="#171717"
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        tk.Label(
            self.window,
            text="Configure how YuiBot behaves.",
            font=(
                "Segoe UI",
                10
            ),
            fg="#aaaaaa",
            bg="#171717"
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 20)
        )

        # ======================================================
        # GENERAL
        # ======================================================

        section = tk.Frame(
            self.window,
            bg="#202020"
        )

        section.pack(
            fill="x",
            padx=30,
            pady=10
        )

        tk.Label(
            section,
            text="General",
            font=(
                "Segoe UI",
                12,
                "bold"
            ),
            fg="white",
            bg="#202020"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        row = tk.Frame(
            section,
            bg="#202020"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=8
        )

        tk.Label(
            row,
            text="Bot name",
            fg="#cccccc",
            bg="#202020",
            font=(
                "Segoe UI",
                10
            )
        ).pack(
            side="left"
        )

        self.name_entry = tk.Entry(
            row,
            width=25,
            bg="#292929",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.name_entry.pack(
            side="right",
            ipady=5
        )

        self.name_entry.insert(
            0,
            self.settings.get(
                "bot_name",
                "YuiBot"
            )
        )

        # ======================================================
        # PERSONALITY
        # ======================================================

        row = tk.Frame(
            section,
            bg="#202020"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=8
        )

        tk.Label(
            row,
            text="Personality",
            fg="#cccccc",
            bg="#202020"
        ).pack(
            side="left"
        )

        self.personality_var = tk.StringVar(
            value=self.settings.get(
                "personality",
                "Friendly"
            )
        )

        self.personality_menu = tk.OptionMenu(
            row,
            self.personality_var,
            "Friendly",
            "Professional",
            "Short",
            "Casual"
        )

        self.personality_menu.configure(
            bg="#292929",
            fg="white",
            activebackground="#8b3d5c",
            activeforeground="white",
            relief="flat",
            bd=0
        )

        self.personality_menu.pack(
            side="right"
        )

        # ======================================================
        # BEHAVIOR
        # ======================================================

        behavior = tk.Frame(
            self.window,
            bg="#202020"
        )

        behavior.pack(
            fill="x",
            padx=30,
            pady=10
        )

        tk.Label(
            behavior,
            text="Behavior",
            font=(
                "Segoe UI",
                12,
                "bold"
            ),
            fg="white",
            bg="#202020"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        self.fuzzy_var = tk.BooleanVar(
            value=self.settings.get(
                "fuzzy_matching",
                True
            )
        )

        self.memory_var = tk.BooleanVar(
            value=self.settings.get(
                "memory_enabled",
                True
            )
        )

        self.context_var = tk.BooleanVar(
            value=self.settings.get(
                "context_enabled",
                True
            )
        )

        self.stats_var = tk.BooleanVar(
            value=self.settings.get(
                "show_statistics",
                True
            )
        )

        self.add_check(
            behavior,
            "Enable fuzzy matching",
            self.fuzzy_var
        )

        self.add_check(
            behavior,
            "Enable personal memory",
            self.memory_var
        )

        self.add_check(
            behavior,
            "Enable conversation context",
            self.context_var
        )

        self.add_check(
            behavior,
            "Show statistics",
            self.stats_var
        )

        # ======================================================
        # BUTTONS
        # ======================================================

        buttons = tk.Frame(
            self.window,
            bg="#171717"
        )

        buttons.pack(
            fill="x",
            padx=30,
            pady=20
        )

        tk.Button(
            buttons,
            text="Reset Defaults",
            command=self.reset,
            bg="#292929",
            fg="white",
            activebackground="#3a3a3a",
            relief="flat",
            bd=0,
            padx=15,
            pady=9
        ).pack(
            side="left"
        )

        tk.Button(
            buttons,
            text="Save Settings",
            command=self.save,
            bg="#8b3d5c",
            fg="white",
            activebackground="#a64b6d",
            relief="flat",
            bd=0,
            padx=20,
            pady=9
        ).pack(
            side="right"
        )

    # ==========================================================
    # CHECKBOX
    # ==========================================================

    def add_check(
        self,
        parent,
        text,
        variable
    ):

        tk.Checkbutton(
            parent,
            text=text,
            variable=variable,
            font=(
                "Segoe UI",
                10
            ),
            fg="#dddddd",
            bg="#202020",
            activebackground="#202020",
            activeforeground="white",
            selectcolor="#292929"
        ).pack(
            anchor="w",
            padx=20,
            pady=3
        )

    # ==========================================================
    # SAVE
    # ==========================================================

    def save(self):

        name = (
            self.name_entry
            .get()
            .strip()
        )

        if not name:
            name = "YuiBot"

        self.settings.set(
            "bot_name",
            name
        )

        self.settings.set(
            "personality",
            self.personality_var.get()
        )

        self.settings.set(
            "fuzzy_matching",
            self.fuzzy_var.get()
        )

        self.settings.set(
            "memory_enabled",
            self.memory_var.get()
        )

        self.settings.set(
            "context_enabled",
            self.context_var.get()
        )

        self.settings.set(
            "show_statistics",
            self.stats_var.get()
        )

        if self.on_save:
            self.on_save()

        messagebox.showinfo(
            "Settings",
            "Settings saved successfully.",
            parent=self.window
        )

    # ==========================================================
    # RESET
    # ==========================================================

    def reset(self):

        result = messagebox.askyesno(
            "Reset Settings",
            "Reset all settings to their defaults?",
            parent=self.window
        )

        if not result:
            return

        self.settings.reset()

        self.name_entry.delete(
            0,
            "end"
        )

        self.name_entry.insert(
            0,
            DEFAULT_SETTINGS[
                "bot_name"
            ]
        )

        self.personality_var.set(
            DEFAULT_SETTINGS[
                "personality"
            ]
        )

        self.fuzzy_var.set(
            DEFAULT_SETTINGS[
                "fuzzy_matching"
            ]
        )

        self.memory_var.set(
            DEFAULT_SETTINGS[
                "memory_enabled"
            ]
        )

        self.context_var.set(
            DEFAULT_SETTINGS[
                "context_enabled"
            ]
        )

        self.stats_var.set(
            DEFAULT_SETTINGS[
                "show_statistics"
            ]
        )

        if self.on_save:
            self.on_save()