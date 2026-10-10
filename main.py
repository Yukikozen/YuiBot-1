

# import tkinter as tk

# from tkinter import ttk, messagebox

# import random

# from chatbot import YuiBot

# from settings_manager import SettingsManager

# from knowledge_manager import KnowledgeManager

# from rule_manager import RuleManager

# # ============================================================

# # YUIBOT KAWAII THEME

# # ============================================================

# BG = "#FFF6FA"

# SIDEBAR = "#F6E8FF"

# PINK = "#FFB7D5"

# PINK_DARK = "#E887B3"

# LAVENDER = "#DCCBFF"

# PURPLE = "#9274C8"

# CREAM = "#FFFDF8"

# WHITE = "#FFFFFF"

# TEXT = "#59465F"

# MUTED = "#A18DA8"

# GREEN = "#A7DDBB"

# BORDER = "#F0D9EC"

# class YuiBotApp:

#     def __init__(self, root):

#         self.root = root

#         self.bot = YuiBot()

#         self.root.title("YuiBot ♡ My Little Chat Companion")

#         self.root.geometry("1180x780")

#         self.root.minsize(900, 650)

#         self.root.configure(bg=BG)

#         self.chat_messages = []

#         self.busy = False

#         self.setup_style()

#         self.build_ui()

#         self.load_history()

#         self.refresh_header()

#         self.root.protocol("WM_DELETE_WINDOW", self.close)

#         self.root.bind("<Control-Return>", self.send_event)

#         self.root.bind("<Control-l>", self.clear_conversation_event)

#     # ========================================================

#     # STYLE

#     # ========================================================

#     def setup_style(self):

#         style = ttk.Style()

#         try:

#             style.theme_use("clam")

#         except tk.TclError:

#             pass

#         style.configure(

#             "Cute.TButton",

#             font=("Segoe UI", 10),

#             background=WHITE,

#             foreground=TEXT,

#             padding=(10, 9),

#             borderwidth=0

#         )

#         style.map(

#             "Cute.TButton",

#             background=[

#                 ("active", "#FFE0EE"),

#                 ("pressed", PINK)

#             ]

#         )

#         style.configure(

#             "Pink.TButton",

#             font=("Segoe UI", 11, "bold"),

#             background=PINK,

#             foreground="#6D3D5B",

#             padding=(18, 12),

#             borderwidth=0

#         )

#         style.map(

#             "Pink.TButton",

#             background=[

#                 ("active", "#FF9FC8"),

#                 ("pressed", PINK_DARK)

#             ]

#         )

#         style.configure(

#             "Cute.TEntry",

#             padding=10,

#             fieldbackground=WHITE,

#             foreground=TEXT

#         )

#     # ========================================================

#     # HELPERS

#     # ========================================================

#     def rounded_rect(

#         self, canvas, x1, y1, x2, y2,

#         radius=18, fill=WHITE, outline=""

#     ):

#         radius = min(

#             radius,

#             (x2 - x1) / 2,

#             (y2 - y1) / 2

#         )

#         points = [

#             x1 + radius, y1,

#             x2 - radius, y1,

#             x2, y1,

#             x2, y1 + radius,

#             x2, y2 - radius,

#             x2, y2,

#             x2 - radius, y2,

#             x1 + radius, y2,

#             x1, y2,

#             x1, y2 - radius,

#             x1, y1 + radius,

#             x1, y1

#         ]

#         return canvas.create_polygon(

#             points,

#             smooth=True,

#             fill=fill,

#             outline=outline

#         )

#     def make_card(self, parent, color=WHITE, padding=12):

#         frame = tk.Frame(

#             parent,

#             bg=color,

#             padx=padding,

#             pady=padding,

#             highlightbackground=BORDER,

#             highlightthickness=1

#         )

#         return frame

#     # ========================================================

#     # MAIN WINDOW

#     # ========================================================

#     def build_ui(self):

#         self.root.grid_rowconfigure(0, weight=1)

#         self.root.grid_columnconfigure(1, weight=1)

#         # ---------------- SIDEBAR ----------------

#         self.sidebar = tk.Frame(

#             self.root,

#             bg=SIDEBAR,

#             width=238

#         )

#         self.sidebar.grid(

#             row=0, column=0,

#             sticky="ns"

#         )

#         self.sidebar.grid_propagate(False)

#         # Mascot / logo panel

#         logo = tk.Frame(

#             self.sidebar,

#             bg=SIDEBAR

#         )

#         logo.pack(fill="x", padx=18, pady=(22, 20))

#         mascot = tk.Canvas(

#             logo,

#             width=88,

#             height=88,

#             bg=SIDEBAR,

#             highlightthickness=0

#         )

#         mascot.pack()

#         # Cute character face

#         mascot.create_oval(

#             12, 12, 76, 76,

#             fill="#FFE1EE",

#             outline="#F6B9D4",

#             width=2

#         )

#         mascot.create_oval(

#             29, 37, 35, 45,

#             fill=TEXT,

#             outline=""

#         )

#         mascot.create_oval(

#             53, 37, 59, 45,

#             fill=TEXT,

#             outline=""

#         )

#         mascot.create_arc(

#             34, 39, 54, 58,

#             start=205, extent=130,

#             style="arc",

#             outline=PINK_DARK,

#             width=2

#         )

#         mascot.create_oval(

#             19, 45, 29, 51,

#             fill="#FFAEC8",

#             outline=""

#         )

#         mascot.create_oval(

#             59, 45, 69, 51,

#             fill="#FFAEC8",

#             outline=""

#         )

#         mascot.create_text(

#             15, 13,

#             text="✦",

#             fill=PURPLE,

#             font=("Segoe UI", 13, "bold")

#         )

#         mascot.create_text(

#             73, 69,

#             text="♡",

#             fill=PINK_DARK,

#             font=("Segoe UI", 16, "bold")

#         )

#         tk.Label(

#             logo,

#             text="YuiBot",

#             bg=SIDEBAR,

#             fg=TEXT,

#             font=("Segoe UI", 23, "bold")

#         ).pack(pady=(6, 0))

#         tk.Label(

#             logo,

#             text="your little chat friend ♡",

#             bg=SIDEBAR,

#             fg=MUTED,

#             font=("Segoe UI", 9)

#         ).pack()

#         self.sidebar_status = tk.Label(

#             self.sidebar,

#             text="✦ OFFLINE & READY ✦",

#             bg="#EADFFF",

#             fg=PURPLE,

#             font=("Segoe UI", 9, "bold"),

#             padx=10,

#             pady=8

#         )

#         self.sidebar_status.pack(

#             fill="x",

#             padx=18,

#             pady=(0, 16)

#         )

#         self.add_sidebar_button("＋   New Chat", self.new_chat)

#         self.add_sidebar_button("✿   Customize", self.open_settings)

#         self.add_sidebar_button("♡   Rule Studio", self.open_rules)

#         self.add_sidebar_button("📚   Knowledge Garden", self.open_knowledge)

#         self.add_sidebar_button("⌕   Search Chats", self.search_conversation)

#         self.add_sidebar_button("♥   My Memories", self.show_memories)

#         self.add_sidebar_button("✧   Statistics", self.show_statistics)

#         self.add_sidebar_button("?   Help", self.show_help)

#         tk.Frame(

#             self.sidebar,

#             bg=SIDEBAR

#         ).pack(fill="both", expand=True)

#         tk.Label(

#             self.sidebar,

#             text="made with ♡ and Python",

#             bg=SIDEBAR,

#             fg=MUTED,

#             font=("Segoe UI", 9)

#         ).pack(pady=(0, 18))

#         # ---------------- MAIN CONTENT ----------------

#         self.content = tk.Frame(

#             self.root,

#             bg=BG

#         )

#         self.content.grid(

#             row=0, column=1,

#             sticky="nsew"

#         )

#         self.content.grid_rowconfigure(1, weight=1)

#         self.content.grid_columnconfigure(0, weight=1)

#         self.build_header()

#         self.build_chat_area()

#         self.build_input_area()

#     def add_sidebar_button(self, text, command):

#         button = tk.Button(

#             self.sidebar,

#             text=text,

#             command=command,

#             bg=SIDEBAR,

#             fg=TEXT,

#             activebackground="#EAD8FF",

#             activeforeground=PURPLE,

#             font=("Segoe UI", 10),

#             anchor="w",

#             relief="flat",

#             bd=0,

#             padx=20,

#             pady=11,

#             cursor="hand2"

#         )

#         button.pack(fill="x", padx=10, pady=2)

#         button.bind(

#             "<Enter>",

#             lambda event: button.configure(

#                 bg="#EAD8FF"

#             )

#         )

#         button.bind(

#             "<Leave>",

#             lambda event: button.configure(

#                 bg=SIDEBAR

#             )

#         )

#     # ========================================================

#     # HEADER

#     # ========================================================

#     def build_header(self):

#         header = tk.Frame(

#             self.content,

#             bg=BG,

#             padx=24,

#             pady=17

#         )

#         header.grid(

#             row=0, column=0,

#             sticky="ew"

#         )

#         header.grid_columnconfigure(0, weight=1)

#         self.header_title = tk.Label(

#             header,

#             text="Hello, friend! ♡",

#             bg=BG,

#             fg=TEXT,

#             font=("Segoe UI", 20, "bold")

#         )

#         self.header_title.grid(

#             row=0, column=0,

#             sticky="w"

#         )

#         self.header_subtitle = tk.Label(

#             header,

#             text="Let's make today a little more magical.",

#             bg=BG,

#             fg=MUTED,

#             font=("Segoe UI", 10)

#         )

#         self.header_subtitle.grid(

#             row=1, column=0,

#             sticky="w",

#             pady=(4, 0)

#         )

#         tk.Label(

#             header,

#             text="✧  ♡  ✧",

#             bg=BG,

#             fg=PINK_DARK,

#             font=("Segoe UI", 17)

#         ).grid(

#             row=0, column=1,

#             rowspan=2,

#             padx=10

#         )

#         separator = tk.Frame(

#             self.content,

#             bg=BORDER,

#             height=1

#         )

#         separator.grid(

#             row=0, column=0,

#             sticky="sew"

#         )

#     # ========================================================

#     # CHAT AREA

#     # ========================================================

#     def build_chat_area(self):

#         wrapper = tk.Frame(

#             self.content,

#             bg=BG

#         )

#         wrapper.grid(

#             row=1, column=0,

#             sticky="nsew",

#             padx=22,

#             pady=(10, 8)

#         )

#         wrapper.grid_rowconfigure(0, weight=1)

#         wrapper.grid_columnconfigure(0, weight=1)

#         self.chat_canvas = tk.Canvas(

#             wrapper,

#             bg=BG,

#             highlightthickness=0

#         )

#         self.chat_canvas.grid(

#             row=0, column=0,

#             sticky="nsew"

#         )

#         scrollbar = ttk.Scrollbar(

#             wrapper,

#             orient="vertical",

#             command=self.chat_canvas.yview

#         )

#         scrollbar.grid(

#             row=0, column=1,

#             sticky="ns"

#         )

#         self.chat_canvas.configure(

#             yscrollcommand=scrollbar.set

#         )

#         self.message_frame = tk.Frame(

#             self.chat_canvas,

#             bg=BG

#         )

#         self.message_window = self.chat_canvas.create_window(

#             (0, 0),

#             window=self.message_frame,

#             anchor="nw"

#         )

#         self.message_frame.bind(

#             "<Configure>",

#             self.update_scroll_region

#         )

#         self.chat_canvas.bind(

#             "<Configure>",

#             self.resize_message_frame

#         )

#         # Allow scrolling while the mouse is over the chat area, including
#         # message labels and bubbles. The handler ignores other parts of the UI.
#         self.chat_canvas.bind_all("<MouseWheel>", self._on_chat_mousewheel)
#         self.chat_canvas.bind_all("<Button-4>", self._on_chat_mousewheel_linux)
#         self.chat_canvas.bind_all("<Button-5>", self._on_chat_mousewheel_linux)

#     def _mouse_is_over_chat(self):

#         try:
#             x = self.chat_canvas.winfo_pointerx() - self.chat_canvas.winfo_rootx()
#             y = self.chat_canvas.winfo_pointery() - self.chat_canvas.winfo_rooty()
#             return 0 <= x < self.chat_canvas.winfo_width() and 0 <= y < self.chat_canvas.winfo_height()
#         except tk.TclError:
#             return False

#     def _on_chat_mousewheel(self, event):

#         if self._mouse_is_over_chat():
#             # Windows typically sends +/-120 per wheel notch.
#             self.chat_canvas.yview_scroll(int(-event.delta / 120), "units")
#             return "break"

#     def _on_chat_mousewheel_linux(self, event):

#         if self._mouse_is_over_chat():
#             direction = -1 if event.num == 4 else 1
#             self.chat_canvas.yview_scroll(direction, "units")
#             return "break"

#     def update_scroll_region(self, event=None):

#         # Only update the scrollable area here. Do not force the view to the
#         # bottom on every resize, or the user cannot scroll back up.
#         self.chat_canvas.configure(

#             scrollregion=self.chat_canvas.bbox("all")

#         )

#     def resize_message_frame(self, event):

#         self.chat_canvas.itemconfigure(

#             self.message_window,

#             width=event.width

#         )

#     # ========================================================

#     # CHAT BUBBLES

#     # ========================================================

#     def add_message(self, sender, message, role="bot", save=False):

#         if save:

#             self.bot.memory.add_message(

#                 "user" if role == "user" else "bot",

#                 message

#             )

#             self.bot.memory.save()

#         outer = tk.Frame(

#             self.message_frame,

#             bg=BG

#         )

#         outer.pack(

#             fill="x",

#             padx=8,

#             pady=7

#         )

#         is_user = role == "user"

#         bubble_color = "#FFE0EE" if is_user else WHITE

#         name_color = PINK_DARK if is_user else PURPLE

#         align = "e" if is_user else "w"

#         row = tk.Frame(

#             outer,

#             bg=BG

#         )

#         row.pack(

#             anchor=align,

#             fill="x"

#         )

#         bubble = tk.Frame(

#             row,

#             bg=bubble_color,

#             padx=15,

#             pady=11,

#             highlightbackground="#F3D0E3",

#             highlightthickness=1

#         )

#         bubble.pack(

#             side="right" if is_user else "left",

#             padx=(45, 3) if is_user else (3, 45)

#         )

#         tk.Label(

#             bubble,

#             text=sender,

#             bg=bubble_color,

#             fg=name_color,

#             font=("Segoe UI", 9, "bold"),

#             anchor="w"

#         ).pack(

#             anchor="w",

#             pady=(0, 5)

#         )

#         tk.Label(

#             bubble,

#             text=message,

#             bg=bubble_color,

#             fg=TEXT,

#             font=("Segoe UI", 10),

#             justify="left",

#             anchor="w",

#             wraplength=570

#         ).pack(

#             anchor="w"

#         )

#         self.chat_canvas.after_idle(

#             lambda: self.chat_canvas.yview_moveto(1.0)

#         )

#     # ========================================================

#     # INPUT

#     # ========================================================

#     def build_input_area(self):

#         panel = tk.Frame(

#             self.content,

#             bg="#FFF0F7",

#             padx=18,

#             pady=13

#         )

#         panel.grid(

#             row=2, column=0,

#             sticky="ew"

#         )

#         panel.grid_columnconfigure(0, weight=1)

#         tk.Label(

#             panel,

#             text="♡  Say something sweet...",

#             bg="#FFF0F7",

#             fg=MUTED,

#             font=("Segoe UI", 9)

#         ).grid(

#             row=0, column=0,

#             sticky="w",

#             pady=(0, 7)

#         )

#         input_row = tk.Frame(

#             panel,

#             bg="#FFF0F7"

#         )

#         input_row.grid(

#             row=1, column=0,

#             sticky="ew"

#         )

#         input_row.grid_columnconfigure(0, weight=1)

#         self.input = tk.Text(

#             input_row,

#             height=3,

#             wrap="word",

#             font=("Segoe UI", 11),

#             bg=WHITE,

#             fg=TEXT,

#             insertbackground=PURPLE,

#             relief="flat",

#             padx=12,

#             pady=10,

#             highlightthickness=1,

#             highlightbackground=BORDER,

#             highlightcolor=PINK_DARK

#         )

#         self.input.grid(

#             row=0, column=0,

#             sticky="ew"

#         )

#         self.input.bind(

#             "<Control-Return>",

#             self.send_event

#         )

#         self.send_button = tk.Button(

#             input_row,

#             text="Send ♡",

#             command=self.send,

#             bg=PINK,

#             fg="#6D3D5B",

#             activebackground="#FF9FC8",

#             activeforeground=TEXT,

#             font=("Segoe UI", 11, "bold"),

#             relief="flat",

#             bd=0,

#             padx=20,

#             pady=14,

#             cursor="hand2"

#         )

#         self.send_button.grid(

#             row=0, column=1,

#             padx=(10, 0),

#             sticky="ns"

#         )

#         self.status = tk.Label(

#             panel,

#             text="✧ Offline • Ready to chat",

#             bg="#FFF0F7",

#             fg=MUTED,

#             font=("Segoe UI", 9)

#         )

#         self.status.grid(

#             row=2, column=0,

#             sticky="w",

#             pady=(8, 0)

#         )

#     # ========================================================

#     # SEND MESSAGE

#     # ========================================================

#     def send_event(self, event):

#         self.send()

#         return "break"

#     def send(self):

#         if self.busy:

#             return

#         text = self.input.get(

#             "1.0",

#             tk.END

#         ).strip()

#         if not text:

#             return

#         self.input.delete(

#             "1.0",

#             tk.END

#         )

#         self.add_message(

#             "You ♡",

#             text,

#             "user",

#             save=False

#         )

#         # /clear is handled by the GUI.

#         if text.strip().lower() == "/clear":

#             self.clear_conversation()

#             return

#         self.busy = True

#         self.send_button.configure(

#             state="disabled",

#             text="Thinking..."

#         )

#         self.status.configure(

#             text="✧ YuiBot is preparing a reply..."

#         )

#         self.root.after(

#             30,

#             lambda: self.finish_response(text)

#         )

#     def finish_response(self, text):

#         try:

#             response = self.bot.respond(text)

#             if response == "__CLEAR_CHAT__":

#                 self.clear_conversation()

#                 return

#             self.add_message(

#                 self.bot.settings.get(

#                     "bot_name",

#                     "YuiBot"

#                 ) + " ♡",

#                 response,

#                 "bot",

#                 save=False

#             )

#             self.status.configure(

#                 text="✧ Offline • Ready to chat"

#             )

#         except Exception as error:

#             self.add_message(

#                 "YuiBot",

#                 f"Oops! Something went wrong:\n{error}",

#                 "bot"

#             )

#             self.status.configure(

#                 text="✧ Something went wrong"

#             )

#         finally:

#             self.busy = False

#             self.send_button.configure(

#                 state="normal",

#                 text="Send ♡"

#             )

#             self.input.focus_set()

#     # ========================================================

#     # HISTORY

#     # ========================================================

#     def load_history(self):

#         history = self.bot.memory.get_history()

#         if not history:

#             self.add_message(

#                 self.bot.settings.get("bot_name", "YuiBot") + " ♡",

#                 (

#                     "Hiii! Welcome to my little chat garden! 🌸\n\n"

#                     "I'm YuiBot, your offline chat companion.\n\n"

#                     "You can chat with me, teach me new things, "

#                     "create custom rules, or explore my settings.\n\n"

#                     "What shall we talk about today? ♡"

#                 ),

#                 "bot"

#             )

#             return

#         for item in history[-100:]:

#             if item.get("role") == "user":

#                 self.add_message(

#                     "You ♡",

#                     item.get("content", item.get("message", "")),

#                     "user"

#                 )

#             else:

#                 self.add_message(

#                     self.bot.settings.get("bot_name", "YuiBot") + " ♡",

#                     item.get("content", item.get("message", "")),

#                     "bot"

#                 )

#     # ========================================================

#     # HEADER

#     # ========================================================

#     def refresh_header(self):

#         name = self.bot.settings.get(

#             "bot_name",

#             "YuiBot"

#         )

#         personality = self.bot.settings.get(

#             "personality",

#             "Friendly"

#         )

#         self.header_title.configure(

#             text=f"Hello, friend! ♡"

#         )

#         self.header_subtitle.configure(

#             text=f"{name} • {personality} personality • Always offline"

#         )

#         self.sidebar_status.configure(

#             text="✦ OFFLINE & READY ✦"

#         )

#     # ========================================================

#     # NEW CHAT

#     # ========================================================

#     def new_chat(self):

#         self.bot.memory.clear_messages()

#         self.bot.memory.save()

#         for widget in self.message_frame.winfo_children():

#             widget.destroy()

#         self.add_message(

#             self.bot.settings.get("bot_name", "YuiBot") + " ♡",

#             "A fresh new conversation! What would you like to talk about? 🌷",

#             "bot"

#         )

#         self.status.configure(

#             text="✧ New conversation started"

#         )

#     # ========================================================

#     # CLEAR

#     # ========================================================

#     def clear_conversation_event(self, event):

#         self.clear_conversation()

#         return "break"

#     def clear_conversation(self):

#         self.bot.memory.clear_messages()

#         self.bot.memory.save()

#         for widget in self.message_frame.winfo_children():

#             widget.destroy()

#         self.add_message(

#             self.bot.settings.get("bot_name", "YuiBot") + " ♡",

#             "Chat cleared! We can start again whenever you're ready. 🌸",

#             "bot"

#         )

#         self.status.configure(

#             text="✧ Conversation cleared"

#         )

#     # ========================================================

#     # WINDOWS

#     # ========================================================

#     def open_settings(self):

#         SettingsManager(

#             self.root,

#             self.bot.settings,

#             self.refresh_header

#         )

#     def open_rules(self):

#         rules = getattr(self.bot, "rules", None)
#         if rules is None:
#             messagebox.showwarning(
#                 "Rules are not connected",
#                 "The chatbot object does not have a rules manager yet. "
#                 "Please connect your rules module in chatbot.py before opening the Rule Studio.",
#                 parent=self.root
#             )
#             return

#         RuleManager(self.root, rules)

#     def open_knowledge(self):

#         KnowledgeManager(

#             self.root,

#             self.bot.memory

#         )

#     # ========================================================

#     # SEARCH

#     # ========================================================

#     def search_conversation(self):

#         window = tk.Toplevel(self.root)

#         window.title("♡ Search Chat History")

#         window.geometry("720x520")

#         window.configure(bg=BG)

#         tk.Label(

#             window,

#             text="Find a little memory ♡",

#             bg=BG,

#             fg=TEXT,

#             font=("Segoe UI", 17, "bold")

#         ).pack(

#             anchor="w",

#             padx=18,

#             pady=(18, 10)

#         )

#         search_var = tk.StringVar()

#         entry = tk.Entry(

#             window,

#             textvariable=search_var,

#             font=("Segoe UI", 11),

#             bg=WHITE,

#             fg=TEXT,

#             relief="flat"

#         )

#         entry.pack(

#             fill="x",

#             padx=18,

#             ipady=9

#         )

#         result = tk.Text(

#             window,

#             wrap="word",

#             font=("Segoe UI", 10),

#             bg=WHITE,

#             fg=TEXT,

#             relief="flat"

#         )

#         result.pack(

#             fill="both",

#             expand=True,

#             padx=18,

#             pady=12

#         )

#         def search():

#             result.delete("1.0", tk.END)

#             keyword = search_var.get().strip()

#             if not keyword:

#                 return

#             matches = self.bot.memory.search_messages(keyword)

#             if not matches:

#                 result.insert(tk.END, "No matching messages found. ♡")

#                 return

#             for item in matches:

#                 result.insert(

#                     tk.END,

#                     f"{item.get('timestamp', item.get('time', ''))}  "

#                     f"{item.get('role', '')}\n"

#                     f"{item.get('message', '')}\n\n"

#                 )

#         tk.Button(

#             window,

#             text="Search ♡",

#             command=search,

#             bg=PINK,

#             fg=TEXT,

#             relief="flat",

#             padx=20,

#             pady=8

#         ).pack(pady=(0, 15))

#         entry.bind("<Return>", lambda event: search())

#         entry.focus_set()

#     # ========================================================

#     # MEMORIES

#     # ========================================================

#     def show_memories(self):

#         memories = self.bot.memory.get_profile_all()

#         window = tk.Toplevel(self.root)

#         window.title("♡ My Memories")

#         window.geometry("550x450")

#         window.configure(bg=BG)

#         tk.Label(

#             window,

#             text="Things YuiBot remembers ♡",

#             bg=BG,

#             fg=TEXT,

#             font=("Segoe UI", 16, "bold")

#         ).pack(

#             anchor="w",

#             padx=18,

#             pady=15

#         )

#         text = tk.Text(

#             window,

#             wrap="word",

#             bg=WHITE,

#             fg=TEXT,

#             font=("Segoe UI", 11),

#             relief="flat"

#         )

#         text.pack(

#             fill="both",

#             expand=True,

#             padx=18,

#             pady=(0, 18)

#         )

#         if not memories:

#             text.insert(

#                 tk.END,

#                 "No memories saved yet.\n\n"

#                 "Try telling YuiBot:\n"

#                 "my name is Alex\n"

#                 "remember my favorite color is blue"

#             )

#         else:

#             for key, value in memories.items():

#                 text.insert(

#                     tk.END,

#                     f"♡ {key}: {value}\n\n"

#                 )

#         text.configure(state="disabled")

#     # ========================================================

#     # STATISTICS

#     # ========================================================

#     def show_statistics(self):

#         stats = self.bot.memory.get_statistics()

#         window = tk.Toplevel(self.root)

#         window.title("✧ YuiBot Statistics")

#         window.geometry("450x510")

#         window.configure(bg=BG)

#         tk.Label(

#             window,

#             text="Our little progress ✧",

#             bg=BG,

#             fg=TEXT,

#             font=("Segoe UI", 19, "bold")

#         ).pack(pady=(22, 6))

#         tk.Label(

#             window,

#             text="Every conversation adds a little something ♡",

#             bg=BG,

#             fg=MUTED,

#             font=("Segoe UI", 9)

#         ).pack(pady=(0, 18))

#         entries = [

#             ("♡", "User messages", stats.get("user_messages", 0)),

#             ("✿", "Bot replies", stats.get("bot_messages", 0)),

#             ("✧", "Sessions", stats.get("sessions", 0)),

#             ("📚", "Knowledge entries", stats.get("knowledge_entries", 0)),

#             ("♥", "Saved memories", stats.get("memories", 0)),

#             ("🧩", "Rules matched", stats.get("rules_matched", 0)),

#             ("🌷", "Rules created", stats.get("rules_created", 0))

#         ]

#         for symbol, label, value in entries:

#             card = tk.Frame(

#                 window,

#                 bg=WHITE,

#                 padx=14,

#                 pady=9

#             )

#             card.pack(

#                 fill="x",

#                 padx=22,

#                 pady=4

#             )

#             tk.Label(

#                 card,

#                 text=f"{symbol}  {label}",

#                 bg=WHITE,

#                 fg=TEXT,

#                 font=("Segoe UI", 10)

#             ).pack(side="left")

#             tk.Label(

#                 card,

#                 text=str(value),

#                 bg=WHITE,

#                 fg=PURPLE,

#                 font=("Segoe UI", 11, "bold")

#             ).pack(side="right")

#     # ========================================================

#     # HELP

#     # ========================================================

#     def show_help(self):

#         messagebox.showinfo(

#             "♡ YuiBot Help",

#             "Cute things to try!\n\n"

#             "hello\n"

#             "what is Python?\n"

#             "2 + 5 * 3\n"

#             "my name is Alex\n"

#             "what is my name?\n"

#             "remember my favorite color is blue\n\n"

#             "Teach YuiBot:\n"

#             "teach: what is my project = My project is YuiBot.\n\n"

#             "Commands:\n"

#             "/help\n"

#             "/time\n"

#             "/date\n"

#             "/memory\n"

#             "/knowledge\n"

#             "/stats\n"

#             "/rules\n"

#             "/ruletest hello\n"

#             "/search hello\n"

#             "/settings\n"

#             "/clear"

#         )

#     # ========================================================

#     # CLOSE

#     # ========================================================

#     def close(self):

#         # Save the components that are present in this YuiBot version.
#         # Some versions of YuiBot do not expose a self.bot.rules attribute.
#         try:
#             memory = getattr(self.bot, "memory", None)
#             if memory is not None and hasattr(memory, "save"):
#                 memory.save()

#             settings = getattr(self.bot, "settings", None)
#             if settings is not None and hasattr(settings, "save"):
#                 settings.save()

#             rules = getattr(self.bot, "rules", None)
#             if rules is not None and hasattr(rules, "save"):
#                 rules.save()
#         except Exception as exc:
#             messagebox.showerror(
#                 "Save warning",
#                 f"YuiBot could not save all data before closing:\n{exc}",
#                 parent=self.root
#             )
#         finally:
#             self.root.destroy()

# def main():

#     root = tk.Tk()

#     YuiBotApp(root)

#     root.mainloop()

# if __name__ == "__main__":

#     main()





import tkinter as tk

from tkinter import ttk, messagebox

import random

from chatbot import YuiBot

from settings_manager import SettingsManager

from knowledge_manager import KnowledgeManager

from rule_manager import RuleManager

# ============================================================

# YUIBOT KAWAII THEME

# ============================================================

BG = "#FFF6FA"

SIDEBAR = "#F6E8FF"

PINK = "#FFB7D5"

PINK_DARK = "#E887B3"

LAVENDER = "#DCCBFF"

PURPLE = "#9274C8"

CREAM = "#FFFDF8"

WHITE = "#FFFFFF"

TEXT = "#59465F"

MUTED = "#A18DA8"

GREEN = "#A7DDBB"

BORDER = "#F0D9EC"

class YuiBotApp:

    def __init__(self, root):

        self.root = root

        self.bot = YuiBot()

        self.root.title("YuiBot ♡ My Little Chat Companion")

        self.root.geometry("1180x780")

        self.root.minsize(900, 650)

        self.root.configure(bg=BG)

        self.chat_messages = []

        self.busy = False

        self.setup_style()

        self.build_ui()

        self.load_history()

        self.refresh_header()

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.root.bind("<Control-Return>", self.send_event)

        self.root.bind("<Control-l>", self.clear_conversation_event)

    # ========================================================

    # STYLE

    # ========================================================

    def setup_style(self):

        style = ttk.Style()

        try:

            style.theme_use("clam")

        except tk.TclError:

            pass

        style.configure(

            "Cute.TButton",

            font=("Segoe UI", 10),

            background=WHITE,

            foreground=TEXT,

            padding=(10, 9),

            borderwidth=0

        )

        style.map(

            "Cute.TButton",

            background=[

                ("active", "#FFE0EE"),

                ("pressed", PINK)

            ]

        )

        style.configure(

            "Pink.TButton",

            font=("Segoe UI", 11, "bold"),

            background=PINK,

            foreground="#6D3D5B",

            padding=(18, 12),

            borderwidth=0

        )

        style.map(

            "Pink.TButton",

            background=[

                ("active", "#FF9FC8"),

                ("pressed", PINK_DARK)

            ]

        )

        style.configure(

            "Cute.TEntry",

            padding=10,

            fieldbackground=WHITE,

            foreground=TEXT

        )

    # ========================================================

    # HELPERS

    # ========================================================

    def rounded_rect(

        self, canvas, x1, y1, x2, y2,

        radius=18, fill=WHITE, outline=""

    ):

        radius = min(

            radius,

            (x2 - x1) / 2,

            (y2 - y1) / 2

        )

        points = [

            x1 + radius, y1,

            x2 - radius, y1,

            x2, y1,

            x2, y1 + radius,

            x2, y2 - radius,

            x2, y2,

            x2 - radius, y2,

            x1 + radius, y2,

            x1, y2,

            x1, y2 - radius,

            x1, y1 + radius,

            x1, y1

        ]

        return canvas.create_polygon(

            points,

            smooth=True,

            fill=fill,

            outline=outline

        )

    def make_card(self, parent, color=WHITE, padding=12):

        frame = tk.Frame(

            parent,

            bg=color,

            padx=padding,

            pady=padding,

            highlightbackground=BORDER,

            highlightthickness=1

        )

        return frame

    # ========================================================

    # MAIN WINDOW

    # ========================================================

    def build_ui(self):

        self.root.grid_rowconfigure(0, weight=1)

        self.root.grid_columnconfigure(1, weight=1)

        # ---------------- SIDEBAR ----------------

        self.sidebar = tk.Frame(

            self.root,

            bg=SIDEBAR,

            width=238

        )

        self.sidebar.grid(

            row=0, column=0,

            sticky="ns"

        )

        self.sidebar.grid_propagate(False)

        # Mascot / logo panel

        logo = tk.Frame(

            self.sidebar,

            bg=SIDEBAR

        )

        logo.pack(fill="x", padx=18, pady=(22, 20))

        mascot = tk.Canvas(

            logo,

            width=88,

            height=88,

            bg=SIDEBAR,

            highlightthickness=0

        )

        mascot.pack()

        # Cute character face

        mascot.create_oval(

            12, 12, 76, 76,

            fill="#FFE1EE",

            outline="#F6B9D4",

            width=2

        )

        mascot.create_oval(

            29, 37, 35, 45,

            fill=TEXT,

            outline=""

        )

        mascot.create_oval(

            53, 37, 59, 45,

            fill=TEXT,

            outline=""

        )

        mascot.create_arc(

            34, 39, 54, 58,

            start=205, extent=130,

            style="arc",

            outline=PINK_DARK,

            width=2

        )

        mascot.create_oval(

            19, 45, 29, 51,

            fill="#FFAEC8",

            outline=""

        )

        mascot.create_oval(

            59, 45, 69, 51,

            fill="#FFAEC8",

            outline=""

        )

        mascot.create_text(

            15, 13,

            text="✦",

            fill=PURPLE,

            font=("Segoe UI", 13, "bold")

        )

        mascot.create_text(

            73, 69,

            text="♡",

            fill=PINK_DARK,

            font=("Segoe UI", 16, "bold")

        )

        tk.Label(

            logo,

            text="YuiBot",

            bg=SIDEBAR,

            fg=TEXT,

            font=("Segoe UI", 23, "bold")

        ).pack(pady=(6, 0))

        tk.Label(

            logo,

            text="your little chat friend ♡",

            bg=SIDEBAR,

            fg=MUTED,

            font=("Segoe UI", 9)

        ).pack()

        self.sidebar_status = tk.Label(

            self.sidebar,

            text="✦ OFFLINE & READY ✦",

            bg="#EADFFF",

            fg=PURPLE,

            font=("Segoe UI", 9, "bold"),

            padx=10,

            pady=8

        )

        self.sidebar_status.pack(

            fill="x",

            padx=18,

            pady=(0, 16)

        )

        self.add_sidebar_button("＋   New Chat", self.new_chat)

        self.add_sidebar_button("✿   Customize", self.open_settings)

        self.add_sidebar_button("♡   Rule Studio", self.open_rules)

        self.add_sidebar_button("📚   Knowledge Garden", self.open_knowledge)

        self.add_sidebar_button("⌕   Search Chats", self.search_conversation)

        self.add_sidebar_button("♥   My Memories", self.show_memories)

        self.add_sidebar_button("✧   Statistics", self.show_statistics)

        self.add_sidebar_button("?   Help", self.show_help)

        tk.Frame(

            self.sidebar,

            bg=SIDEBAR

        ).pack(fill="both", expand=True)

        tk.Label(

            self.sidebar,

            text="made with ♡ and Python",

            bg=SIDEBAR,

            fg=MUTED,

            font=("Segoe UI", 9)

        ).pack(pady=(0, 18))

        # ---------------- MAIN CONTENT ----------------

        self.content = tk.Frame(

            self.root,

            bg=BG

        )

        self.content.grid(

            row=0, column=1,

            sticky="nsew"

        )

        self.content.grid_rowconfigure(1, weight=1)

        self.content.grid_columnconfigure(0, weight=1)

        self.build_header()

        self.build_chat_area()

        self.build_input_area()

    def add_sidebar_button(self, text, command):

        button = tk.Button(

            self.sidebar,

            text=text,

            command=command,

            bg=SIDEBAR,

            fg=TEXT,

            activebackground="#EAD8FF",

            activeforeground=PURPLE,

            font=("Segoe UI", 10),

            anchor="w",

            relief="flat",

            bd=0,

            padx=20,

            pady=11,

            cursor="hand2"

        )

        button.pack(fill="x", padx=10, pady=2)

        button.bind(

            "<Enter>",

            lambda event: button.configure(

                bg="#EAD8FF"

            )

        )

        button.bind(

            "<Leave>",

            lambda event: button.configure(

                bg=SIDEBAR

            )

        )

    # ========================================================

    # HEADER

    # ========================================================

    def build_header(self):

        header = tk.Frame(

            self.content,

            bg=BG,

            padx=24,

            pady=17

        )

        header.grid(

            row=0, column=0,

            sticky="ew"

        )

        header.grid_columnconfigure(0, weight=1)

        self.header_title = tk.Label(

            header,

            text="Hello, friend! ♡",

            bg=BG,

            fg=TEXT,

            font=("Segoe UI", 20, "bold")

        )

        self.header_title.grid(

            row=0, column=0,

            sticky="w"

        )

        self.header_subtitle = tk.Label(

            header,

            text="Let's make today a little more magical.",

            bg=BG,

            fg=MUTED,

            font=("Segoe UI", 10)

        )

        self.header_subtitle.grid(

            row=1, column=0,

            sticky="w",

            pady=(4, 0)

        )

        tk.Label(

            header,

            text="✧  ♡  ✧",

            bg=BG,

            fg=PINK_DARK,

            font=("Segoe UI", 17)

        ).grid(

            row=0, column=1,

            rowspan=2,

            padx=10

        )

        separator = tk.Frame(

            self.content,

            bg=BORDER,

            height=1

        )

        separator.grid(

            row=0, column=0,

            sticky="sew"

        )

    # ========================================================

    # CHAT AREA

    # ========================================================

    def build_chat_area(self):

        wrapper = tk.Frame(

            self.content,

            bg=BG

        )

        wrapper.grid(

            row=1, column=0,

            sticky="nsew",

            padx=22,

            pady=(10, 8)

        )

        wrapper.grid_rowconfigure(0, weight=1)

        wrapper.grid_columnconfigure(0, weight=1)

        self.chat_canvas = tk.Canvas(

            wrapper,

            bg=BG,

            highlightthickness=0

        )

        self.chat_canvas.grid(

            row=0, column=0,

            sticky="nsew"

        )

        scrollbar = ttk.Scrollbar(

            wrapper,

            orient="vertical",

            command=self.chat_canvas.yview

        )

        scrollbar.grid(

            row=0, column=1,

            sticky="ns"

        )

        self.chat_canvas.configure(

            yscrollcommand=scrollbar.set

        )

        self.message_frame = tk.Frame(

            self.chat_canvas,

            bg=BG

        )

        self.message_window = self.chat_canvas.create_window(

            (0, 0),

            window=self.message_frame,

            anchor="nw"

        )

        self.message_frame.bind(

            "<Configure>",

            self.update_scroll_region

        )

        self.chat_canvas.bind(

            "<Configure>",

            self.resize_message_frame

        )

        # Allow scrolling while the mouse is over the chat area, including
        # message labels and bubbles. The handler ignores other parts of the UI.
        self.chat_canvas.bind_all("<MouseWheel>", self._on_chat_mousewheel)
        self.chat_canvas.bind_all("<Button-4>", self._on_chat_mousewheel_linux)
        self.chat_canvas.bind_all("<Button-5>", self._on_chat_mousewheel_linux)

    def _mouse_is_over_chat(self):

        try:
            x = self.chat_canvas.winfo_pointerx() - self.chat_canvas.winfo_rootx()
            y = self.chat_canvas.winfo_pointery() - self.chat_canvas.winfo_rooty()
            return 0 <= x < self.chat_canvas.winfo_width() and 0 <= y < self.chat_canvas.winfo_height()
        except tk.TclError:
            return False

    def _on_chat_mousewheel(self, event):

        if self._mouse_is_over_chat():
            # Windows typically sends +/-120 per wheel notch.
            self.chat_canvas.yview_scroll(int(-event.delta / 120), "units")
            return "break"

    def _on_chat_mousewheel_linux(self, event):

        if self._mouse_is_over_chat():
            direction = -1 if event.num == 4 else 1
            self.chat_canvas.yview_scroll(direction, "units")
            return "break"

    def update_scroll_region(self, event=None):

        # Only update the scrollable area here. Do not force the view to the
        # bottom on every resize, or the user cannot scroll back up.
        self.chat_canvas.configure(

            scrollregion=self.chat_canvas.bbox("all")

        )

    def resize_message_frame(self, event):

        self.chat_canvas.itemconfigure(

            self.message_window,

            width=event.width

        )

    # ========================================================

    # CHAT BUBBLES

    # ========================================================

    def add_message(self, sender, message, role="bot", save=False):

        if save:

            self.bot.memory.add_message(

                "user" if role == "user" else "bot",

                message

            )

            self.bot.memory.save()

        outer = tk.Frame(

            self.message_frame,

            bg=BG

        )

        outer.pack(

            fill="x",

            padx=8,

            pady=7

        )

        is_user = role == "user"

        bubble_color = "#FFE0EE" if is_user else WHITE

        name_color = PINK_DARK if is_user else PURPLE

        align = "e" if is_user else "w"

        row = tk.Frame(

            outer,

            bg=BG

        )

        row.pack(

            anchor=align,

            fill="x"

        )

        bubble = tk.Frame(

            row,

            bg=bubble_color,

            padx=15,

            pady=11,

            highlightbackground="#F3D0E3",

            highlightthickness=1

        )

        bubble.pack(

            side="right" if is_user else "left",

            padx=(45, 3) if is_user else (3, 45)

        )

        tk.Label(

            bubble,

            text=sender,

            bg=bubble_color,

            fg=name_color,

            font=("Segoe UI", 9, "bold"),

            anchor="w"

        ).pack(

            anchor="w",

            pady=(0, 5)

        )

        tk.Label(

            bubble,

            text=message,

            bg=bubble_color,

            fg=TEXT,

            font=("Segoe UI", 10),

            justify="left",

            anchor="w",

            wraplength=570

        ).pack(

            anchor="w"

        )

        self.chat_canvas.after_idle(

            lambda: self.chat_canvas.yview_moveto(1.0)

        )

    # ========================================================

    # INPUT

    # ========================================================

    def build_input_area(self):

        panel = tk.Frame(

            self.content,

            bg="#FFF0F7",

            padx=18,

            pady=13

        )

        panel.grid(

            row=2, column=0,

            sticky="ew"

        )

        panel.grid_columnconfigure(0, weight=1)

        tk.Label(

            panel,

            text="♡  Say something sweet...",

            bg="#FFF0F7",

            fg=MUTED,

            font=("Segoe UI", 9)

        ).grid(

            row=0, column=0,

            sticky="w",

            pady=(0, 7)

        )

        input_row = tk.Frame(

            panel,

            bg="#FFF0F7"

        )

        input_row.grid(

            row=1, column=0,

            sticky="ew"

        )

        input_row.grid_columnconfigure(0, weight=1)

        self.input = tk.Text(

            input_row,

            height=3,

            wrap="word",

            font=("Segoe UI", 11),

            bg=WHITE,

            fg=TEXT,

            insertbackground=PURPLE,

            relief="flat",

            padx=12,

            pady=10,

            highlightthickness=1,

            highlightbackground=BORDER,

            highlightcolor=PINK_DARK

        )

        self.input.grid(

            row=0, column=0,

            sticky="ew"

        )

        self.input.bind(

            "<Control-Return>",

            self.send_event

        )

        self.send_button = tk.Button(

            input_row,

            text="Send ♡",

            command=self.send,

            bg=PINK,

            fg="#6D3D5B",

            activebackground="#FF9FC8",

            activeforeground=TEXT,

            font=("Segoe UI", 11, "bold"),

            relief="flat",

            bd=0,

            padx=20,

            pady=14,

            cursor="hand2"

        )

        self.send_button.grid(

            row=0, column=1,

            padx=(10, 0),

            sticky="ns"

        )

        self.status = tk.Label(

            panel,

            text="✧ Offline • Ready to chat",

            bg="#FFF0F7",

            fg=MUTED,

            font=("Segoe UI", 9)

        )

        self.status.grid(

            row=2, column=0,

            sticky="w",

            pady=(8, 0)

        )

    # ========================================================

    # SEND MESSAGE

    # ========================================================

    def send_event(self, event):

        self.send()

        return "break"

    def send(self):

        if self.busy:

            return

        text = self.input.get(

            "1.0",

            tk.END

        ).strip()

        if not text:

            return

        self.input.delete(

            "1.0",

            tk.END

        )

        self.add_message(

            "You ♡",

            text,

            "user",

            save=False

        )

        # /clear is handled by the GUI.

        if text.strip().lower() == "/clear":

            self.clear_conversation()

            return

        self.busy = True

        self.send_button.configure(

            state="disabled",

            text="Thinking..."

        )

        self.status.configure(

            text="✧ YuiBot is preparing a reply..."

        )

        self.root.after(

            30,

            lambda: self.finish_response(text)

        )

    def finish_response(self, text):

        try:

            response = self.bot.respond(text)

            if response == "__CLEAR_CHAT__":

                self.clear_conversation()

                return

            self.add_message(

                self.bot.settings.get(

                    "bot_name",

                    "YuiBot"

                ) + " ♡",

                response,

                "bot",

                save=False

            )

            self.status.configure(

                text="✧ Offline • Ready to chat"

            )

        except Exception as error:

            self.add_message(

                "YuiBot",

                f"Oops! Something went wrong:\n{error}",

                "bot"

            )

            self.status.configure(

                text="✧ Something went wrong"

            )

        finally:

            self.busy = False

            self.send_button.configure(

                state="normal",

                text="Send ♡"

            )

            self.input.focus_set()

    # ========================================================

    # HISTORY

    # ========================================================

    def load_history(self):

        history = self.bot.memory.get_history()

        if not history:

            self.add_message(

                self.bot.settings.get("bot_name", "YuiBot") + " ♡",

                (

                    "Hiii! Welcome to my little chat garden! 🌸\n\n"

                    "I'm YuiBot, your offline chat companion.\n\n"

                    "You can chat with me, teach me new things, "

                    "create custom rules, or explore my settings.\n\n"

                    "What shall we talk about today? ♡"

                ),

                "bot"

            )

            return

        for item in history[-100:]:

            if item.get("role") == "user":

                self.add_message(

                    "You ♡",

                    item.get("content", item.get("message", "")),

                    "user"

                )

            else:

                self.add_message(

                    self.bot.settings.get("bot_name", "YuiBot") + " ♡",

                    item.get("content", item.get("message", "")),

                    "bot"

                )

    # ========================================================

    # HEADER

    # ========================================================

    def refresh_header(self):

        name = self.bot.settings.get(

            "bot_name",

            "YuiBot"

        )

        personality = self.bot.settings.get(

            "personality",

            "Friendly"

        )

        self.header_title.configure(

            text=f"Hello, friend! ♡"

        )

        self.header_subtitle.configure(

            text=f"{name} • {personality} personality • Always offline"

        )

        self.sidebar_status.configure(

            text="✦ OFFLINE & READY ✦"

        )

    # ========================================================

    # NEW CHAT

    # ========================================================

    def new_chat(self):

        self.bot.memory.clear_messages()

        self.bot.memory.save()

        for widget in self.message_frame.winfo_children():

            widget.destroy()

        self.add_message(

            self.bot.settings.get("bot_name", "YuiBot") + " ♡",

            "A fresh new conversation! What would you like to talk about? 🌷",

            "bot"

        )

        self.status.configure(

            text="✧ New conversation started"

        )

    # ========================================================

    # CLEAR

    # ========================================================

    def clear_conversation_event(self, event):

        self.clear_conversation()

        return "break"

    def clear_conversation(self):

        self.bot.memory.clear_messages()

        self.bot.memory.save()

        for widget in self.message_frame.winfo_children():

            widget.destroy()

        self.add_message(

            self.bot.settings.get("bot_name", "YuiBot") + " ♡",

            "Chat cleared! We can start again whenever you're ready. 🌸",

            "bot"

        )

        self.status.configure(

            text="✧ Conversation cleared"

        )

    # ========================================================

    # WINDOWS

    # ========================================================

    def open_settings(self):

        SettingsManager(

            self.root,

            self.bot.settings,

            self.refresh_header

        )

    def open_rules(self):

        rules = getattr(self.bot, "rules", None)
        if rules is None:
            messagebox.showwarning(
                "Rules are not connected",
                "The chatbot object does not have a rules manager yet. "
                "Please connect your rules module in chatbot.py before opening the Rule Studio.",
                parent=self.root
            )
            return

        RuleManager(self.root, rules)

    def open_knowledge(self):

        KnowledgeManager(

            self.root,

            self.bot.knowledge

        )

    # ========================================================

    # SEARCH

    # ========================================================

    def search_conversation(self):

        window = tk.Toplevel(self.root)

        window.title("♡ Search Chat History")

        window.geometry("720x520")

        window.configure(bg=BG)

        tk.Label(

            window,

            text="Find a little memory ♡",

            bg=BG,

            fg=TEXT,

            font=("Segoe UI", 17, "bold")

        ).pack(

            anchor="w",

            padx=18,

            pady=(18, 10)

        )

        search_var = tk.StringVar()

        entry = tk.Entry(

            window,

            textvariable=search_var,

            font=("Segoe UI", 11),

            bg=WHITE,

            fg=TEXT,

            relief="flat"

        )

        entry.pack(

            fill="x",

            padx=18,

            ipady=9

        )

        result = tk.Text(

            window,

            wrap="word",

            font=("Segoe UI", 10),

            bg=WHITE,

            fg=TEXT,

            relief="flat"

        )

        result.pack(

            fill="both",

            expand=True,

            padx=18,

            pady=12

        )

        def search():

            result.delete("1.0", tk.END)

            keyword = search_var.get().strip()

            if not keyword:

                return

            matches = self.bot.memory.search_messages(keyword)

            if not matches:

                result.insert(tk.END, "No matching messages found. ♡")

                return

            for item in matches:

                result.insert(

                    tk.END,

                    f"{item.get('timestamp', item.get('time', ''))}  "

                    f"{item.get('role', '')}\n"

                    f"{item.get('message', '')}\n\n"

                )

        tk.Button(

            window,

            text="Search ♡",

            command=search,

            bg=PINK,

            fg=TEXT,

            relief="flat",

            padx=20,

            pady=8

        ).pack(pady=(0, 15))

        entry.bind("<Return>", lambda event: search())

        entry.focus_set()

    # ========================================================

    # MEMORIES

    # ========================================================

    def show_memories(self):

        memories = self.bot.memory.get_profile_all()

        window = tk.Toplevel(self.root)

        window.title("♡ My Memories")

        window.geometry("550x450")

        window.configure(bg=BG)

        tk.Label(

            window,

            text="Things YuiBot remembers ♡",

            bg=BG,

            fg=TEXT,

            font=("Segoe UI", 16, "bold")

        ).pack(

            anchor="w",

            padx=18,

            pady=15

        )

        text = tk.Text(

            window,

            wrap="word",

            bg=WHITE,

            fg=TEXT,

            font=("Segoe UI", 11),

            relief="flat"

        )

        text.pack(

            fill="both",

            expand=True,

            padx=18,

            pady=(0, 18)

        )

        if not memories:

            text.insert(

                tk.END,

                "No memories saved yet.\n\n"

                "Try telling YuiBot:\n"

                "my name is Alex\n"

                "remember my favorite color is blue"

            )

        else:

            for key, value in memories.items():

                text.insert(

                    tk.END,

                    f"♡ {key}: {value}\n\n"

                )

        text.configure(state="disabled")

    # ========================================================

    # STATISTICS

    # ========================================================

    def show_statistics(self):

        stats = self.bot.memory.get_statistics()

        window = tk.Toplevel(self.root)

        window.title("✧ YuiBot Statistics")

        window.geometry("450x510")

        window.configure(bg=BG)

        tk.Label(

            window,

            text="Our little progress ✧",

            bg=BG,

            fg=TEXT,

            font=("Segoe UI", 19, "bold")

        ).pack(pady=(22, 6))

        tk.Label(

            window,

            text="Every conversation adds a little something ♡",

            bg=BG,

            fg=MUTED,

            font=("Segoe UI", 9)

        ).pack(pady=(0, 18))

        entries = [

            ("♡", "User messages", stats.get("user_messages", 0)),

            ("✿", "Bot replies", stats.get("bot_messages", 0)),

            ("✧", "Sessions", stats.get("sessions", 0)),

            ("📚", "Knowledge entries", len(self.bot.knowledge.get_all())),

            ("♥", "Saved memories", stats.get("memories", 0)),

            ("🧩", "Rules matched", stats.get("rules_matched", 0)),

            ("🌷", "Rules created", stats.get("rules_created", 0))

        ]

        for symbol, label, value in entries:

            card = tk.Frame(

                window,

                bg=WHITE,

                padx=14,

                pady=9

            )

            card.pack(

                fill="x",

                padx=22,

                pady=4

            )

            tk.Label(

                card,

                text=f"{symbol}  {label}",

                bg=WHITE,

                fg=TEXT,

                font=("Segoe UI", 10)

            ).pack(side="left")

            tk.Label(

                card,

                text=str(value),

                bg=WHITE,

                fg=PURPLE,

                font=("Segoe UI", 11, "bold")

            ).pack(side="right")

    # ========================================================

    # HELP

    # ========================================================

    def show_help(self):

        messagebox.showinfo(

            "♡ YuiBot Help",

            "Cute things to try!\n\n"

            "hello\n"

            "what is Python?\n"

            "2 + 5 * 3\n"

            "my name is Alex\n"

            "what is my name?\n"

            "remember my favorite color is blue\n\n"

            "Teach YuiBot:\n"

            "teach: what is my project = My project is YuiBot.\n\n"

            "Commands:\n"

            "/help\n"

            "/time\n"

            "/date\n"

            "/memory\n"

            "/knowledge\n"

            "/stats\n"

            "/rules\n"

            "/ruletest hello\n"

            "/search hello\n"

            "/settings\n"

            "/clear"

        )

    # ========================================================

    # CLOSE

    # ========================================================

    def close(self):

        # Save the components that are present in this YuiBot version.
        # Some versions of YuiBot do not expose a self.bot.rules attribute.
        try:
            memory = getattr(self.bot, "memory", None)
            if memory is not None and hasattr(memory, "save"):
                memory.save()

            settings = getattr(self.bot, "settings", None)
            if settings is not None and hasattr(settings, "save"):
                settings.save()

            rules = getattr(self.bot, "rules", None)
            if rules is not None and hasattr(rules, "save"):
                rules.save()

            knowledge = getattr(self.bot, "knowledge", None)
            if knowledge is not None and hasattr(knowledge, "save"):
                knowledge.save()
        except Exception as exc:
            messagebox.showerror(
                "Save warning",
                f"YuiBot could not save all data before closing:\n{exc}",
                parent=self.root
            )
        finally:
            self.root.destroy()

def main():

    root = tk.Tk()

    YuiBotApp(root)

    root.mainloop()

if __name__ == "__main__":

    main()
