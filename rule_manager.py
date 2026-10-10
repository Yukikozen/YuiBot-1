import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class RuleManager:

    def __init__(self, parent, rule_store):

        self.rule_store = rule_store
        self.selected_id = None

        self.window = tk.Toplevel(parent)
        self.window.title("YuiBot Rule / Intent Manager")
        self.window.geometry("1100x750")
        self.window.minsize(900, 600)

        self.build()
        self.refresh()

    # =========================================================
    # GUI
    # =========================================================

    def build(self):

        # -----------------------------------------------------
        # SEARCH
        # -----------------------------------------------------

        search_frame = ttk.Frame(
            self.window,
            padding=10
        )

        search_frame.pack(
            fill="x"
        )

        ttk.Label(
            search_frame,
            text="Search rules:"
        ).pack(
            side="left"
        )

        self.search_var = tk.StringVar()

        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var
        )

        search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10
        )

        ttk.Button(
            search_frame,
            text="Search",
            command=self.refresh
        ).pack(
            side="left"
        )

        # -----------------------------------------------------
        # MAIN AREA
        # -----------------------------------------------------

        main = ttk.PanedWindow(
            self.window,
            orient=tk.HORIZONTAL
        )

        main.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        # -----------------------------------------------------
        # LEFT
        # -----------------------------------------------------

        left = ttk.Frame(
            main,
            padding=5
        )

        main.add(
            left,
            weight=1
        )

        ttk.Label(
            left,
            text="Rules",
            font=("Segoe UI", 12, "bold")
        ).pack(
            anchor="w",
            pady=(0, 8)
        )

        self.listbox = tk.Listbox(
            left,
            activestyle="dotbox"
        )

        self.listbox.pack(
            fill="both",
            expand=True
        )

        self.listbox.bind(
            "<<ListboxSelect>>",
            self.select_rule
        )

        # -----------------------------------------------------
        # RIGHT
        # -----------------------------------------------------

        right = ttk.Frame(
            main,
            padding=15
        )

        main.add(
            right,
            weight=3
        )

        ttk.Label(
            right,
            text="Intent name"
        ).pack(
            anchor="w"
        )

        self.intent_var = tk.StringVar()

        ttk.Entry(
            right,
            textvariable=self.intent_var
        ).pack(
            fill="x",
            pady=(3, 12)
        )

        ttk.Label(
            right,
            text="Category"
        ).pack(
            anchor="w"
        )

        self.category_var = tk.StringVar(
            value="General"
        )

        ttk.Entry(
            right,
            textvariable=self.category_var
        ).pack(
            fill="x",
            pady=(3, 12)
        )

        self.enabled_var = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            right,
            text="Rule enabled",
            variable=self.enabled_var
        ).pack(
            anchor="w",
            pady=(0, 12)
        )

        # -----------------------------------------------------
        # TRIGGERS
        # -----------------------------------------------------

        ttk.Label(
            right,
            text="Trigger phrases"
        ).pack(
            anchor="w"
        )

        ttk.Label(
            right,
            text="One trigger per line"
        ).pack(
            anchor="w"
        )

        self.triggers_text = tk.Text(
            right,
            height=7,
            wrap="word"
        )

        self.triggers_text.pack(
            fill="x",
            pady=(3, 12)
        )

        # -----------------------------------------------------
        # RESPONSES
        # -----------------------------------------------------

        ttk.Label(
            right,
            text="Responses"
        ).pack(
            anchor="w"
        )

        ttk.Label(
            right,
            text="One response per line"
        ).pack(
            anchor="w"
        )

        self.responses_text = tk.Text(
            right,
            height=9,
            wrap="word"
        )

        self.responses_text.pack(
            fill="both",
            expand=True,
            pady=(3, 12)
        )

        # -----------------------------------------------------
        # BUTTONS
        # -----------------------------------------------------

        buttons = ttk.Frame(
            self.window,
            padding=10
        )

        buttons.pack(
            fill="x"
        )

        ttk.Button(
            buttons,
            text="New / Clear",
            command=self.clear
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            buttons,
            text="Add Rule",
            command=self.add
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            buttons,
            text="Update Rule",
            command=self.update
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            buttons,
            text="Delete Rule",
            command=self.delete
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            buttons,
            text="Test Rule",
            command=self.test_rule
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            buttons,
            text="Restore Defaults",
            command=self.restore_defaults
        ).pack(
            side="right",
            padx=3
        )

        ttk.Button(
            buttons,
            text="Import JSON",
            command=self.import_rules
        ).pack(
            side="right",
            padx=3
        )

        ttk.Button(
            buttons,
            text="Export JSON",
            command=self.export_rules
        ).pack(
            side="right",
            padx=3
        )

    # =========================================================
    # LIST
    # =========================================================

    def refresh(self):

        self.listbox.delete(
            0,
            tk.END
        )

        keyword = self.search_var.get().strip()

        if keyword:
            rules = self.rule_store.search(
                keyword
            )
        else:
            rules = self.rule_store.get_all()

        for rule in rules:

            status = (
                "ON"
                if rule.get("enabled", True)
                else "OFF"
            )

            display = (
                f"[{status}] "
                f"{rule.get('intent', 'Unnamed')} "
                f"({rule.get('category', 'General')})"
            )

            self.listbox.insert(
                tk.END,
                display
            )

    def get_visible_rules(self):

        keyword = self.search_var.get().strip()

        if keyword:
            return self.rule_store.search(
                keyword
            )

        return self.rule_store.get_all()

    # =========================================================
    # SELECT
    # =========================================================

    def select_rule(self, event=None):

        selection = self.listbox.curselection()

        if not selection:
            return

        rules = self.get_visible_rules()

        index = selection[0]

        if index >= len(rules):
            return

        rule = rules[index]

        self.selected_id = rule["id"]

        self.intent_var.set(
            rule.get("intent", "")
        )

        self.category_var.set(
            rule.get("category", "General")
        )

        self.enabled_var.set(
            rule.get("enabled", True)
        )

        self.triggers_text.delete(
            "1.0",
            tk.END
        )

        self.triggers_text.insert(
            "1.0",
            "\n".join(
                rule.get("triggers", [])
            )
        )

        self.responses_text.delete(
            "1.0",
            tk.END
        )

        self.responses_text.insert(
            "1.0",
            "\n".join(
                rule.get("responses", [])
            )
        )

    # =========================================================
    # DATA
    # =========================================================

    def get_form_data(self):

        intent = self.intent_var.get().strip()

        category = self.category_var.get().strip()

        triggers = [
            line.strip()
            for line in self.triggers_text.get(
                "1.0",
                tk.END
            ).splitlines()
            if line.strip()
        ]

        responses = [
            line.strip()
            for line in self.responses_text.get(
                "1.0",
                tk.END
            ).splitlines()
            if line.strip()
        ]

        if not intent:
            messagebox.showwarning(
                "Rule",
                "Enter an intent name."
            )
            return None

        if not triggers:
            messagebox.showwarning(
                "Rule",
                "Enter at least one trigger."
            )
            return None

        if not responses:
            messagebox.showwarning(
                "Rule",
                "Enter at least one response."
            )
            return None

        if not category:
            category = "General"

        return (
            intent,
            category,
            triggers,
            responses,
            self.enabled_var.get()
        )

    # =========================================================
    # ADD
    # =========================================================

    def add(self):

        data = self.get_form_data()

        if not data:
            return

        intent, category, triggers, responses, enabled = data

        self.rule_store.add(
            intent,
            category,
            triggers,
            responses,
            enabled
        )

        self.clear()
        self.refresh()

        messagebox.showinfo(
            "Rule Manager",
            "Rule added successfully."
        )

    # =========================================================
    # UPDATE
    # =========================================================

    def update(self):

        if not self.selected_id:
            messagebox.showwarning(
                "Rule Manager",
                "Select a rule first."
            )
            return

        data = self.get_form_data()

        if not data:
            return

        intent, category, triggers, responses, enabled = data

        success = self.rule_store.update(
            self.selected_id,
            intent,
            category,
            triggers,
            responses,
            enabled
        )

        if success:
            self.refresh()

            messagebox.showinfo(
                "Rule Manager",
                "Rule updated."
            )

    # =========================================================
    # DELETE
    # =========================================================

    def delete(self):

        if not self.selected_id:
            messagebox.showwarning(
                "Rule Manager",
                "Select a rule first."
            )
            return

        confirm = messagebox.askyesno(
            "Delete Rule",
            "Delete the selected rule?"
        )

        if not confirm:
            return

        self.rule_store.delete(
            self.selected_id
        )

        self.clear()
        self.refresh()

    # =========================================================
    # CLEAR
    # =========================================================

    def clear(self):

        self.selected_id = None

        self.intent_var.set("")

        self.category_var.set(
            "General"
        )

        self.enabled_var.set(True)

        self.triggers_text.delete(
            "1.0",
            tk.END
        )

        self.responses_text.delete(
            "1.0",
            tk.END
        )

        self.listbox.selection_clear(
            0,
            tk.END
        )

    # =========================================================
    # TEST
    # =========================================================

    def test_rule(self):

        triggers = [
            line.strip()
            for line in self.triggers_text.get(
                "1.0",
                tk.END
            ).splitlines()
            if line.strip()
        ]

        responses = [
            line.strip()
            for line in self.responses_text.get(
                "1.0",
                tk.END
            ).splitlines()
            if line.strip()
        ]

        if not triggers:
            messagebox.showwarning(
                "Test Rule",
                "Enter triggers first."
            )
            return

        test_window = tk.Toplevel(
            self.window
        )

        test_window.title(
            "Test Rule"
        )

        test_window.geometry(
            "500x300"
        )

        frame = ttk.Frame(
            test_window,
            padding=20
        )

        frame.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            frame,
            text="Enter a message:"
        ).pack(
            anchor="w"
        )

        input_var = tk.StringVar()

        entry = ttk.Entry(
            frame,
            textvariable=input_var
        )

        entry.pack(
            fill="x",
            pady=10
        )

        result_label = ttk.Label(
            frame,
            text="",
            wraplength=440
        )

        result_label.pack(
            pady=15
        )

        def run_test():

            import difflib

            text = input_var.get().lower().strip()

            if not text:
                return

            best = 0

            for trigger in triggers:

                score = difflib.SequenceMatcher(
                    None,
                    text,
                    trigger.lower()
                ).ratio()

                if trigger.lower() in text:
                    score = 0.93

                best = max(
                    best,
                    score
                )

            if best >= 0.72:
                response = (
                    responses[0]
                    if responses
                    else "No response."
                )

                result_label.config(
                    text=(
                        f"Matched!\n\n"
                        f"Score: {best:.2f}\n\n"
                        f"Example response:\n"
                        f"{response}"
                    )
                )

            else:

                result_label.config(
                    text=f"No match.\nScore: {best:.2f}"
                )

        ttk.Button(
            frame,
            text="Test",
            command=run_test
        ).pack()

        entry.focus_set()

    # =========================================================
    # IMPORT / EXPORT
    # =========================================================

    def import_rules(self):

        path = filedialog.askopenfilename(
            filetypes=[
                ("JSON files", "*.json"),
                ("All files", "*.*")
            ]
        )

        if not path:
            return

        try:

            self.rule_store.import_rules(
                path
            )

            self.clear()
            self.refresh()

            messagebox.showinfo(
                "Import",
                "Rules imported successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Import Error",
                str(e)
            )

    def export_rules(self):

        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[
                ("JSON files", "*.json")
            ]
        )

        if not path:
            return

        try:

            self.rule_store.export_rules(
                path
            )

            messagebox.showinfo(
                "Export",
                "Rules exported successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Export Error",
                str(e)
            )

    # =========================================================
    # RESTORE
    # =========================================================

    def restore_defaults(self):

        confirm = messagebox.askyesno(
            "Restore Defaults",
            "Replace all current rules with the default rules?"
        )

        if not confirm:
            return

        self.rule_store.restore_defaults()

        self.clear()
        self.refresh()

        messagebox.showinfo(
            "Rules",
            "Default rules restored."
        )