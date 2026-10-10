# # import json
# # import os
# # import tkinter as tk
# # from tkinter import filedialog, messagebox


# # class KnowledgeManager:

# #     def __init__(
# #         self,
# #         parent,
# #         memory,
# #         refresh_callback=None
# #     ):

# #         self.parent = parent
# #         self.memory = memory
# #         self.refresh_callback = (
# #             refresh_callback
# #         )

# #         self.window = tk.Toplevel(
# #             parent
# #         )

# #         self.window.title(
# #             "YuiBot Knowledge Manager"
# #         )

# #         self.window.geometry(
# #             "950x650"
# #         )

# #         self.window.minsize(
# #             750,
# #             500
# #         )

# #         self.window.configure(
# #             bg="#171717"
# #         )

# #         self.selected_question = None

# #         self.build_ui()

# #         self.load_items()

# #     # ==========================================================
# #     # UI
# #     # ==========================================================

# #     def build_ui(self):

# #         # ------------------------------------------------------
# #         # HEADER
# #         # ------------------------------------------------------

# #         header = tk.Frame(
# #             self.window,
# #             bg="#202020",
# #             height=70
# #         )

# #         header.pack(
# #             fill="x"
# #         )

# #         header.pack_propagate(
# #             False
# #         )

# #         title = tk.Label(
# #             header,
# #             text="Knowledge Manager",
# #             font=(
# #                 "Segoe UI",
# #                 18,
# #                 "bold"
# #             ),
# #             fg="#f0f0f0",
# #             bg="#202020"
# #         )

# #         title.pack(
# #             side="left",
# #             padx=20,
# #             pady=18
# #         )

# #         # ------------------------------------------------------
# #         # SEARCH
# #         # ------------------------------------------------------

# #         search_frame = tk.Frame(
# #             self.window,
# #             bg="#171717"
# #         )

# #         search_frame.pack(
# #             fill="x",
# #             padx=20,
# #             pady=15
# #         )

# #         tk.Label(
# #             search_frame,
# #             text="Search:",
# #             font=(
# #                 "Segoe UI",
# #                 10
# #             ),
# #             fg="#dddddd",
# #             bg="#171717"
# #         ).pack(
# #             side="left"
# #         )

# #         self.search_entry = tk.Entry(
# #             search_frame,
# #             font=(
# #                 "Segoe UI",
# #                 10
# #             ),
# #             bg="#292929",
# #             fg="white",
# #             insertbackground="white",
# #             relief="flat"
# #         )

# #         self.search_entry.pack(
# #             side="left",
# #             fill="x",
# #             expand=True,
# #             padx=10,
# #             ipady=7
# #         )

# #         tk.Button(
# #             search_frame,
# #             text="Search",
# #             command=self.search,
# #             bg="#8b3d5c",
# #             fg="white",
# #             activebackground="#a64b6d",
# #             relief="flat",
# #             bd=0,
# #             padx=15,
# #             pady=7
# #         ).pack(
# #             side="left"
# #         )

# #         # ------------------------------------------------------
# #         # LIST
# #         # ------------------------------------------------------

# #         list_frame = tk.Frame(
# #             self.window,
# #             bg="#171717"
# #         )

# #         list_frame.pack(
# #             fill="both",
# #             expand=True,
# #             padx=20
# #         )

# #         self.listbox = tk.Listbox(
# #             list_frame,
# #             font=(
# #                 "Segoe UI",
# #                 10
# #             ),
# #             bg="#222222",
# #             fg="#eeeeee",
# #             selectbackground="#8b3d5c",
# #             selectforeground="white",
# #             relief="flat",
# #             bd=0
# #         )

# #         self.listbox.pack(
# #             side="left",
# #             fill="both",
# #             expand=True
# #         )

# #         scrollbar = tk.Scrollbar(
# #             list_frame,
# #             command=self.listbox.yview
# #         )

# #         scrollbar.pack(
# #             side="right",
# #             fill="y"
# #         )

# #         self.listbox.configure(
# #             yscrollcommand=scrollbar.set
# #         )

# #         self.listbox.bind(
# #             "<<ListboxSelect>>",
# #             self.select_item
# #         )

# #         # ------------------------------------------------------
# #         # EDITOR
# #         # ------------------------------------------------------

# #         editor = tk.Frame(
# #             self.window,
# #             bg="#202020"
# #         )

# #         editor.pack(
# #             fill="x",
# #             padx=20,
# #             pady=15
# #         )

# #         tk.Label(
# #             editor,
# #             text="Question",
# #             font=(
# #                 "Segoe UI",
# #                 9,
# #                 "bold"
# #             ),
# #             fg="#bbbbbb",
# #             bg="#202020"
# #         ).pack(
# #             anchor="w",
# #             padx=15,
# #             pady=(12, 3)
# #         )

# #         self.question_entry = tk.Entry(
# #             editor,
# #             font=(
# #                 "Segoe UI",
# #                 10
# #             ),
# #             bg="#292929",
# #             fg="white",
# #             insertbackground="white",
# #             relief="flat"
# #         )

# #         self.question_entry.pack(
# #             fill="x",
# #             padx=15,
# #             ipady=7
# #         )

# #         tk.Label(
# #             editor,
# #             text="Answer",
# #             font=(
# #                 "Segoe UI",
# #                 9,
# #                 "bold"
# #             ),
# #             fg="#bbbbbb",
# #             bg="#202020"
# #         ).pack(
# #             anchor="w",
# #             padx=15,
# #             pady=(10, 3)
# #         )

# #         self.answer_text = tk.Text(
# #             editor,
# #             height=5,
# #             font=(
# #                 "Segoe UI",
# #                 10
# #             ),
# #             bg="#292929",
# #             fg="white",
# #             insertbackground="white",
# #             relief="flat"
# #         )

# #         self.answer_text.pack(
# #             fill="x",
# #             padx=15
# #         )

# #         # ------------------------------------------------------
# #         # CATEGORY
# #         # ------------------------------------------------------

# #         category_frame = tk.Frame(
# #             editor,
# #             bg="#202020"
# #         )

# #         category_frame.pack(
# #             fill="x",
# #             padx=15,
# #             pady=10
# #         )

# #         tk.Label(
# #             category_frame,
# #             text="Category:",
# #             fg="#bbbbbb",
# #             bg="#202020"
# #         ).pack(
# #             side="left"
# #         )

# #         self.category_entry = tk.Entry(
# #             category_frame,
# #             width=25,
# #             bg="#292929",
# #             fg="white",
# #             insertbackground="white",
# #             relief="flat"
# #         )

# #         self.category_entry.pack(
# #             side="left",
# #             padx=10,
# #             ipady=5
# #         )

# #         # ------------------------------------------------------
# #         # BUTTONS
# #         # ------------------------------------------------------

# #         buttons = tk.Frame(
# #             editor,
# #             bg="#202020"
# #         )

# #         buttons.pack(
# #             fill="x",
# #             padx=15,
# #             pady=(0, 15)
# #         )

# #         self.make_button(
# #             buttons,
# #             "Add",
# #             self.add_item
# #         )

# #         self.make_button(
# #             buttons,
# #             "Update",
# #             self.update_item
# #         )

# #         self.make_button(
# #             buttons,
# #             "Delete",
# #             self.delete_item
# #         )

# #         self.make_button(
# #             buttons,
# #             "Clear",
# #             self.clear_editor
# #         )

# #         self.make_button(
# #             buttons,
# #             "Import",
# #             self.import_data
# #         )

# #         self.make_button(
# #             buttons,
# #             "Export",
# #             self.export_data
# #         )

# #     # ==========================================================
# #     # BUTTON
# #     # ==========================================================

# #     def make_button(
# #         self,
# #         parent,
# #         text,
# #         command
# #     ):

# #         tk.Button(
# #             parent,
# #             text=text,
# #             command=command,
# #             font=(
# #                 "Segoe UI",
# #                 9
# #             ),
# #             bg="#292929",
# #             fg="#eeeeee",
# #             activebackground="#8b3d5c",
# #             activeforeground="white",
# #             relief="flat",
# #             bd=0,
# #             padx=15,
# #             pady=7
# #         ).pack(
# #             side="left",
# #             padx=(0, 8)
# #         )

# #     # ==========================================================
# #     # LOAD
# #     # ==========================================================

# #     def load_items(
# #         self,
# #         filter_text=""
# #     ):

# #         self.listbox.delete(
# #             0,
# #             "end"
# #         )

# #         knowledge = (
# #             self.memory.get_knowledge()
# #         )

# #         filter_text = (
# #             filter_text.lower()
# #         )

# #         for question, item in sorted(
# #             knowledge.items()
# #         ):

# #             answer = item.get(
# #                 "answer",
# #                 ""
# #             )

# #             category = item.get(
# #                 "category",
# #                 "General"
# #             )

# #             combined = (
# #                 question
# #                 + " "
# #                 + answer
# #                 + " "
# #                 + category
# #             )

# #             if (
# #                 filter_text
# #                 and filter_text not in combined.lower()
# #             ):
# #                 continue

# #             display = (
# #                 f"[{category}] "
# #                 f"{question}"
# #             )

# #             self.listbox.insert(
# #                 "end",
# #                 display
# #             )

# #     # ==========================================================
# #     # SELECT
# #     # ==========================================================

# #     def select_item(
# #         self,
# #         event=None
# #     ):

# #         selection = (
# #             self.listbox.curselection()
# #         )

# #         if not selection:
# #             return

# #         display = self.listbox.get(
# #             selection[0]
# #         )

# #         question = display

# #         if "] " in question:

# #             question = question.split(
# #                 "] ",
# #                 1
# #             )[1]

# #         knowledge = (
# #             self.memory.get_knowledge()
# #         )

# #         if question not in knowledge:
# #             return

# #         item = knowledge[
# #             question
# #         ]

# #         self.selected_question = (
# #             question
# #         )

# #         self.question_entry.delete(
# #             0,
# #             "end"
# #         )

# #         self.question_entry.insert(
# #             0,
# #             question
# #         )

# #         self.answer_text.delete(
# #             "1.0",
# #             "end"
# #         )

# #         self.answer_text.insert(
# #             "1.0",
# #             item.get(
# #                 "answer",
# #                 ""
# #             )
# #         )

# #         self.category_entry.delete(
# #             0,
# #             "end"
# #         )

# #         self.category_entry.insert(
# #             0,
# #             item.get(
# #                 "category",
# #                 "General"
# #             )
# #         )

# #     # ==========================================================
# #     # ADD
# #     # ==========================================================

# #     def add_item(self):

# #         question = (
# #             self.question_entry
# #             .get()
# #             .strip()
# #         )

# #         answer = (
# #             self.answer_text
# #             .get(
# #                 "1.0",
# #                 "end"
# #             )
# #             .strip()
# #         )

# #         category = (
# #             self.category_entry
# #             .get()
# #             .strip()
# #             or "General"
# #         )

# #         if not question or not answer:

# #             messagebox.showwarning(
# #                 "Missing information",
# #                 "Please enter both a question and an answer.",
# #                 parent=self.window
# #             )

# #             return

# #         self.memory.set_knowledge(
# #             question.lower(),
# #             answer,
# #             category
# #         )

# #         self.load_items()

# #         self.clear_editor()

# #         messagebox.showinfo(
# #             "Knowledge",
# #             "Knowledge added successfully.",
# #             parent=self.window
# #         )

# #     # ==========================================================
# #     # UPDATE
# #     # ==========================================================

# #     def update_item(self):

# #         if not self.selected_question:

# #             messagebox.showwarning(
# #                 "Nothing selected",
# #                 "Select a knowledge item first.",
# #                 parent=self.window
# #             )

# #             return

# #         question = (
# #             self.question_entry
# #             .get()
# #             .strip()
# #         )

# #         answer = (
# #             self.answer_text
# #             .get(
# #                 "1.0",
# #                 "end"
# #             )
# #             .strip()
# #         )

# #         category = (
# #             self.category_entry
# #             .get()
# #             .strip()
# #             or "General"
# #         )

# #         if not question or not answer:
# #             return

# #         if (
# #             self.selected_question
# #             != question
# #         ):

# #             self.memory.delete_knowledge(
# #                 self.selected_question
# #             )

# #         self.memory.set_knowledge(
# #             question.lower(),
# #             answer,
# #             category
# #         )

# #         self.load_items()

# #         self.clear_editor()

# #         messagebox.showinfo(
# #             "Knowledge",
# #             "Knowledge updated successfully.",
# #             parent=self.window
# #         )

# #     # ==========================================================
# #     # DELETE
# #     # ==========================================================

# #     def delete_item(self):

# #         if not self.selected_question:

# #             messagebox.showwarning(
# #                 "Nothing selected",
# #                 "Select a knowledge item first.",
# #                 parent=self.window
# #             )

# #             return

# #         result = messagebox.askyesno(
# #             "Delete Knowledge",
# #             "Delete this knowledge item?",
# #             parent=self.window
# #         )

# #         if not result:
# #             return

# #         self.memory.delete_knowledge(
# #             self.selected_question
# #         )

# #         self.load_items()

# #         self.clear_editor()

# #     # ==========================================================
# #     # CLEAR EDITOR
# #     # ==========================================================

# #     def clear_editor(self):

# #         self.selected_question = None

# #         self.question_entry.delete(
# #             0,
# #             "end"
# #         )

# #         self.answer_text.delete(
# #             "1.0",
# #             "end"
# #         )

# #         self.category_entry.delete(
# #             0,
# #             "end"
# #         )

# #         self.listbox.selection_clear(
# #             0,
# #             "end"
# #         )

# #     # ==========================================================
# #     # SEARCH
# #     # ==========================================================

# #     def search(self):

# #         query = (
# #             self.search_entry
# #             .get()
# #             .strip()
# #         )

# #         self.load_items(
# #             query
# #         )

# #     # ==========================================================
# #     # EXPORT
# #     # ==========================================================

# #     def export_data(self):

# #         filename = filedialog.asksaveasfilename(
# #             parent=self.window,
# #             title="Export Knowledge",
# #             defaultextension=".json",
# #             filetypes=[
# #                 (
# #                     "JSON files",
# #                     "*.json"
# #                 )
# #             ]
# #         )

# #         if not filename:
# #             return

# #         success = (
# #             self.memory.export_knowledge(
# #                 filename
# #             )
# #         )

# #         if success:

# #             messagebox.showinfo(
# #                 "Export",
# #                 "Knowledge exported successfully.",
# #                 parent=self.window
# #             )

# #         else:

# #             messagebox.showerror(
# #                 "Export",
# #                 "Failed to export knowledge.",
# #                 parent=self.window
# #             )

# #     # ==========================================================
# #     # IMPORT
# #     # ==========================================================

# #     def import_data(self):

# #         filename = filedialog.askopenfilename(
# #             parent=self.window,
# #             title="Import Knowledge",
# #             filetypes=[
# #                 (
# #                     "JSON files",
# #                     "*.json"
# #                 )
# #             ]
# #         )

# #         if not filename:
# #             return

# #         success = (
# #             self.memory.import_knowledge(
# #                 filename
# #             )
# #         )

# #         if success:

# #             self.load_items()

# #             messagebox.showinfo(
# #                 "Import",
# #                 "Knowledge imported successfully.",
# #                 parent=self.window
# #             )

# #         else:

# #             messagebox.showerror(
# #                 "Import",
# #                 "The selected JSON file is invalid.",
# #                 parent=self.window
# #             )


# import tkinter as tk
# from tkinter import filedialog, messagebox


# class KnowledgeManager:

#     def __init__(
#         self,
#         parent,
#         memory
#     ):

#         self.memory = memory

#         self.window = tk.Toplevel(
#             parent
#         )

#         self.window.title(
#             "YuiBot Knowledge Manager"
#         )

#         self.window.geometry(
#             "950x650"
#         )

#         self.window.configure(
#             bg="#171717"
#         )

#         self.selected_question = None

#         self.build_ui()
#         self.load_items()

#     # ==========================================================
#     # UI
#     # ==========================================================

#     def build_ui(self):

#         tk.Label(
#             self.window,
#             text="Knowledge Manager",
#             font=(
#                 "Segoe UI",
#                 20,
#                 "bold"
#             ),
#             fg="white",
#             bg="#171717"
#         ).pack(
#             anchor="w",
#             padx=20,
#             pady=20
#         )

#         search_frame = tk.Frame(
#             self.window,
#             bg="#171717"
#         )

#         search_frame.pack(
#             fill="x",
#             padx=20
#         )

#         self.search_entry = tk.Entry(
#             search_frame,
#             bg="#292929",
#             fg="white",
#             insertbackground="white",
#             relief="flat"
#         )

#         self.search_entry.pack(
#             side="left",
#             fill="x",
#             expand=True,
#             ipady=7
#         )

#         tk.Button(
#             search_frame,
#             text="Search",
#             command=self.search,
#             bg="#8b3d5c",
#             fg="white",
#             relief="flat",
#             bd=0,
#             padx=15,
#             pady=7
#         ).pack(
#             side="left",
#             padx=10
#         )

#         # ------------------------------------------------------
#         # LIST
#         # ------------------------------------------------------

#         list_frame = tk.Frame(
#             self.window,
#             bg="#171717"
#         )

#         list_frame.pack(
#             fill="both",
#             expand=True,
#             padx=20,
#             pady=15
#         )

#         self.listbox = tk.Listbox(
#             list_frame,
#             bg="#202020",
#             fg="#eeeeee",
#             selectbackground="#8b3d5c",
#             relief="flat",
#             bd=0
#         )

#         self.listbox.pack(
#             side="left",
#             fill="both",
#             expand=True
#         )

#         scrollbar = tk.Scrollbar(
#             list_frame,
#             command=self.listbox.yview
#         )

#         scrollbar.pack(
#             side="right",
#             fill="y"
#         )

#         self.listbox.configure(
#             yscrollcommand=scrollbar.set
#         )

#         self.listbox.bind(
#             "<<ListboxSelect>>",
#             self.select_item
#         )

#         # ------------------------------------------------------
#         # EDITOR
#         # ------------------------------------------------------

#         editor = tk.Frame(
#             self.window,
#             bg="#202020"
#         )

#         editor.pack(
#             fill="x",
#             padx=20,
#             pady=10
#         )

#         tk.Label(
#             editor,
#             text="Question",
#             fg="#bbbbbb",
#             bg="#202020"
#         ).pack(
#             anchor="w",
#             padx=15,
#             pady=(10, 3)
#         )

#         self.question = tk.Entry(
#             editor,
#             bg="#292929",
#             fg="white",
#             insertbackground="white",
#             relief="flat"
#         )

#         self.question.pack(
#             fill="x",
#             padx=15,
#             ipady=6
#         )

#         tk.Label(
#             editor,
#             text="Answer",
#             fg="#bbbbbb",
#             bg="#202020"
#         ).pack(
#             anchor="w",
#             padx=15,
#             pady=(10, 3)
#         )

#         self.answer = tk.Text(
#             editor,
#             height=4,
#             bg="#292929",
#             fg="white",
#             insertbackground="white",
#             relief="flat"
#         )

#         self.answer.pack(
#             fill="x",
#             padx=15
#         )

#         tk.Label(
#             editor,
#             text="Category",
#             fg="#bbbbbb",
#             bg="#202020"
#         ).pack(
#             anchor="w",
#             padx=15,
#             pady=(10, 3)
#         )

#         self.category = tk.Entry(
#             editor,
#             bg="#292929",
#             fg="white",
#             insertbackground="white",
#             relief="flat"
#         )

#         self.category.pack(
#             fill="x",
#             padx=15,
#             ipady=6
#         )

#         buttons = tk.Frame(
#             editor,
#             bg="#202020"
#         )

#         buttons.pack(
#             fill="x",
#             padx=15,
#             pady=15
#         )

#         self.button(
#             buttons,
#             "Add",
#             self.add
#         )

#         self.button(
#             buttons,
#             "Update",
#             self.update
#         )

#         self.button(
#             buttons,
#             "Delete",
#             self.delete
#         )

#         self.button(
#             buttons,
#             "Clear",
#             self.clear
#         )

#         self.button(
#             buttons,
#             "Import",
#             self.import_data
#         )

#         self.button(
#             buttons,
#             "Export",
#             self.export_data
#         )

#     # ==========================================================
#     # BUTTON
#     # ==========================================================

#     def button(
#         self,
#         parent,
#         text,
#         command
#     ):

#         tk.Button(
#             parent,
#             text=text,
#             command=command,
#             bg="#292929",
#             fg="white",
#             activebackground="#8b3d5c",
#             relief="flat",
#             bd=0,
#             padx=15,
#             pady=7
#         ).pack(
#             side="left",
#             padx=4
#         )

#     # ==========================================================
#     # LOAD
#     # ==========================================================

#     def load_items(
#         self,
#         search=""
#     ):

#         self.listbox.delete(
#             0,
#             "end"
#         )

#         search = search.lower()

#         for question, item in sorted(
#             self.memory.get_knowledge().items()
#         ):

#             answer = item.get(
#                 "answer",
#                 ""
#             )

#             category = item.get(
#                 "category",
#                 "General"
#             )

#             combined = (
#                 question
#                 + " "
#                 + answer
#                 + " "
#                 + category
#             )

#             if search and search not in combined.lower():
#                 continue

#             self.listbox.insert(
#                 "end",
#                 f"[{category}] {question}"
#             )

#     # ==========================================================
#     # SELECT
#     # ==========================================================

#     def select_item(
#         self,
#         event=None
#     ):

#         selection = (
#             self.listbox.curselection()
#         )

#         if not selection:
#             return

#         display = self.listbox.get(
#             selection[0]
#         )

#         if "] " in display:

#             question = display.split(
#                 "] ",
#                 1
#             )[1]

#         else:

#             question = display

#         knowledge = (
#             self.memory.get_knowledge()
#         )

#         if question not in knowledge:
#             return

#         item = knowledge[
#             question
#         ]

#         self.selected_question = (
#             question
#         )

#         self.question.delete(
#             0,
#             "end"
#         )

#         self.question.insert(
#             0,
#             question
#         )

#         self.answer.delete(
#             "1.0",
#             "end"
#         )

#         self.answer.insert(
#             "1.0",
#             item.get(
#                 "answer",
#                 ""
#             )
#         )

#         self.category.delete(
#             0,
#             "end"
#         )

#         self.category.insert(
#             0,
#             item.get(
#                 "category",
#                 "General"
#             )
#         )

#     # ==========================================================
#     # ADD
#     # ==========================================================

#     def add(self):

#         question = self.question.get().strip()
#         answer = self.answer.get(
#             "1.0",
#             "end"
#         ).strip()

#         category = (
#             self.category.get().strip()
#             or "General"
#         )

#         if not question or not answer:

#             messagebox.showwarning(
#                 "Knowledge",
#                 "Enter a question and answer.",
#                 parent=self.window
#             )

#             return

#         self.memory.set_knowledge(
#             question.lower(),
#             answer,
#             category
#         )

#         self.load_items()
#         self.clear()

#     # ==========================================================
#     # UPDATE
#     # ==========================================================

#     def update(self):

#         if not self.selected_question:

#             messagebox.showwarning(
#                 "Knowledge",
#                 "Select an item first.",
#                 parent=self.window
#             )

#             return

#         question = self.question.get().strip()
#         answer = self.answer.get(
#             "1.0",
#             "end"
#         ).strip()

#         category = (
#             self.category.get().strip()
#             or "General"
#         )

#         if self.selected_question != question:

#             self.memory.delete_knowledge(
#                 self.selected_question
#             )

#         self.memory.set_knowledge(
#             question.lower(),
#             answer,
#             category
#         )

#         self.load_items()
#         self.clear()

#     # ==========================================================
#     # DELETE
#     # ==========================================================

#     def delete(self):

#         if not self.selected_question:
#             return

#         result = messagebox.askyesno(
#             "Delete",
#             "Delete this knowledge entry?",
#             parent=self.window
#         )

#         if not result:
#             return

#         self.memory.delete_knowledge(
#             self.selected_question
#         )

#         self.load_items()
#         self.clear()

#     # ==========================================================
#     # CLEAR
#     # ==========================================================

#     def clear(self):

#         self.selected_question = None

#         self.question.delete(
#             0,
#             "end"
#         )

#         self.answer.delete(
#             "1.0",
#             "end"
#         )

#         self.category.delete(
#             0,
#             "end"
#         )

#         self.listbox.selection_clear(
#             0,
#             "end"
#         )

#     # ==========================================================
#     # SEARCH
#     # ==========================================================

#     def search(self):

#         self.load_items(
#             self.search_entry.get().strip()
#         )

#     # ==========================================================
#     # EXPORT
#     # ==========================================================

#     def export_data(self):

#         filename = filedialog.asksaveasfilename(
#             parent=self.window,
#             defaultextension=".json",
#             filetypes=[
#                 (
#                     "JSON files",
#                     "*.json"
#                 )
#             ]
#         )

#         if not filename:
#             return

#         if self.memory.export_knowledge(
#             filename
#         ):

#             messagebox.showinfo(
#                 "Export",
#                 "Knowledge exported successfully.",
#                 parent=self.window
#             )

#     # ==========================================================
#     # IMPORT
#     # ==========================================================

#     def import_data(self):

#         filename = filedialog.askopenfilename(
#             parent=self.window,
#             filetypes=[
#                 (
#                     "JSON files",
#                     "*.json"
#                 )
#             ]
#         )

#         if not filename:
#             return

#         if self.memory.import_knowledge(
#             filename
#         ):

#             self.load_items()

#             messagebox.showinfo(
#                 "Import",
#                 "Knowledge imported successfully.",
#                 parent=self.window
#             )

#         else:

#             messagebox.showerror(
#                 "Import",
#                 "Invalid knowledge file.",
#                 parent=self.window
#             )




"""Tkinter Knowledge Garden: create, edit, delete, search, import and export."""
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

BG = "#FFF6FA"
WHITE = "#FFFFFF"
TEXT = "#59465F"
MUTED = "#A18DA8"
PINK = "#FFB7D5"
PURPLE = "#9274C8"
BORDER = "#F0D9EC"


class KnowledgeManager:
    def __init__(self, parent, knowledge_store):
        self.parent = parent
        self.store = knowledge_store
        self.selected_id = None
        self.window = tk.Toplevel(parent)
        self.window.title("♡ Knowledge Garden — Teach YuiBot")
        self.window.geometry("940x650")
        self.window.minsize(760, 520)
        self.window.configure(bg=BG)
        self._build()
        self.refresh()
        self.window.transient(parent)

    def _build(self):
        header = tk.Frame(self.window, bg=BG, padx=18, pady=14)
        header.pack(fill="x")
        tk.Label(header, text="Knowledge Garden ♡", bg=BG, fg=TEXT,
                 font=("Segoe UI", 18, "bold")).pack(anchor="w")
        tk.Label(header, text="Teach YuiBot facts it can save and recall offline.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 0))

        toolbar = tk.Frame(self.window, bg=BG, padx=18)
        toolbar.pack(fill="x", pady=(0, 10))
        tk.Button(toolbar, text="＋ New", command=self.new_entry, bg=PINK, fg=TEXT,
                  relief="flat", padx=12, pady=7).pack(side="left", padx=(0, 6))
        tk.Button(toolbar, text="Import .txt / .json", command=self.import_file, bg=WHITE,
                  fg=TEXT, relief="flat", padx=12, pady=7).pack(side="left", padx=6)
        tk.Button(toolbar, text="Export JSON", command=self.export_file, bg=WHITE,
                  fg=TEXT, relief="flat", padx=12, pady=7).pack(side="left", padx=6)
        self.search_var = tk.StringVar()
        search = tk.Entry(toolbar, textvariable=self.search_var, bg=WHITE, fg=TEXT,
                          relief="flat", font=("Segoe UI", 10), width=25)
        search.pack(side="right", ipady=7)
        search.bind("<KeyRelease>", lambda _e: self.refresh())
        tk.Label(toolbar, text="Search", bg=BG, fg=MUTED).pack(side="right", padx=8)

        body = tk.Frame(self.window, bg=BG, padx=18, pady=6)
        body.pack(fill="both", expand=True)
        body.grid_columnconfigure(0, weight=3)
        body.grid_columnconfigure(1, weight=4)
        body.grid_rowconfigure(0, weight=1)

        left = tk.Frame(body, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        left.grid_rowconfigure(0, weight=1)
        left.grid_columnconfigure(0, weight=1)
        self.tree = ttk.Treeview(left, columns=("category",), show="tree headings", selectmode="browse")
        self.tree.heading("#0", text="Question")
        self.tree.heading("category", text="Category")
        self.tree.column("#0", width=230, minwidth=150)
        self.tree.column("category", width=100, minwidth=70)
        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(left, orient="vertical", command=self.tree.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.bind("<<TreeviewSelect>>", self.select_entry)

        right = tk.Frame(body, bg=WHITE, padx=14, pady=14,
                         highlightbackground=BORDER, highlightthickness=1)
        right.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        right.grid_columnconfigure(0, weight=1)
        tk.Label(right, text="Question", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w")
        self.question_var = tk.StringVar()
        tk.Entry(right, textvariable=self.question_var, bg="#FFFBFD", fg=TEXT,
                 relief="solid", bd=1, font=("Segoe UI", 10)).grid(row=1, column=0, sticky="ew", pady=(5, 12), ipady=7)
        tk.Label(right, text="Answer", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).grid(row=2, column=0, sticky="w")
        self.answer_text = tk.Text(right, height=11, wrap="word", bg="#FFFBFD", fg=TEXT,
                                   relief="solid", bd=1, font=("Segoe UI", 10), undo=True)
        self.answer_text.grid(row=3, column=0, sticky="nsew", pady=(5, 12))
        right.grid_rowconfigure(3, weight=1)
        tk.Label(right, text="Category", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).grid(row=4, column=0, sticky="w")
        self.category_var = tk.StringVar(value="General")
        tk.Entry(right, textvariable=self.category_var, bg="#FFFBFD", fg=TEXT,
                 relief="solid", bd=1, font=("Segoe UI", 10)).grid(row=5, column=0, sticky="ew", pady=(5, 12), ipady=6)
        buttons = tk.Frame(right, bg=WHITE)
        buttons.grid(row=6, column=0, sticky="ew")
        tk.Button(buttons, text="Save Entry", command=self.save_entry, bg=PINK, fg=TEXT,
                  relief="flat", padx=14, pady=8).pack(side="left")
        tk.Button(buttons, text="Delete", command=self.delete_entry, bg="#FFE7EC", fg=TEXT,
                  relief="flat", padx=14, pady=8).pack(side="left", padx=8)
        tk.Button(buttons, text="Clear", command=self.new_entry, bg=WHITE, fg=TEXT,
                  relief="flat", padx=14, pady=8).pack(side="left")
        self.status = tk.Label(self.window, text="", bg=BG, fg=MUTED,
                               font=("Segoe UI", 9), anchor="w", padx=20, pady=8)
        self.status.pack(fill="x")

    def refresh(self):
        if not hasattr(self, "tree"):
            return
        current = self.selected_id
        for item in self.tree.get_children(""):
            self.tree.delete(item)
        entries = self.store.search(self.search_var.get())
        for entry in entries:
            self.tree.insert("", "end", iid=entry["id"], text=entry["question"],
                             values=(entry.get("category", "General"),))
        if current and self.tree.exists(current):
            self.tree.selection_set(current)
        self.status.configure(text=f"{len(entries)} matching entr{'y' if len(entries) == 1 else 'ies'} · Saved locally")

    def select_entry(self, _event=None):
        selection = self.tree.selection()
        if not selection:
            return
        entry_id = selection[0]
        entry = self.store.get(entry_id)
        if not entry:
            return
        self.selected_id = entry_id
        self.question_var.set(entry["question"])
        self.answer_text.delete("1.0", "end")
        self.answer_text.insert("1.0", entry["answer"])
        self.category_var.set(entry.get("category", "General"))

    def new_entry(self):
        self.selected_id = None
        self.tree.selection_remove(self.tree.selection())
        self.question_var.set("")
        self.answer_text.delete("1.0", "end")
        self.category_var.set("General")

    def save_entry(self):
        question = self.question_var.get().strip()
        answer = self.answer_text.get("1.0", "end").strip()
        category = self.category_var.get().strip() or "General"
        if not question or not answer:
            messagebox.showwarning("Missing information", "Please enter both a question and an answer.", parent=self.window)
            return
        try:
            if self.selected_id and self.store.get(self.selected_id):
                self.store.update(self.selected_id, question, answer, category, "Knowledge Garden")
                saved = self.store.get(self.selected_id)
            else:
                saved = self.store.add(question, answer, category, "Knowledge Garden")
                self.selected_id = saved["id"]
            self.refresh()
            if self.tree.exists(self.selected_id):
                self.tree.selection_set(self.selected_id)
            self.status.configure(text="Saved! YuiBot can now use this knowledge.")
        except Exception as exc:
            messagebox.showerror("Could not save", str(exc), parent=self.window)

    def delete_entry(self):
        if not self.selected_id:
            messagebox.showinfo("Choose an entry", "Select a knowledge entry to delete.", parent=self.window)
            return
        entry = self.store.get(self.selected_id)
        if not entry:
            return
        if not messagebox.askyesno("Delete knowledge?", f"Delete this entry?\n\n{entry['question']}", parent=self.window):
            return
        self.store.delete(self.selected_id)
        self.new_entry()
        self.refresh()

    def import_file(self):
        path = filedialog.askopenfilename(parent=self.window, title="Import knowledge",
            filetypes=[("Knowledge files", "*.txt *.json"), ("Text files", "*.txt"), ("JSON files", "*.json")])
        if not path:
            return
        try:
            result = self.store.import_file(path)
            self.refresh()
            messagebox.showinfo("Import complete",
                f"Read {result['imported']} entries.\nNew entries: {result['new']}\nTotal saved: {result['total']}.", parent=self.window)
        except Exception as exc:
            messagebox.showerror("Import failed", str(exc), parent=self.window)

    def export_file(self):
        path = filedialog.asksaveasfilename(parent=self.window, title="Export knowledge",
            defaultextension=".json", initialfile="yui_knowledge_export.json",
            filetypes=[("JSON files", "*.json")])
        if not path:
            return
        try:
            self.store.export_file(path)
            messagebox.showinfo("Export complete", f"Knowledge exported to:\n{path}", parent=self.window)
        except Exception as exc:
            messagebox.showerror("Export failed", str(exc), parent=self.window)
