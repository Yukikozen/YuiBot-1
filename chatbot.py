# # import ast
# # import datetime
# # import difflib
# # import operator
# # import random
# # import re

# # from memory import ChatMemory
# # from settings import Settings
# # from knowledge import BUILT_IN_KNOWLEDGE


# # class YuiBot:

# #     def __init__(self):

# #         self.memory = ChatMemory()
# #         self.settings = Settings()

# #         self.last_intent = None
# #         self.last_topic = None
# #         self.last_question = None

# #         self.memory.new_session()

# #         self.responses = {

# #             "Friendly": {

# #                 "greeting": [
# #                     "Hello!",
# #                     "Hi!",
# #                     "Hey!",
# #                     "Hello! How can I help?"
# #                 ],

# #                 "thanks": [
# #                     "You're welcome!",
# #                     "No problem!",
# #                     "Glad I could help!"
# #                 ],

# #                 "goodbye": [
# #                     "Goodbye!",
# #                     "See you later!",
# #                     "Bye!"
# #                 ]
# #             },

# #             "Professional": {

# #                 "greeting": [
# #                     "Hello. How may I assist you?",
# #                     "Hello. What would you like to know?",
# #                     "Good day. How can I help?"
# #                 ],

# #                 "thanks": [
# #                     "You're welcome.",
# #                     "You're welcome. I'm glad I could help."
# #                 ],

# #                 "goodbye": [
# #                     "Goodbye.",
# #                     "Have a good day.",
# #                     "Until next time."
# #                 ]
# #             },

# #             "Short": {

# #                 "greeting": [
# #                     "Hi!",
# #                     "Hello!",
# #                     "Hey!"
# #                 ],

# #                 "thanks": [
# #                     "You're welcome.",
# #                     "No problem."
# #                 ],

# #                 "goodbye": [
# #                     "Bye!",
# #                     "See you!"
# #                 ]
# #             },

# #             "Casual": {

# #                 "greeting": [
# #                     "Hey!",
# #                     "Yo!",
# #                     "Hi there!"
# #                 ],

# #                 "thanks": [
# #                     "No worries!",
# #                     "Anytime!",
# #                     "Sure thing!"
# #                 ],

# #                 "goodbye": [
# #                     "Later!",
# #                     "Bye!",
# #                     "See ya!"
# #                 ]
# #             }
# #         }

# #         self.typos = {

# #             "helo": "hello",
# #             "helllo": "hello",
# #             "hllo": "hello",
# #             "hii": "hi",
# #             "hiiii": "hi",
# #             "heyy": "hey",

# #             "wht": "what",
# #             "whatt": "what",
# #             "wat": "what",
# #             "wut": "what",

# #             "whos": "who is",
# #             "whats": "what is",

# #             "ur": "your",
# #             "u": "you",
# #             "r": "are",

# #             "pls": "please",
# #             "plz": "please",
# #             "thx": "thanks",

# #             "im": "i am",
# #             "idk": "i do not know",

# #             "tim": "time",
# #             "todai": "today",

# #             "calcluate": "calculate",
# #             "calculte": "calculate",

# #             "favrite": "favorite",
# #             "favouritee": "favorite",

# #             "pyhton": "python",
# #             "pythn": "python",

# #             "databse": "database",
# #             "javscript": "javascript"
# #         }

# #     # ==========================================================
# #     # SETTINGS
# #     # ==========================================================

# #     def reload_settings(self):

# #         self.settings.load()

# #     def personality(
# #         self,
# #         category
# #     ):

# #         mode = self.settings.get(
# #             "personality",
# #             "Friendly"
# #         )

# #         group = self.responses.get(
# #             mode,
# #             self.responses[
# #                 "Friendly"
# #             ]
# #         )

# #         values = group.get(
# #             category,
# #             []
# #         )

# #         if not values:
# #             return ""

# #         return random.choice(
# #             values
# #         )

# #     # ==========================================================
# #     # NORMALIZE
# #     # ==========================================================

# #     def normalize(
# #         self,
# #         text
# #     ):

# #         text = text.lower().strip()

# #         text = re.sub(
# #             r"\s+",
# #             " ",
# #             text
# #         )

# #         words = text.split()

# #         fixed = []

# #         for word in words:

# #             punctuation = ""

# #             while (
# #                 word
# #                 and word[-1] in ".,!?"
# #             ):

# #                 punctuation = (
# #                     word[-1]
# #                     + punctuation
# #                 )

# #                 word = word[:-1]

# #             word = self.typos.get(
# #                 word,
# #                 word
# #             )

# #             fixed.append(
# #                 word + punctuation
# #             )

# #         text = " ".join(
# #             fixed
# #         )

# #         text = re.sub(
# #             r"\bwhat's\b",
# #             "what is",
# #             text
# #         )

# #         text = re.sub(
# #             r"\bwho's\b",
# #             "who is",
# #             text
# #         )

# #         return text

# #     # ==========================================================
# #     # SIMILARITY
# #     # ==========================================================

# #     def similarity(
# #         self,
# #         a,
# #         b
# #     ):

# #         if not self.settings.get(
# #             "fuzzy_matching",
# #             True
# #         ):

# #             return 1.0 if a == b else 0

# #         a = a.lower().strip()
# #         b = b.lower().strip()

# #         if a == b:
# #             return 1.0

# #         if a in b or b in a:
# #             return 0.92

# #         ratio = difflib.SequenceMatcher(
# #             None,
# #             a,
# #             b
# #         ).ratio()

# #         a_words = set(
# #             re.findall(
# #                 r"\b\w+\b",
# #                 a
# #             )
# #         )

# #         b_words = set(
# #             re.findall(
# #                 r"\b\w+\b",
# #                 b
# #             )
# #         )

# #         if a_words and b_words:

# #             overlap = len(
# #                 a_words & b_words
# #             ) / max(
# #                 len(a_words),
# #                 len(b_words)
# #             )

# #         else:

# #             overlap = 0

# #         return max(
# #             ratio,
# #             overlap
# #         )

# #     # ==========================================================
# #     # KNOWLEDGE
# #     # ==========================================================

# #     def search_knowledge(
# #         self,
# #         question
# #     ):

# #         question = self.normalize(
# #             question
# #         )

# #         all_knowledge = {}

# #         for key, value in BUILT_IN_KNOWLEDGE.items():

# #             all_knowledge[
# #                 key
# #             ] = {
# #                 "answer": value,
# #                 "category": "Built-in"
# #             }

# #         all_knowledge.update(
# #             self.memory.get_knowledge()
# #         )

# #         if question in all_knowledge:

# #             item = all_knowledge[
# #                 question
# #             ]

# #             return (
# #                 item["answer"],
# #                 1.0,
# #                 item.get(
# #                     "category",
# #                     "General"
# #                 )
# #             )

# #         best = None
# #         best_score = 0

# #         for key, item in all_knowledge.items():

# #             score = self.similarity(
# #                 question,
# #                 key
# #             )

# #             if score > best_score:

# #                 best_score = score
# #                 best = item

# #         if (
# #             best is not None
# #             and best_score >= 0.58
# #         ):

# #             return (
# #                 best["answer"],
# #                 best_score,
# #                 best.get(
# #                     "category",
# #                     "General"
# #                 )
# #             )

# #         return None, 0, None

# #     # ==========================================================
# #     # MEMORY
# #     # ==========================================================

# #     def remember_fact(
# #         self,
# #         text
# #     ):

# #         if not self.settings.get(
# #             "memory_enabled",
# #             True
# #         ):
# #             return None

# #         patterns = [

# #             r"^remember my (.+?) is (.+)$",

# #             r"^remember that my (.+?) is (.+)$",

# #             r"^my (.+?) is (.+)$"
# #         ]

# #         for pattern in patterns:

# #             match = re.match(
# #                 pattern,
# #                 text,
# #                 re.IGNORECASE
# #             )

# #             if not match:
# #                 continue

# #             key = match.group(
# #                 1
# #             ).strip()

# #             value = match.group(
# #                 2
# #             ).strip()

# #             if key in [
# #                 "name"
# #             ]:

# #                 continue

# #             self.memory.set_profile(
# #                 key,
# #                 value,
# #                 "Preferences"
# #             )

# #             return (
# #                 f"Okay, I'll remember that "
# #                 f"your {key} is {value}."
# #             )

# #         return None

# #     def recall_fact(
# #         self,
# #         text
# #     ):

# #         if not self.settings.get(
# #             "memory_enabled",
# #             True
# #         ):
# #             return None

# #         profile = (
# #             self.memory.get_profile_all()
# #         )

# #         if not profile:
# #             return None

# #         match = re.match(
# #             r"^(?:what is|what's|tell me) my (.+?)[?!.]*$",
# #             text,
# #             re.IGNORECASE
# #         )

# #         if match:

# #             key = match.group(
# #                 1
# #             ).strip()

# #             if key in profile:

# #                 value = self.memory.get_profile(
# #                     key
# #                 )

# #                 return (
# #                     f"Your {key} is {value}."
# #                 )

# #         return None

# #     def forget_fact(
# #         self,
# #         text
# #     ):

# #         if not self.settings.get(
# #             "memory_enabled",
# #             True
# #         ):
# #             return None

# #         match = re.match(
# #             r"^forget my (.+?)[?!.]*$",
# #             text,
# #             re.IGNORECASE
# #         )

# #         if not match:
# #             return None

# #         key = match.group(
# #             1
# #         ).strip()

# #         if self.memory.delete_profile(
# #             key
# #         ):

# #             return (
# #                 f"Okay. I forgot your {key}."
# #             )

# #         return (
# #             f"I don't have a saved memory "
# #             f"for your {key}."
# #         )

# #     def show_memories(self):

# #         if not self.settings.get(
# #             "memory_enabled",
# #             True
# #         ):

# #             return (
# #                 "Personal memory is disabled "
# #                 "in Settings."
# #             )

# #         profile = (
# #             self.memory.get_profile_all()
# #         )

# #         if not profile:

# #             return (
# #                 "I don't have any personal "
# #                 "memories saved."
# #             )

# #         lines = [
# #             "Things I remember:"
# #         ]

# #         for key, item in profile.items():

# #             if isinstance(
# #                 item,
# #                 dict
# #             ):

# #                 value = item.get(
# #                     "value",
# #                     ""
# #                 )

# #             else:

# #                 value = item

# #             lines.append(
# #                 f"• {key}: {value}"
# #             )

# #         return "\n".join(
# #             lines
# #         )

# #     # ==========================================================
# #     # NAME
# #     # ==========================================================

# #     def extract_name(
# #         self,
# #         text
# #     ):

# #         if not self.settings.get(
# #             "memory_enabled",
# #             True
# #         ):
# #             return None

# #         patterns = [

# #             r"\bmy name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",

# #             r"\bremember my name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",

# #             r"\bcall me ([a-zA-Z][a-zA-Z0-9 _-]{0,30})"
# #         ]

# #         for pattern in patterns:

# #             match = re.search(
# #                 pattern,
# #                 text,
# #                 re.IGNORECASE
# #             )

# #             if match:

# #                 name = match.group(
# #                     1
# #                 ).strip()

# #                 name = re.split(
# #                     r"\b(?:and|but|because|please)\b",
# #                     name,
# #                     flags=re.IGNORECASE
# #                 )[0].strip()

# #                 return name

# #         return None

# #     # ==========================================================
# #     # CALCULATOR
# #     # ==========================================================

# #     def calculate(
# #         self,
# #         text
# #     ):

# #         original = text

# #         text = re.sub(
# #             r"^(calculate|solve|compute)\s+",
# #             "",
# #             text,
# #             flags=re.IGNORECASE
# #         )

# #         text = re.sub(
# #             r"^what is\s+",
# #             "",
# #             text,
# #             flags=re.IGNORECASE
# #         )

# #         replacements = {

# #             "multiplied by": "*",
# #             "divided by": "/",
# #             "divide by": "/",
# #             "plus": "+",
# #             "minus": "-",
# #             "times": "*"
# #         }

# #         for word, symbol in replacements.items():

# #             text = text.replace(
# #                 word,
# #                 symbol
# #             )

# #         text = text.replace(
# #             "^",
# #             "**"
# #         )

# #         if not re.fullmatch(
# #             r"[0-9\s+\-*/().%]+",
# #             text
# #         ):

# #             return None

# #         try:

# #             tree = ast.parse(
# #                 text,
# #                 mode="eval"
# #             )

# #             result = self.safe_eval(
# #                 tree.body
# #             )

# #             if (
# #                 isinstance(
# #                     result,
# #                     float
# #                 )
# #                 and result.is_integer()
# #             ):

# #                 result = int(
# #                     result
# #                 )

# #             return (
# #                 f"The answer is {result}."
# #             )

# #         except Exception:

# #             if original.startswith(
# #                 (
# #                     "calculate",
# #                     "solve",
# #                     "compute"
# #                 )
# #             ):

# #                 return (
# #                     "I couldn't calculate that."
# #                 )

# #         return None

# #     def safe_eval(
# #         self,
# #         node
# #     ):

# #         operators = {

# #             ast.Add: operator.add,
# #             ast.Sub: operator.sub,
# #             ast.Mult: operator.mul,
# #             ast.Div: operator.truediv,
# #             ast.Mod: operator.mod,
# #             ast.Pow: operator.pow,

# #             ast.USub: operator.neg,
# #             ast.UAdd: operator.pos
# #         }

# #         if isinstance(
# #             node,
# #             ast.Constant
# #         ):

# #             if isinstance(
# #                 node.value,
# #                 (int, float)
# #             ):

# #                 return node.value

# #             raise ValueError

# #         if isinstance(
# #             node,
# #             ast.BinOp
# #         ):

# #             left = self.safe_eval(
# #                 node.left
# #             )

# #             right = self.safe_eval(
# #                 node.right
# #             )

# #             operation = operators.get(
# #                 type(node.op)
# #             )

# #             if operation is None:
# #                 raise ValueError

# #             return operation(
# #                 left,
# #                 right
# #             )

# #         if isinstance(
# #             node,
# #             ast.UnaryOp
# #         ):

# #             operation = operators.get(
# #                 type(node.op)
# #             )

# #             if operation is None:
# #                 raise ValueError

# #             return operation(
# #                 self.safe_eval(
# #                     node.operand
# #                 )
# #             )

# #         raise ValueError

# #     # ==========================================================
# #     # CONTEXT
# #     # ==========================================================

# #     def contextual_question(
# #         self,
# #         text
# #     ):

# #         if not self.settings.get(
# #             "context_enabled",
# #             True
# #         ):
# #             return None

# #         if not self.last_topic:
# #             return None

# #         topic = self.last_topic.lower()

# #         if text in [
# #             "who created it",
# #             "who made it",
# #             "who invented it"
# #         ]:

# #             if topic == "python":

# #                 return (
# #                     "Python was created by "
# #                     "Guido van Rossum."
# #                 )

# #         if text in [
# #             "what does it do",
# #             "what can it do"
# #         ]:

# #             if topic == "python":

# #                 return (
# #                     "Python is a general-purpose "
# #                     "programming language used for "
# #                     "automation, applications, web "
# #                     "development, data processing, "
# #                     "and many other tasks."
# #                 )

# #         if text in [
# #             "what is it",
# #             "tell me more"
# #         ]:

# #             answer, _, _ = (
# #                 self.search_knowledge(
# #                     f"what is {topic}"
# #                 )
# #             )

# #             return answer

# #         return None

# #     # ==========================================================
# #     # TOPIC
# #     # ==========================================================

# #     def detect_topic(
# #         self,
# #         text,
# #         category=None
# #     ):

# #         topics = [
# #             "python",
# #             "html",
# #             "css",
# #             "javascript",
# #             "database",
# #             "mysql",
# #             "sqlite",
# #             "sql",
# #             "computer",
# #             "cpu",
# #             "ram",
# #             "gpu",
# #             "cybersecurity",
# #             "encryption",
# #             "password",
# #             "tkinter",
# #             "pygame",
# #             "website",
# #             "api"
# #         ]

# #         for topic in topics:

# #             if topic in text:

# #                 return topic

# #         return category

# #     # ==========================================================
# #     # COMMANDS
# #     # ==========================================================

# #     def command(
# #         self,
# #         text
# #     ):

# #         if not text.startswith(
# #             "/"
# #         ):

# #             return None

# #         parts = text.split(
# #             maxsplit=1
# #         )

# #         command = parts[0].lower()

# #         argument = ""

# #         if len(parts) > 1:

# #             argument = parts[1].strip()

# #         # ------------------------------------------------------
# #         # HELP
# #         # ------------------------------------------------------

# #         if command == "/help":

# #             return self.help_text()

# #         # ------------------------------------------------------
# #         # TIME
# #         # ------------------------------------------------------

# #         if command == "/time":

# #             now = datetime.datetime.now()

# #             return (
# #                 "Current time: "
# #                 + now.strftime(
# #                     "%I:%M %p"
# #                 ).lstrip("0")
# #             )

# #         # ------------------------------------------------------
# #         # DATE
# #         # ------------------------------------------------------

# #         if command == "/date":

# #             now = datetime.datetime.now()

# #             return (
# #                 "Today is "
# #                 + now.strftime(
# #                     "%A, %d %B %Y"
# #                 )
# #                 + "."
# #             )

# #         # ------------------------------------------------------
# #         # MEMORY
# #         # ------------------------------------------------------

# #         if command == "/memory":

# #             return self.show_memories()

# #         # ------------------------------------------------------
# #         # KNOWLEDGE
# #         # ------------------------------------------------------

# #         if command == "/knowledge":

# #             count = len(
# #                 self.memory.get_knowledge()
# #             )

# #             return (
# #                 f"You have {count} "
# #                 f"custom knowledge entries."
# #             )

# #         # ------------------------------------------------------
# #         # STATS
# #         # ------------------------------------------------------

# #         if command == "/stats":

# #             return self.statistics_text()

# #         # ------------------------------------------------------
# #         # ABOUT
# #         # ------------------------------------------------------

# #         if command == "/about":

# #             return self.about_text()

# #         # ------------------------------------------------------
# #         # CLEAR
# #         # ------------------------------------------------------

# #         if command == "/clear":

# #             return "__CLEAR_CHAT__"

# #         # ------------------------------------------------------
# #         # SEARCH
# #         # ------------------------------------------------------

# #         if command == "/search":

# #             if not argument:

# #                 return (
# #                     "Usage:\n"
# #                     "/search keyword"
# #                 )

# #             results = (
# #                 self.memory.search_messages(
# #                     argument
# #                 )
# #             )

# #             if not results:

# #                 return (
# #                     "No matching messages found."
# #                 )

# #             lines = [
# #                 f"Found {len(results)} message(s):",
# #                 ""
# #             ]

# #             for item in results[-10:]:

# #                 role = item.get(
# #                     "role",
# #                     ""
# #                 )

# #                 content = item.get(
# #                     "content",
# #                     ""
# #                 )

# #                 label = (
# #                     "You"
# #                     if role == "user"
# #                     else "YuiBot"
# #                 )

# #                 lines.append(
# #                     f"{label}: {content}"
# #                 )

# #             return "\n".join(
# #                 lines
# #             )

# #         # ------------------------------------------------------
# #         # UNKNOWN
# #         # ------------------------------------------------------

# #         return (
# #             f"Unknown command: {command}\n\n"
# #             "Type /help to see available commands."
# #         )

# #     # ==========================================================
# #     # STATISTICS
# #     # ==========================================================

# #     def statistics_text(self):

# #         stats = (
# #             self.memory.get_statistics()
# #         )

# #         return (
# #             "YuiBot Statistics\n\n"
# #             f"User messages: "
# #             f"{stats['user_messages']}\n"
# #             f"Bot messages: "
# #             f"{stats['bot_messages']}\n"
# #             f"Sessions: "
# #             f"{stats['sessions']}\n"
# #             f"Custom knowledge: "
# #             f"{stats['knowledge_entries']}\n"
# #             f"Personal memories: "
# #             f"{stats['memories']}\n"
# #             f"Conversation messages: "
# #             f"{stats['conversation_messages']}"
# #         )

# #     # ==========================================================
# #     # HELP
# #     # ==========================================================

# #     def help_text(self):

# #         return """YuiBot v5 Commands

# # CHAT
# #   hello
# #   how are you?
# #   thanks
# #   bye

# # MEMORY
# #   my name is Alex
# #   remember my favorite color is blue
# #   what is my favorite color?
# #   forget my favorite color
# #   show my memories

# # KNOWLEDGE
# #   what is Python?
# #   what is HTML?
# #   what is a database?

# # TEACH
# #   teach: what is my favorite food = Pizza

# # CALCULATOR
# #   calculate 100 + 25
# #   calculate 20 * 5
# #   what is 100 divided by 4

# # COMMANDS
# #   /help
# #   /time
# #   /date
# #   /memory
# #   /knowledge
# #   /stats
# #   /search Python
# #   /about
# #   /clear

# # YuiBot is completely offline.
# # No AI model or external API is used."""

# #     # ==========================================================
# #     # ABOUT
# #     # ==========================================================

# #     def about_text(self):

# #         return (
# #             "YuiBot v5\n\n"
# #             "A Python rule-based chatbot.\n\n"
# #             "Features:\n"
# #             "• Memory\n"
# #             "• Knowledge\n"
# #             "• Context\n"
# #             "• Personality\n"
# #             "• Commands\n"
# #             "• Statistics\n"
# #             "• Fuzzy matching\n\n"
# #             "No AI model.\n"
# #             "No API.\n"
# #             "No internet."
# #         )

# #     # ==========================================================
# #     # MAIN RESPONSE
# #     # ==========================================================

# #     def respond(
# #         self,
# #         original_message
# #     ):

# #         if not original_message.strip():

# #             return "Please type something."

# #         text = self.normalize(
# #             original_message
# #         )

# #         self.last_question = text

# #         # ======================================================
# #         # COMMAND
# #         # ======================================================

# #         if text.startswith(
# #             "/"
# #         ):

# #             self.last_intent = "command"

# #             return self.command(
# #                 text
# #             )

# #         # ======================================================
# #         # TEACH
# #         # ======================================================

# #         if text.startswith(
# #             "teach:"
# #         ):

# #             content = original_message[
# #                 6:
# #             ].strip()

# #             if "=" not in content:

# #                 return (
# #                     "Teaching format:\n\n"
# #                     "teach: question = answer"
# #                 )

# #             question, answer = (
# #                 content.split(
# #                     "=",
# #                     1
# #                 )
# #             )

# #             question = self.normalize(
# #                 question.strip()
# #             )

# #             answer = answer.strip()

# #             if not question or not answer:

# #                 return (
# #                     "Question and answer "
# #                     "cannot be empty."
# #                 )

# #             self.memory.set_knowledge(
# #                 question,
# #                 answer,
# #                 "Custom"
# #             )

# #             self.last_intent = "teach"

# #             return (
# #                 "Knowledge learned successfully.\n\n"
# #                 f"Question: {question}\n"
# #                 f"Answer: {answer}"
# #             )

# #         # ======================================================
# #         # HELP
# #         # ======================================================

# #         if text in [
# #             "help",
# #             "help me",
# #             "commands"
# #         ]:

# #             return self.help_text()

# #         # ======================================================
# #         # MEMORY
# #         # ======================================================

# #         if text in [
# #             "show my memories",
# #             "show memories",
# #             "what do you remember",
# #             "what do you remember about me"
# #         ]:

# #             return self.show_memories()

# #         # ======================================================
# #         # NAME
# #         # ======================================================

# #         name = self.extract_name(
# #             original_message
# #         )

# #         if name:

# #             self.memory.set_profile(
# #                 "name",
# #                 name,
# #                 "Personal"
# #             )

# #             return (
# #                 f"Nice to meet you, {name}! "
# #                 "I'll remember your name."
# #             )

# #         if text in [
# #             "what is my name",
# #             "what's my name",
# #             "who am i",
# #             "do you remember my name"
# #         ]:

# #             name = self.memory.get_profile(
# #                 "name"
# #             )

# #             if name:

# #                 return (
# #                     f"Your name is {name}."
# #                 )

# #             return (
# #                 "You haven't told me your "
# #                 "name yet."
# #             )

# #         # ======================================================
# #         # FORGET
# #         # ======================================================

# #         if text in [
# #             "forget everything",
# #             "forget all",
# #             "clear knowledge"
# #         ]:

# #             self.memory.clear_knowledge()

# #             return (
# #                 "I cleared all custom knowledge."
# #             )

# #         if text in [
# #             "clear memories",
# #             "forget my memories"
# #         ]:

# #             self.memory.clear_profile()

# #             return (
# #                 "I cleared my personal memories."
# #             )

# #         forgotten = self.forget_fact(
# #             text
# #         )

# #         if forgotten:
# #             return forgotten

# #         remembered = self.remember_fact(
# #             text
# #         )

# #         if remembered:
# #             return remembered

# #         recalled = self.recall_fact(
# #             text
# #         )

# #         if recalled:
# #             return recalled

# #         # ======================================================
# #         # GREETING
# #         # ======================================================

# #         if text in [
# #             "hello",
# #             "hi",
# #             "hey",
# #             "good morning",
# #             "good afternoon",
# #             "good evening"
# #         ]:

# #             self.last_intent = "greeting"

# #             return self.personality(
# #                 "greeting"
# #             )

# #         # ======================================================
# #         # HOW ARE YOU
# #         # ======================================================

# #         if (
# #             "how are you" in text
# #             or "how do you feel" in text
# #         ):

# #             self.last_intent = (
# #                 "how_are_you"
# #             )

# #             mode = self.settings.get(
# #                 "personality",
# #                 "Friendly"
# #             )

# #             if mode == "Short":

# #                 return "I'm good!"

# #             if mode == "Professional":

# #                 return (
# #                     "I'm operating normally "
# #                     "and ready to assist."
# #                 )

# #             if mode == "Casual":

# #                 return "I'm good! Ready to chat."

# #             return "I'm doing well! Ready to chat."

# #         # ======================================================
# #         # THANKS
# #         # ======================================================

# #         if text in [
# #             "thanks",
# #             "thank you",
# #             "thx"
# #         ]:

# #             return self.personality(
# #                 "thanks"
# #             )

# #         # ======================================================
# #         # GOODBYE
# #         # ======================================================

# #         if (
# #             text in [
# #                 "bye",
# #                 "goodbye",
# #                 "good night"
# #             ]
# #             or "see you" in text
# #         ):

# #             return self.personality(
# #                 "goodbye"
# #             )

# #         # ======================================================
# #         # POSITIVE
# #         # ======================================================

# #         if text in [
# #             "good",
# #             "great",
# #             "awesome",
# #             "nice",
# #             "fine",
# #             "okay",
# #             "ok"
# #         ]:

# #             if self.last_intent == "how_are_you":

# #                 return "Glad to hear it!"

# #             return "Nice!"

# #         # ======================================================
# #         # TIME
# #         # ======================================================

# #         if (
# #             "what time" in text
# #             or "current time" in text
# #             or text == "time"
# #             or "tell me the time" in text
# #         ):

# #             now = datetime.datetime.now()

# #             return (
# #                 "The current time is "
# #                 + now.strftime(
# #                     "%I:%M %p"
# #                 ).lstrip("0")
# #                 + "."
# #             )

# #         # ======================================================
# #         # DATE
# #         # ======================================================

# #         if (
# #             "what date" in text
# #             or "today's date" in text
# #             or "todays date" in text
# #             or text == "date"
# #             or "what day is it" in text
# #         ):

# #             now = datetime.datetime.now()

# #             return (
# #                 "Today is "
# #                 + now.strftime(
# #                     "%A, %d %B %Y"
# #                 )
# #                 + "."
# #             )

# #         # ======================================================
# #         # CALCULATOR
# #         # ======================================================

# #         calculation = self.calculate(
# #             text
# #         )

# #         if calculation:
# #             return calculation

# #         # ======================================================
# #         # CONTEXT
# #         # ======================================================

# #         contextual = (
# #             self.contextual_question(
# #                 text
# #             )
# #         )

# #         if contextual:

# #             self.last_intent = "context"

# #             return contextual

# #         # ======================================================
# #         # KNOWLEDGE
# #         # ======================================================

# #         answer, score, category = (
# #             self.search_knowledge(
# #                 text
# #             )
# #         )

# #         if answer:

# #             self.last_intent = "knowledge"

# #             self.last_topic = (
# #                 self.detect_topic(
# #                     text,
# #                     category
# #                 )
# #             )

# #             return answer

# #         # ======================================================
# #         # UNKNOWN
# #         # ======================================================

# #         self.last_intent = "unknown"

# #         return (
# #             "I'm not sure how to answer that yet.\n\n"
# #             "You can teach me with:\n"
# #             "teach: question = answer\n\n"
# #             "Or type /help to see my commands."
# #         )



# import ast
# import datetime
# import difflib
# import operator
# import random
# import re

# from memory import ChatMemory
# from settings import Settings
# from knowledge import BUILT_IN_KNOWLEDGE
# from rules import RuleStore


# class YuiBot:
#     def __init__(self):
#         self.memory = ChatMemory()
#         self.settings = Settings()

#         # The rule engine is persistent in data/rules.json.
#         self.rule_store = RuleStore(self.memory)
#         # Compatibility with the existing main.py close() and Rule Manager.
#         self.rules = self.rule_store

#         self.last_intent = None
#         self.last_topic = None
#         self.last_question = None

#         self.memory.new_session()

#         self.responses = {
#             "Friendly": {
#                 "greeting": ["Hello!", "Hi!", "Hey!", "Hello! How can I help?"],
#                 "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
#                 "goodbye": ["Goodbye!", "See you later!", "Bye!"],
#             },
#             "Professional": {
#                 "greeting": [
#                     "Hello. How may I assist you?",
#                     "Hello. What would you like to know?",
#                     "Good day. How can I help?",
#                 ],
#                 "thanks": ["You're welcome.", "You're welcome. I'm glad I could help."],
#                 "goodbye": ["Goodbye.", "Have a good day.", "Until next time."],
#             },
#             "Short": {
#                 "greeting": ["Hi!", "Hello!", "Hey!"],
#                 "thanks": ["You're welcome.", "No problem."],
#                 "goodbye": ["Bye!", "See you!"],
#             },
#             "Casual": {
#                 "greeting": ["Hey!", "Yo!", "Hi there!"],
#                 "thanks": ["No worries!", "Anytime!", "Sure thing!"],
#                 "goodbye": ["Later!", "Bye!", "See ya!"],
#             },
#         }

#         self.typos = {
#             "helo": "hello", "helllo": "hello", "hllo": "hello",
#             "hii": "hi", "hiiii": "hi", "heyy": "hey",
#             "wht": "what", "whatt": "what", "wat": "what", "wut": "what",
#             "whos": "who is", "whats": "what is",
#             "ur": "your", "u": "you", "r": "are",
#             "pls": "please", "plz": "please", "thx": "thanks",
#             "im": "i am", "idk": "i do not know",
#             "tim": "time", "todai": "today",
#             "calcluate": "calculate", "calculte": "calculate",
#             "favrite": "favorite", "favouritee": "favorite",
#             "pyhton": "python", "pythn": "python",
#             "databse": "database", "javscript": "javascript",
#         }

#     # ==========================================================
#     # SETTINGS / PERSONALITY
#     # ==========================================================

#     def reload_settings(self):
#         self.settings.load()

#     def personality(self, category):
#         mode = self.settings.get("personality", "Friendly")
#         group = self.responses.get(mode, self.responses["Friendly"])
#         values = group.get(category, [])
#         return random.choice(values) if values else ""

#     # ==========================================================
#     # NORMALIZATION / SIMILARITY
#     # ==========================================================

#     def normalize(self, text):
#         text = text.lower().strip()
#         text = re.sub(r"\s+", " ", text)
#         fixed = []

#         for word in text.split():
#             punctuation = ""
#             while word and word[-1] in ".,!?":
#                 punctuation = word[-1] + punctuation
#                 word = word[:-1]
#             word = self.typos.get(word, word)
#             fixed.append(word + punctuation)

#         text = " ".join(fixed)
#         text = re.sub(r"\bwhat's\b", "what is", text)
#         text = re.sub(r"\bwho's\b", "who is", text)
#         return text

#     def similarity(self, a, b):
#         if not self.settings.get("fuzzy_matching", True):
#             return 1.0 if a == b else 0.0

#         a = a.lower().strip()
#         b = b.lower().strip()

#         if a == b:
#             return 1.0
#         if a in b or b in a:
#             return 0.92

#         ratio = difflib.SequenceMatcher(None, a, b).ratio()
#         a_words = set(re.findall(r"\b\w+\b", a))
#         b_words = set(re.findall(r"\b\w+\b", b))
#         overlap = (
#             len(a_words & b_words) / max(len(a_words), len(b_words))
#             if a_words and b_words else 0
#         )
#         return max(ratio, overlap)

#     # ==========================================================
#     # RULE ENGINE
#     # ==========================================================

#     def match_rule(self, text):
#         """Return a random response from the best enabled matching rule."""
#         normalized = self.normalize(text).strip(" .!?")
#         if not normalized:
#             return None

#         best_rule = None
#         best_score = 0.0

#         for rule in self.rule_store.get_enabled():
#             triggers = rule.get("triggers", [])
#             responses = rule.get("responses", [])
#             if not triggers or not responses:
#                 continue

#             for raw_trigger in triggers:
#                 trigger = self.normalize(str(raw_trigger)).strip(" .!?")
#                 if not trigger:
#                     continue

#                 if normalized == trigger:
#                     score = 1.0
#                 elif re.search(
#                     r"(?<!\w)" + re.escape(trigger) + r"(?!\w)",
#                     normalized
#                 ):
#                     score = 0.93
#                 else:
#                     score = self.similarity(normalized, trigger)

#                 if score > best_score:
#                     best_score = score
#                     best_rule = rule

#         if best_rule and best_score >= 0.72:
#             choices = best_rule.get("responses", [])
#             if choices:
#                 self.last_intent = best_rule.get("intent", "rule")
#                 return random.choice(choices)

#         return None

#     # ==========================================================
#     # KNOWLEDGE
#     # ==========================================================

#     def search_knowledge(self, question):
#         question = self.normalize(question)
#         all_knowledge = {
#             key: {"answer": value, "category": "Built-in"}
#             for key, value in BUILT_IN_KNOWLEDGE.items()
#         }
#         all_knowledge.update(self.memory.get_knowledge())

#         if question in all_knowledge:
#             item = all_knowledge[question]
#             return item["answer"], 1.0, item.get("category", "General")

#         best = None
#         best_score = 0.0
#         for key, item in all_knowledge.items():
#             score = self.similarity(question, key)
#             if score > best_score:
#                 best_score = score
#                 best = item

#         if best is not None and best_score >= 0.58:
#             return best["answer"], best_score, best.get("category", "General")
#         return None, 0, None

#     # ==========================================================
#     # PERSONAL MEMORY
#     # ==========================================================

#     def remember_fact(self, text):
#         if not self.settings.get("memory_enabled", True):
#             return None

#         patterns = [
#             r"^remember my (.+?) is (.+)$",
#             r"^remember that my (.+?) is (.+)$",
#             r"^my (.+?) is (.+)$",
#         ]

#         for pattern in patterns:
#             match = re.match(pattern, text, re.IGNORECASE)
#             if not match:
#                 continue

#             key = match.group(1).strip()
#             value = match.group(2).strip()
#             if key == "name":
#                 continue

#             self.memory.set_profile(key, value, "Preferences")
#             return f"Okay, I'll remember that your {key} is {value}."
#         return None

#     def recall_fact(self, text):
#         if not self.settings.get("memory_enabled", True):
#             return None

#         profile = self.memory.get_profile_all()
#         if not profile:
#             return None

#         match = re.match(
#             r"^(?:what is|what's|tell me) my (.+?)[?!.]*$",
#             text,
#             re.IGNORECASE,
#         )
#         if match:
#             key = match.group(1).strip()
#             if key in profile:
#                 value = self.memory.get_profile(key)
#                 return f"Your {key} is {value}."
#         return None

#     def forget_fact(self, text):
#         if not self.settings.get("memory_enabled", True):
#             return None

#         match = re.match(r"^forget my (.+?)[?!.]*$", text, re.IGNORECASE)
#         if not match:
#             return None

#         key = match.group(1).strip()
#         if self.memory.delete_profile(key):
#             return f"Okay. I forgot your {key}."
#         return f"I don't have a saved memory for your {key}."

#     def show_memories(self):
#         if not self.settings.get("memory_enabled", True):
#             return "Personal memory is disabled in Settings."

#         profile = self.memory.get_profile_all()
#         if not profile:
#             return "I don't have any personal memories saved."

#         lines = ["Things I remember:"]
#         for key, item in profile.items():
#             value = item.get("value", "") if isinstance(item, dict) else item
#             lines.append(f"• {key}: {value}")
#         return "\n".join(lines)

#     def extract_name(self, text):
#         if not self.settings.get("memory_enabled", True):
#             return None

#         patterns = [
#             r"\bmy name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
#             r"\bremember my name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
#             r"\bcall me ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
#         ]
#         for pattern in patterns:
#             match = re.search(pattern, text, re.IGNORECASE)
#             if match:
#                 name = match.group(1).strip()
#                 name = re.split(
#                     r"\b(?:and|but|because|please)\b",
#                     name,
#                     flags=re.IGNORECASE,
#                 )[0].strip()
#                 return name
#         return None

#     # ==========================================================
#     # CALCULATOR
#     # ==========================================================

#     def calculate(self, text):
#         original = text
#         text = re.sub(r"^(calculate|solve|compute)\s+", "", text, flags=re.IGNORECASE)
#         text = re.sub(r"^what is\s+", "", text, flags=re.IGNORECASE)

#         replacements = {
#             "multiplied by": "*",
#             "divided by": "/",
#             "divide by": "/",
#             "plus": "+",
#             "minus": "-",
#             "times": "*",
#         }
#         for word, symbol in replacements.items():
#             text = text.replace(word, symbol)
#         text = text.replace("^", "**")

#         if not re.fullmatch(r"[0-9\s+\-*/().%]+", text):
#             return None

#         try:
#             tree = ast.parse(text, mode="eval")
#             result = self.safe_eval(tree.body)
#             if isinstance(result, float) and result.is_integer():
#                 result = int(result)
#             return f"The answer is {result}."
#         except Exception:
#             if original.startswith(("calculate", "solve", "compute")):
#                 return "I couldn't calculate that."
#         return None

#     def safe_eval(self, node):
#         operators = {
#             ast.Add: operator.add,
#             ast.Sub: operator.sub,
#             ast.Mult: operator.mul,
#             ast.Div: operator.truediv,
#             ast.Mod: operator.mod,
#             ast.Pow: operator.pow,
#             ast.USub: operator.neg,
#             ast.UAdd: operator.pos,
#         }

#         if isinstance(node, ast.Constant):
#             if isinstance(node.value, (int, float)):
#                 return node.value
#             raise ValueError("Unsupported value")

#         if isinstance(node, ast.BinOp):
#             left = self.safe_eval(node.left)
#             right = self.safe_eval(node.right)
#             operation = operators.get(type(node.op))
#             if operation is None:
#                 raise ValueError("Unsupported operator")
#             # Avoid pathological exponentiation / huge values.
#             if isinstance(node.op, ast.Pow) and abs(right) > 100:
#                 raise ValueError("Exponent too large")
#             result = operation(left, right)
#             if isinstance(result, (int, float)) and abs(result) > 1e100:
#                 raise ValueError("Result too large")
#             return result

#         if isinstance(node, ast.UnaryOp):
#             operation = operators.get(type(node.op))
#             if operation is None:
#                 raise ValueError("Unsupported unary operator")
#             return operation(self.safe_eval(node.operand))

#         raise ValueError("Unsupported expression")

#     # ==========================================================
#     # CONTEXT / TOPIC
#     # ==========================================================

#     def contextual_question(self, text):
#         if not self.settings.get("context_enabled", True) or not self.last_topic:
#             return None

#         topic = self.last_topic.lower()

#         if text in ("who created it", "who made it", "who invented it"):
#             if topic == "python":
#                 return "Python was created by Guido van Rossum."

#         if text in ("what does it do", "what can it do"):
#             if topic == "python":
#                 return (
#                     "Python is a general-purpose programming language used for "
#                     "automation, applications, web development, data processing, "
#                     "and many other tasks."
#                 )

#         if text in ("what is it", "tell me more"):
#             answer, _, _ = self.search_knowledge(f"what is {topic}")
#             return answer
#         return None

#     def detect_topic(self, text, category=None):
#         topics = [
#             "python", "html", "css", "javascript", "database", "mysql",
#             "sqlite", "sql", "computer", "cpu", "ram", "gpu",
#             "cybersecurity", "encryption", "password", "tkinter",
#             "pygame", "website", "api",
#         ]
#         for topic in topics:
#             if topic in text:
#                 return topic
#         return category

#     # ==========================================================
#     # COMMANDS
#     # ==========================================================

#     def command(self, text):
#         if not text.startswith("/"):
#             return None

#         parts = text.split(maxsplit=1)
#         command = parts[0].lower()
#         argument = parts[1].strip() if len(parts) > 1 else ""

#         if command == "/help":
#             return self.help_text()

#         if command == "/time":
#             now = datetime.datetime.now()
#             return "Current time: " + now.strftime("%I:%M %p").lstrip("0")

#         if command == "/date":
#             now = datetime.datetime.now()
#             return "Today is " + now.strftime("%A, %d %B %Y") + "."

#         if command == "/memory":
#             return self.show_memories()

#         if command == "/knowledge":
#             count = len(self.memory.get_knowledge())
#             return f"You have {count} custom knowledge entries."

#         if command == "/stats":
#             return self.statistics_text()

#         if command == "/about":
#             return self.about_text()

#         if command == "/clear":
#             return "__CLEAR_CHAT__"

#         if command == "/search":
#             if not argument:
#                 return "Usage:\n/search keyword"

#             results = self.memory.search_messages(argument)
#             if not results:
#                 return "No matching messages found."

#             lines = [f"Found {len(results)} message(s):", ""]
#             for item in results[-10:]:
#                 role = item.get("role", "")
#                 content = item.get("content", "")
#                 label = "You" if role == "user" else "YuiBot"
#                 lines.append(f"{label}: {content}")
#             return "\n".join(lines)

#         if command == "/rules":
#             enabled = self.rule_store.get_enabled()
#             lines = [f"Rules: {len(self.rule_store.get_all())} total, {len(enabled)} enabled."]
#             for rule in enabled[:20]:
#                 lines.append(f"• {rule.get('intent', 'Unnamed')} — {', '.join(rule.get('triggers', []))}")
#             return "\n".join(lines)

#         return (
#             f"Unknown command: {command}\n\n"
#             "Type /help to see available commands."
#         )

#     def statistics_text(self):
#         stats = self.memory.get_statistics()
#         return (
#             "YuiBot Statistics\n\n"
#             f"User messages: {stats.get('user_messages', 0)}\n"
#             f"Bot messages: {stats.get('bot_messages', 0)}\n"
#             f"Sessions: {stats.get('sessions', 0)}\n"
#             f"Custom knowledge: {stats.get('knowledge_entries', 0)}\n"
#             f"Personal memories: {stats.get('memories', 0)}\n"
#             f"Conversation messages: {stats.get('conversation_messages', 0)}\n"
#             f"Rules: {len(self.rule_store.get_all())}"
#         )

#     def help_text(self):
#         return """YuiBot v5 Commands

# CHAT
#   hello
#   how are you?
#   thanks
#   bye

# MEMORY
#   my name is Alex
#   remember my favorite color is blue
#   what is my favorite color?
#   forget my favorite color
#   show my memories

# KNOWLEDGE
#   what is Python?
#   what is HTML?
#   what is a database?

# TEACH
#   teach: what is my favorite food = Pizza

# CALCULATOR
#   calculate 100 + 25
#   calculate 20 * 5
#   what is 100 divided by 4

# COMMANDS
#   /help
#   /time
#   /date
#   /memory
#   /knowledge
#   /stats
#   /search Python
#   /rules
#   /about
#   /clear

# YuiBot is completely offline.
# No AI model or external API is used."""

#     def about_text(self):
#         return (
#             "YuiBot v5\n\n"
#             "A Python rule-based chatbot.\n\n"
#             "Features:\n"
#             "• Memory\n• Knowledge\n• Context\n• Personality\n"
#             "• Custom rules\n• Commands\n• Statistics\n• Fuzzy matching\n\n"
#             "No AI model.\nNo API.\nNo internet."
#         )

#     # ==========================================================
#     # MAIN RESPONSE
#     # ==========================================================

#     def respond(self, original_message):
#         if not original_message.strip():
#             return "Please type something."

#         text = self.normalize(original_message)
#         self.last_question = text

#         # Commands have priority over chat rules.
#         if text.startswith("/"):
#             self.last_intent = "command"
#             return self.command(text)

#         # Teaching is a dedicated command and should not be intercepted by rules.
#         if text.startswith("teach:"):
#             content = original_message[6:].strip()
#             if "=" not in content:
#                 return "Teaching format:\n\nteach: question = answer"

#             question, answer = content.split("=", 1)
#             question = self.normalize(question.strip())
#             answer = answer.strip()

#             if not question or not answer:
#                 return "Question and answer cannot be empty."

#             self.memory.set_knowledge(question, answer, "Custom")
#             self.last_intent = "teach"
#             return (
#                 "Knowledge learned successfully.\n\n"
#                 f"Question: {question}\n"
#                 f"Answer: {answer}"
#             )

#         if text in ("help", "help me", "commands"):
#             return self.help_text()

#         if text in (
#             "show my memories", "show memories", "what do you remember",
#             "what do you remember about me",
#         ):
#             return self.show_memories()

#         name = self.extract_name(original_message)
#         if name:
#             self.memory.set_profile("name", name, "Personal")
#             return f"Nice to meet you, {name}! I'll remember your name."

#         if text in ("what is my name", "what's my name", "who am i", "do you remember my name"):
#             name = self.memory.get_profile("name")
#             return f"Your name is {name}." if name else "You haven't told me your name yet."

#         if text in ("forget everything", "forget all", "clear knowledge"):
#             self.memory.clear_knowledge()
#             return "I cleared all custom knowledge."

#         if text in ("clear memories", "forget my memories"):
#             self.memory.clear_profile()
#             return "I cleared my personal memories."

#         forgotten = self.forget_fact(text)
#         if forgotten:
#             return forgotten

#         remembered = self.remember_fact(text)
#         if remembered:
#             return remembered

#         recalled = self.recall_fact(text)
#         if recalled:
#             return recalled

#         # Keep the explicit built-in greeting/personality behaviour.
#         if text in ("hello", "hi", "hey", "good morning", "good afternoon", "good evening"):
#             self.last_intent = "greeting"
#             return self.personality("greeting")

#         if "how are you" in text or "how do you feel" in text:
#             self.last_intent = "how_are_you"
#             mode = self.settings.get("personality", "Friendly")
#             if mode == "Short":
#                 return "I'm good!"
#             if mode == "Professional":
#                 return "I'm operating normally and ready to assist."
#             if mode == "Casual":
#                 return "I'm good! Ready to chat."
#             return "I'm doing well! Ready to chat."

#         if text in ("thanks", "thank you", "thx"):
#             return self.personality("thanks")

#         if text in ("bye", "goodbye", "good night") or "see you" in text:
#             return self.personality("goodbye")

#         if text in ("good", "great", "awesome", "nice", "fine", "okay", "ok"):
#             if self.last_intent == "how_are_you":
#                 return "Glad to hear it!"
#             return "Nice!"

#         if (
#             "what time" in text or "current time" in text or
#             text == "time" or "tell me the time" in text
#         ):
#             now = datetime.datetime.now()
#             return "The current time is " + now.strftime("%I:%M %p").lstrip("0") + "."

#         if (
#             "what date" in text or "today's date" in text or
#             "todays date" in text or text == "date" or "what day is it" in text
#         ):
#             now = datetime.datetime.now()
#             return "Today is " + now.strftime("%A, %d %B %Y") + "."

#         calculation = self.calculate(text)
#         if calculation:
#             return calculation

#         contextual = self.contextual_question(text)
#         if contextual:
#             self.last_intent = "context"
#             return contextual

#         # Try custom rules before the knowledge fallback.
#         rule_response = self.match_rule(text)
#         if rule_response is not None:
#             return rule_response

#         answer, score, category = self.search_knowledge(text)
#         if answer:
#             self.last_intent = "knowledge"
#             self.last_topic = self.detect_topic(text, category)
#             return answer

#         self.last_intent = "unknown"
#         return (
#             "I'm not sure how to answer that yet.\n\n"
#             "You can teach me with:\n"
#             "teach: question = answer\n\n"
#             "Or type /help to see my commands."
#         )


import ast
import datetime
import difflib
import operator
import random
import re

from memory import ChatMemory
from settings import Settings
from knowledge import BUILT_IN_KNOWLEDGE, KnowledgeStore
from rules import RuleStore


class YuiBot:
    def __init__(self):
        self.memory = ChatMemory()
        self.settings = Settings()
        # Persistent offline knowledge, separate from personal conversation memory.
        self.knowledge = KnowledgeStore()
        self.knowledge_store = self.knowledge
        self.last_unknown_question = None

        # The rule engine is persistent in data/rules.json.
        self.rule_store = RuleStore(self.memory)
        # Compatibility with the existing main.py close() and Rule Manager.
        self.rules = self.rule_store

        self.last_intent = None
        self.last_topic = None
        self.last_question = None

        self.memory.new_session()

        self.responses = {
            "Friendly": {
                "greeting": ["Hello!", "Hi!", "Hey!", "Hello! How can I help?"],
                "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
                "goodbye": ["Goodbye!", "See you later!", "Bye!"],
            },
            "Professional": {
                "greeting": [
                    "Hello. How may I assist you?",
                    "Hello. What would you like to know?",
                    "Good day. How can I help?",
                ],
                "thanks": ["You're welcome.", "You're welcome. I'm glad I could help."],
                "goodbye": ["Goodbye.", "Have a good day.", "Until next time."],
            },
            "Short": {
                "greeting": ["Hi!", "Hello!", "Hey!"],
                "thanks": ["You're welcome.", "No problem."],
                "goodbye": ["Bye!", "See you!"],
            },
            "Casual": {
                "greeting": ["Hey!", "Yo!", "Hi there!"],
                "thanks": ["No worries!", "Anytime!", "Sure thing!"],
                "goodbye": ["Later!", "Bye!", "See ya!"],
            },
        }

        self.typos = {
            "helo": "hello", "helllo": "hello", "hllo": "hello",
            "hii": "hi", "hiiii": "hi", "heyy": "hey",
            "wht": "what", "whatt": "what", "wat": "what", "wut": "what",
            "whos": "who is", "whats": "what is",
            "ur": "your", "u": "you", "r": "are",
            "pls": "please", "plz": "please", "thx": "thanks",
            "im": "i am", "idk": "i do not know",
            "tim": "time", "todai": "today",
            "calcluate": "calculate", "calculte": "calculate",
            "favrite": "favorite", "favouritee": "favorite",
            "pyhton": "python", "pythn": "python",
            "databse": "database", "javscript": "javascript",
        }

    # ==========================================================
    # SETTINGS / PERSONALITY
    # ==========================================================

    def reload_settings(self):
        self.settings.load()

    def personality(self, category):
        mode = self.settings.get("personality", "Friendly")
        group = self.responses.get(mode, self.responses["Friendly"])
        values = group.get(category, [])
        return random.choice(values) if values else ""

    # ==========================================================
    # NORMALIZATION / SIMILARITY
    # ==========================================================

    def normalize(self, text):
        text = text.lower().strip()
        text = re.sub(r"\s+", " ", text)
        fixed = []

        for word in text.split():
            punctuation = ""
            while word and word[-1] in ".,!?":
                punctuation = word[-1] + punctuation
                word = word[:-1]
            word = self.typos.get(word, word)
            fixed.append(word + punctuation)

        text = " ".join(fixed)
        text = re.sub(r"\bwhat's\b", "what is", text)
        text = re.sub(r"\bwho's\b", "who is", text)
        return text

    def similarity(self, a, b):
        if not self.settings.get("fuzzy_matching", True):
            return 1.0 if a == b else 0.0

        a = a.lower().strip()
        b = b.lower().strip()

        if a == b:
            return 1.0
        if a in b or b in a:
            return 0.92

        ratio = difflib.SequenceMatcher(None, a, b).ratio()
        a_words = set(re.findall(r"\b\w+\b", a))
        b_words = set(re.findall(r"\b\w+\b", b))
        overlap = (
            len(a_words & b_words) / max(len(a_words), len(b_words))
            if a_words and b_words else 0
        )
        return max(ratio, overlap)

    # ==========================================================
    # RULE ENGINE
    # ==========================================================

    def match_rule(self, text):
        """Return a random response from the best enabled matching rule."""
        normalized = self.normalize(text).strip(" .!?")
        if not normalized:
            return None

        best_rule = None
        best_score = 0.0

        for rule in self.rule_store.get_enabled():
            triggers = rule.get("triggers", [])
            responses = rule.get("responses", [])
            if not triggers or not responses:
                continue

            for raw_trigger in triggers:
                trigger = self.normalize(str(raw_trigger)).strip(" .!?")
                if not trigger:
                    continue

                if normalized == trigger:
                    score = 1.0
                elif re.search(
                    r"(?<!\w)" + re.escape(trigger) + r"(?!\w)",
                    normalized
                ):
                    score = 0.93
                else:
                    score = self.similarity(normalized, trigger)

                if score > best_score:
                    best_score = score
                    best_rule = rule

        if best_rule and best_score >= 0.72:
            choices = best_rule.get("responses", [])
            if choices:
                self.last_intent = best_rule.get("intent", "rule")
                return random.choice(choices)

        return None

    # ==========================================================
    # KNOWLEDGE
    # ==========================================================

    def search_knowledge(self, question):
        question = self.normalize(question)
        all_knowledge = {
            key: {"answer": value, "category": "Built-in"}
            for key, value in BUILT_IN_KNOWLEDGE.items()
        }
        for item in self.knowledge.get_all():
            key = self.normalize(item["question"])
            all_knowledge[key] = {
                "answer": item["answer"],
                "category": item.get("category", "General"),
                "source": item.get("source", "Manual"),
            }

        if question in all_knowledge:
            item = all_knowledge[question]
            return item["answer"], 1.0, item.get("category", "General")

        best = None
        best_score = 0.0
        for key, item in all_knowledge.items():
            score = self.similarity(question, key)
            if score > best_score:
                best_score = score
                best = item

        if best is not None and best_score >= 0.58:
            return best["answer"], best_score, best.get("category", "General")
        return None, 0, None

    # ==========================================================
    # PERSONAL MEMORY
    # ==========================================================

    def remember_fact(self, text):
        if not self.settings.get("memory_enabled", True):
            return None

        patterns = [
            r"^remember my (.+?) is (.+)$",
            r"^remember that my (.+?) is (.+)$",
            r"^my (.+?) is (.+)$",
        ]

        for pattern in patterns:
            match = re.match(pattern, text, re.IGNORECASE)
            if not match:
                continue

            key = match.group(1).strip()
            value = match.group(2).strip()
            if key == "name":
                continue

            self.memory.set_profile(key, value, "Preferences")
            return f"Okay, I'll remember that your {key} is {value}."
        return None

    def recall_fact(self, text):
        if not self.settings.get("memory_enabled", True):
            return None

        profile = self.memory.get_profile_all()
        if not profile:
            return None

        match = re.match(
            r"^(?:what is|what's|tell me) my (.+?)[?!.]*$",
            text,
            re.IGNORECASE,
        )
        if match:
            key = match.group(1).strip()
            if key in profile:
                value = self.memory.get_profile(key)
                return f"Your {key} is {value}."
        return None

    def forget_fact(self, text):
        if not self.settings.get("memory_enabled", True):
            return None

        match = re.match(r"^forget my (.+?)[?!.]*$", text, re.IGNORECASE)
        if not match:
            return None

        key = match.group(1).strip()
        if self.memory.delete_profile(key):
            return f"Okay. I forgot your {key}."
        return f"I don't have a saved memory for your {key}."

    def show_memories(self):
        if not self.settings.get("memory_enabled", True):
            return "Personal memory is disabled in Settings."

        profile = self.memory.get_profile_all()
        if not profile:
            return "I don't have any personal memories saved."

        lines = ["Things I remember:"]
        for key, item in profile.items():
            value = item.get("value", "") if isinstance(item, dict) else item
            lines.append(f"• {key}: {value}")
        return "\n".join(lines)

    def extract_name(self, text):
        if not self.settings.get("memory_enabled", True):
            return None

        patterns = [
            r"\bmy name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
            r"\bremember my name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
            r"\bcall me ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                name = match.group(1).strip()
                name = re.split(
                    r"\b(?:and|but|because|please)\b",
                    name,
                    flags=re.IGNORECASE,
                )[0].strip()
                return name
        return None

    # ==========================================================
    # CALCULATOR
    # ==========================================================

    def calculate(self, text):
        original = text
        text = re.sub(r"^(calculate|solve|compute)\s+", "", text, flags=re.IGNORECASE)
        text = re.sub(r"^what is\s+", "", text, flags=re.IGNORECASE)

        replacements = {
            "multiplied by": "*",
            "divided by": "/",
            "divide by": "/",
            "plus": "+",
            "minus": "-",
            "times": "*",
        }
        for word, symbol in replacements.items():
            text = text.replace(word, symbol)
        text = text.replace("^", "**")

        if not re.fullmatch(r"[0-9\s+\-*/().%]+", text):
            return None

        try:
            tree = ast.parse(text, mode="eval")
            result = self.safe_eval(tree.body)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return f"The answer is {result}."
        except Exception:
            if original.startswith(("calculate", "solve", "compute")):
                return "I couldn't calculate that."
        return None

    def safe_eval(self, node):
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Unsupported value")

        if isinstance(node, ast.BinOp):
            left = self.safe_eval(node.left)
            right = self.safe_eval(node.right)
            operation = operators.get(type(node.op))
            if operation is None:
                raise ValueError("Unsupported operator")
            # Avoid pathological exponentiation / huge values.
            if isinstance(node.op, ast.Pow) and abs(right) > 100:
                raise ValueError("Exponent too large")
            result = operation(left, right)
            if isinstance(result, (int, float)) and abs(result) > 1e100:
                raise ValueError("Result too large")
            return result

        if isinstance(node, ast.UnaryOp):
            operation = operators.get(type(node.op))
            if operation is None:
                raise ValueError("Unsupported unary operator")
            return operation(self.safe_eval(node.operand))

        raise ValueError("Unsupported expression")

    # ==========================================================
    # CONTEXT / TOPIC
    # ==========================================================

    def contextual_question(self, text):
        if not self.settings.get("context_enabled", True) or not self.last_topic:
            return None

        topic = self.last_topic.lower()

        if text in ("who created it", "who made it", "who invented it"):
            if topic == "python":
                return "Python was created by Guido van Rossum."

        if text in ("what does it do", "what can it do"):
            if topic == "python":
                return (
                    "Python is a general-purpose programming language used for "
                    "automation, applications, web development, data processing, "
                    "and many other tasks."
                )

        if text in ("what is it", "tell me more"):
            answer, _, _ = self.search_knowledge(f"what is {topic}")
            return answer
        return None

    def detect_topic(self, text, category=None):
        topics = [
            "python", "html", "css", "javascript", "database", "mysql",
            "sqlite", "sql", "computer", "cpu", "ram", "gpu",
            "cybersecurity", "encryption", "password", "tkinter",
            "pygame", "website", "api",
        ]
        for topic in topics:
            if topic in text:
                return topic
        return category

    # ==========================================================
    # COMMANDS
    # ==========================================================

    def command(self, text):
        if not text.startswith("/"):
            return None

        parts = text.split(maxsplit=1)
        command = parts[0].lower()
        argument = parts[1].strip() if len(parts) > 1 else ""

        if command == "/help":
            return self.help_text()

        if command == "/time":
            now = datetime.datetime.now()
            return "Current time: " + now.strftime("%I:%M %p").lstrip("0")

        if command == "/date":
            now = datetime.datetime.now()
            return "Today is " + now.strftime("%A, %d %B %Y") + "."

        if command == "/memory":
            return self.show_memories()

        if command == "/knowledge":
            count = len(self.knowledge.get_all())
            return f"You have {count} custom knowledge entries saved locally."

        if command == "/stats":
            return self.statistics_text()

        if command == "/about":
            return self.about_text()

        if command == "/clear":
            return "__CLEAR_CHAT__"

        if command == "/search":
            if not argument:
                return "Usage:\n/search keyword"

            results = self.memory.search_messages(argument)
            if not results:
                return "No matching messages found."

            lines = [f"Found {len(results)} message(s):", ""]
            for item in results[-10:]:
                role = item.get("role", "")
                content = item.get("content", "")
                label = "You" if role == "user" else "YuiBot"
                lines.append(f"{label}: {content}")
            return "\n".join(lines)

        if command == "/rules":
            enabled = self.rule_store.get_enabled()
            lines = [f"Rules: {len(self.rule_store.get_all())} total, {len(enabled)} enabled."]
            for rule in enabled[:20]:
                lines.append(f"• {rule.get('intent', 'Unnamed')} — {', '.join(rule.get('triggers', []))}")
            return "\n".join(lines)

        return (
            f"Unknown command: {command}\n\n"
            "Type /help to see available commands."
        )

    def statistics_text(self):
        stats = self.memory.get_statistics()
        return (
            "YuiBot Statistics\n\n"
            f"User messages: {stats.get('user_messages', 0)}\n"
            f"Bot messages: {stats.get('bot_messages', 0)}\n"
            f"Sessions: {stats.get('sessions', 0)}\n"
            f"Custom knowledge: {len(self.knowledge.get_all())}\n"
            f"Personal memories: {stats.get('memories', 0)}\n"
            f"Conversation messages: {stats.get('conversation_messages', 0)}\n"
            f"Rules: {len(self.rule_store.get_all())}"
        )

    def help_text(self):
        return """YuiBot v5 Commands

CHAT
  hello
  how are you?
  thanks
  bye

MEMORY
  my name is Alex
  remember my favorite color is blue
  what is my favorite color?
  forget my favorite color
  show my memories

KNOWLEDGE
  what is Python?
  what is HTML?
  what is a database?
  /knowledge

TEACH / CORRECT
  teach: what is my favorite food = Pizza
  correct: who made my game = I made it in Python
  the answer is ... (after YuiBot says it does not know)

IMPORT / EDIT
  Open Knowledge Garden to add, edit, delete, import .txt/.json, or export JSON.

CALCULATOR
  calculate 100 + 25
  calculate 20 * 5
  what is 100 divided by 4

COMMANDS
  /help
  /time
  /date
  /memory
  /knowledge
  /stats
  /search Python
  /rules
  /about
  /clear

YuiBot is completely offline.
No AI model or external API is used."""

    def about_text(self):
        return (
            "YuiBot v5\n\n"
            "A Python rule-based chatbot.\n\n"
            "Features:\n"
            "• Memory\n• Knowledge\n• Context\n• Personality\n"
            "• Custom rules\n• Commands\n• Statistics\n• Fuzzy matching\n\n"
            "No AI model.\nNo API.\nNo internet."
        )

    # ==========================================================
    # MAIN RESPONSE
    # ==========================================================

    def respond(self, original_message):
        if not original_message.strip():
            return "Please type something."

        text = self.normalize(original_message)
        self.last_question = text

        # Commands have priority over chat rules.
        if text.startswith("/"):
            self.last_intent = "command"
            return self.command(text)

        # Teaching is a dedicated command and should not be intercepted by rules.
        if text.startswith(("teach:", "correct:")):
            is_correction = text.startswith("correct:")
            content = original_message.split(":", 1)[1].strip()
            if "=" not in content:
                prefix = "correct" if is_correction else "teach"
                return f"Format:\n\n{prefix}: question = answer"

            question, answer = content.split("=", 1)
            question = question.strip()
            answer = answer.strip()
            if not question or not answer:
                return "Question and answer cannot be empty."
            try:
                entry = self.knowledge.add(question, answer, "Corrected" if is_correction else "General", "Correction" if is_correction else "Chat teaching")
            except Exception as exc:
                return f"I couldn't save that knowledge: {exc}"
            self.last_unknown_question = None
            self.last_intent = "correction" if is_correction else "teach"
            return (
                ("Thanks for correcting me! I've updated my knowledge.\n\n" if is_correction else "Knowledge learned and saved locally!\n\n")
                + f"Question: {entry['question']}\nAnswer: {entry['answer']}"
            )

        # A simple follow-up correction works after an unknown question.
        if self.last_unknown_question and text.startswith(("the answer is ", "answer: ")):
            answer = re.sub(r"^(the answer is |answer:\s*)", "", original_message.strip(), flags=re.IGNORECASE).strip()
            if answer:
                question = self.last_unknown_question
                self.knowledge.add(question, answer, "Corrected", "Conversation correction")
                self.last_unknown_question = None
                self.last_intent = "correction"
                return f"Thank you for teaching me! I'll remember this locally.\n\nQuestion: {question}\nAnswer: {answer}"

        if text in ("help", "help me", "commands"):
            return self.help_text()

        if text in (
            "show my memories", "show memories", "what do you remember",
            "what do you remember about me",
        ):
            return self.show_memories()

        name = self.extract_name(original_message)
        if name:
            self.memory.set_profile("name", name, "Personal")
            return f"Nice to meet you, {name}! I'll remember your name."

        if text in ("what is my name", "what's my name", "who am i", "do you remember my name"):
            name = self.memory.get_profile("name")
            return f"Your name is {name}." if name else "You haven't told me your name yet."

        if text in ("forget everything", "forget all", "clear knowledge"):
            self.knowledge.clear()
            return "I cleared all custom knowledge entries from the local knowledge store."

        if text in ("clear memories", "forget my memories"):
            self.memory.clear_profile()
            return "I cleared my personal memories."

        forgotten = self.forget_fact(text)
        if forgotten:
            return forgotten

        remembered = self.remember_fact(text)
        if remembered:
            return remembered

        recalled = self.recall_fact(text)
        if recalled:
            return recalled

        # Keep the explicit built-in greeting/personality behaviour.
        if text in ("hello", "hi", "hey", "good morning", "good afternoon", "good evening"):
            self.last_intent = "greeting"
            return self.personality("greeting")

        if "how are you" in text or "how do you feel" in text:
            self.last_intent = "how_are_you"
            mode = self.settings.get("personality", "Friendly")
            if mode == "Short":
                return "I'm good!"
            if mode == "Professional":
                return "I'm operating normally and ready to assist."
            if mode == "Casual":
                return "I'm good! Ready to chat."
            return "I'm doing well! Ready to chat."

        if text in ("thanks", "thank you", "thx"):
            return self.personality("thanks")

        if text in ("bye", "goodbye", "good night") or "see you" in text:
            return self.personality("goodbye")

        if text in ("good", "great", "awesome", "nice", "fine", "okay", "ok"):
            if self.last_intent == "how_are_you":
                return "Glad to hear it!"
            return "Nice!"

        if (
            "what time" in text or "current time" in text or
            text == "time" or "tell me the time" in text
        ):
            now = datetime.datetime.now()
            return "The current time is " + now.strftime("%I:%M %p").lstrip("0") + "."

        if (
            "what date" in text or "today's date" in text or
            "todays date" in text or text == "date" or "what day is it" in text
        ):
            now = datetime.datetime.now()
            return "Today is " + now.strftime("%A, %d %B %Y") + "."

        calculation = self.calculate(text)
        if calculation:
            return calculation

        contextual = self.contextual_question(text)
        if contextual:
            self.last_intent = "context"
            return contextual

        # Try custom rules before the knowledge fallback.
        rule_response = self.match_rule(text)
        if rule_response is not None:
            return rule_response

        answer, score, category = self.search_knowledge(text)
        if answer:
            self.last_intent = "knowledge"
            self.last_topic = self.detect_topic(text, category)
            return answer

        self.last_intent = "unknown"
        self.last_unknown_question = original_message.strip()
        return (
            "I'm not sure how to answer that yet.\n\n"
            "You can teach or correct me with:\n"
            "teach: question = answer\n"
            "correct: question = answer\n\n"
            "Or send the next message as: the answer is ...\n"
            "You can also open Knowledge Garden to import, edit, or delete entries."
        )
