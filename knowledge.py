

# # BUILT_IN_KNOWLEDGE = {

# #     "what is your name":
# #         "My name is YuiBot.",

# #     "who are you":
# #         "I am YuiBot, an offline rule-based chatbot written in Python.",

# #     "what are you":
# #         "I am a Python chatbot that uses programmed rules, pattern matching, memory, and stored knowledge.",

# #     "who created you":
# #         "I was created as a Python chatbot project.",

# #     "what can you do":
# #         "I can chat, remember information, search conversations, calculate numbers, answer stored questions, learn custom knowledge, and run commands.",

# #     "what is your purpose":
# #         "My purpose is to demonstrate how a chatbot can be built using Python logic without an AI language model.",

# #     "are you ai":
# #         "I am a chatbot program, but I do not use an AI language model.",

# #     "do you use openai":
# #         "No. YuiBot does not use OpenAI.",

# #     "do you use ollama":
# #         "No. YuiBot does not use Ollama.",

# #     "do you use llama":
# #         "No. YuiBot does not use Llama.",

# #     "do you use qwen":
# #         "No. YuiBot does not use Qwen.",

# #     "do you use a model":
# #         "No. YuiBot does not use an AI model.",

# #     "what is python":
# #         "Python is a high-level programming language known for readable syntax and a large standard library.",

# #     "who created python":
# #         "Python was created by Guido van Rossum.",

# #     "when was python created":
# #         "Python was first released in 1991.",

# #     "what is programming":
# #         "Programming is the process of writing instructions that a computer can execute.",

# #     "what is tkinter":
# #         "Tkinter is Python's standard library for creating graphical user interfaces.",

# #     "what is pygame":
# #         "Pygame is a Python library commonly used for games and multimedia applications.",

# #     "what is html":
# #         "HTML is the markup language used to structure content on web pages.",

# #     "what is css":
# #         "CSS controls the appearance, layout, and presentation of web pages.",

# #     "what is javascript":
# #         "JavaScript is a programming language commonly used to add behavior and interactivity to websites.",

# #     "what is a website":
# #         "A website is a collection of web pages and resources accessible through the web.",

# #     "what is an api":
# #         "An API is an interface that allows software systems to communicate with each other.",

# #     "what is a database":
# #         "A database is an organized collection of data that can be stored, searched, and managed.",

# #     "what is sql":
# #         "SQL is a language used to work with relational databases.",

# #     "what is mysql":
# #         "MySQL is a relational database management system that uses SQL.",

# #     "what is sqlite":
# #         "SQLite is a lightweight database engine that stores a database in a single file.",

# #     "what is a computer":
# #         "A computer is an electronic system that processes data according to instructions.",

# #     "what is cpu":
# #         "CPU stands for Central Processing Unit. It executes instructions and performs calculations.",

# #     "what is ram":
# #         "RAM is temporary memory used by active programs.",

# #     "what is gpu":
# #         "A GPU is a processor designed for graphics and highly parallel calculations.",

# #     "what is cybersecurity":
# #         "Cybersecurity is the practice of protecting systems, networks, applications, and data.",

# #     "what is encryption":
# #         "Encryption transforms readable information into a protected form.",

# #     "what is a password":
# #         "A password is a secret string used to authenticate access to an account or system."
# # }


# # """Offline, JSON-backed knowledge store for YuiBot.

# # Supported imports: .txt and .json. Nothing is sent to the internet.
# # """
# import json
# import os
# import re
# import uuid
# from datetime import datetime

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# KNOWLEDGE_FILE = os.path.join(DATA_DIR, "knowledge.json")

# BUILT_IN_KNOWLEDGE = {
#     "what is python": "Python is a general-purpose programming language known for readable syntax and broad use in automation, applications, web development, and data processing.",
#     "what is html": "HTML is the markup language used to structure content on web pages.",
#     "what is css": "CSS describes the presentation and layout of HTML documents, including colors, spacing, and responsive layouts.",
#     "what is javascript": "JavaScript is a programming language commonly used to add interactivity to websites and also used in servers and other environments.",
#     "what is a database": "A database is an organized collection of information that can be stored, searched, updated, and managed.",
#     "what is sql": "SQL is a language used to query and manage data in relational databases.",
#     "what is sqlite": "SQLite is a lightweight, file-based relational database engine.",
#     "what is tkinter": "Tkinter is Python's standard interface to the Tk GUI toolkit, useful for building desktop windows and controls.",
#     "what is pygame": "Pygame is a Python library for making games and multimedia applications.",
#     "what is a cpu": "A CPU (central processing unit) executes instructions and performs general-purpose calculations for a computer.",
#     "what is ram": "RAM is short-term working memory used by a computer while programs are running.",
#     "what is cybersecurity": "Cybersecurity is the practice of protecting systems, networks, and information from unauthorized access and attacks.",
# }


# def _clean(value):
#     return str(value or "").strip()


# def _normalise_question(value):
#     value = _clean(value).lower()
#     value = re.sub(r"\s+", " ", value)
#     return value.rstrip(" ?.!\t\r\n")


# class KnowledgeStore:
#     """Persistent user-editable knowledge entries."""

#     def __init__(self, path=None):
#         self.path = os.path.abspath(path or KNOWLEDGE_FILE)
#         os.makedirs(os.path.dirname(self.path), exist_ok=True)
#         self.entries = []
#         self.load()

#     def load(self):
#         if not os.path.exists(self.path):
#             self.entries = []
#             self.save()
#             return self.get_all()
#         try:
#             with open(self.path, "r", encoding="utf-8") as f:
#                 data = json.load(f)
#             if isinstance(data, dict):
#                 data = data.get("entries", [])
#             if not isinstance(data, list):
#                 raise ValueError("Knowledge JSON must contain a list of entries.")
#             clean = []
#             for item in data:
#                 if not isinstance(item, dict):
#                     continue
#                 question = _clean(item.get("question", item.get("key", "")))
#                 answer = _clean(item.get("answer", item.get("value", "")))
#                 if not question or not answer:
#                     continue
#                 clean.append({
#                     "id": _clean(item.get("id")) or str(uuid.uuid4()),
#                     "question": question,
#                     "answer": answer,
#                     "category": _clean(item.get("category")) or "General",
#                     "source": _clean(item.get("source")) or "Manual",
#                     "created_at": _clean(item.get("created_at")) or datetime.now().isoformat(timespec="seconds"),
#                     "updated_at": _clean(item.get("updated_at")) or datetime.now().isoformat(timespec="seconds"),
#                 })
#             self.entries = clean
#         except (OSError, json.JSONDecodeError, ValueError) as exc:
#             # Do not overwrite a malformed file automatically; keep the store usable.
#             self.entries = []
#             self.last_load_error = str(exc)
#         return self.get_all()

#     def save(self):
#         os.makedirs(os.path.dirname(self.path), exist_ok=True)
#         temp_path = self.path + ".tmp"
#         with open(temp_path, "w", encoding="utf-8") as f:
#             json.dump({"version": 1, "entries": self.entries}, f, ensure_ascii=False, indent=2)
#         os.replace(temp_path, self.path)

#     def get_all(self):
#         return [dict(item) for item in self.entries]

#     def get(self, entry_id):
#         for item in self.entries:
#             if item["id"] == entry_id:
#                 return dict(item)
#         return None

#     def find_question(self, question):
#         key = _normalise_question(question)
#         for item in self.entries:
#             if _normalise_question(item["question"]) == key:
#                 return dict(item)
#         return None

#     def add(self, question, answer, category="General", source="Manual"):
#         question, answer = _clean(question), _clean(answer)
#         if not question or not answer:
#             raise ValueError("Question and answer are required.")
#         existing = self.find_question(question)
#         if existing:
#             self.update(existing["id"], question, answer, category, source)
#             return self.get(existing["id"])
#         now = datetime.now().isoformat(timespec="seconds")
#         item = {"id": str(uuid.uuid4()), "question": question, "answer": answer,
#                 "category": _clean(category) or "General", "source": _clean(source) or "Manual",
#                 "created_at": now, "updated_at": now}
#         self.entries.append(item)
#         self.save()
#         return dict(item)

#     def update(self, entry_id, question, answer, category="General", source=None):
#         question, answer = _clean(question), _clean(answer)
#         if not question or not answer:
#             raise ValueError("Question and answer are required.")
#         for item in self.entries:
#             if item["id"] == entry_id:
#                 item["question"] = question
#                 item["answer"] = answer
#                 item["category"] = _clean(category) or "General"
#                 if source is not None:
#                     item["source"] = _clean(source) or "Manual"
#                 item["updated_at"] = datetime.now().isoformat(timespec="seconds")
#                 self.save()
#                 return True
#         return False

#     def delete(self, entry_id):
#         old = len(self.entries)
#         self.entries = [item for item in self.entries if item["id"] != entry_id]
#         if len(self.entries) != old:
#             self.save()
#             return True
#         return False

#     def search(self, keyword=""):
#         needle = _clean(keyword).casefold()
#         if not needle:
#             return self.get_all()
#         return [dict(item) for item in self.entries
#                 if needle in item["question"].casefold()
#                 or needle in item["answer"].casefold()
#                 or needle in item["category"].casefold()]

#     def clear(self):
#         self.entries = []
#         self.save()

#     def export_file(self, path):
#         with open(path, "w", encoding="utf-8") as f:
#             json.dump({"version": 1, "entries": self.entries}, f, ensure_ascii=False, indent=2)

#     def import_file(self, path):
#         """Import .json entries or text lines in 'question = answer' format.

#         Plain text also accepts blocks:
#           Q: question\nA: answer
#         Blank lines separate Q/A blocks.
#         """
#         ext = os.path.splitext(path)[1].lower()
#         parsed = []
#         if ext == ".json":
#             with open(path, "r", encoding="utf-8-sig") as f:
#                 data = json.load(f)
#             if isinstance(data, dict):
#                 if any(key in data for key in ("entries", "knowledge", "items")):
#                     data = data.get("entries", data.get("knowledge", data.get("items", [])))
#                 else:
#                     # Also accept a simple mapping such as {"question": "answer"}.
#                     data = [{"question": key, "answer": value} for key, value in data.items()]
#                 if isinstance(data, dict):
#                     data = [{"question": key, "answer": value} for key, value in data.items()]
#             if not isinstance(data, list):
#                 raise ValueError("JSON must contain a list of entries or a question-to-answer object.")
#             for item in data:
#                 if isinstance(item, dict):
#                     q = item.get("question", item.get("key", item.get("trigger", "")))
#                     a = item.get("answer", item.get("value", item.get("response", "")))
#                     if _clean(q) and _clean(a):
#                         parsed.append((q, a, item.get("category", "Imported")))
#                 elif isinstance(item, str) and "=" in item:
#                     q, a = item.split("=", 1)
#                     if _clean(q) and _clean(a): parsed.append((q, a, "Imported"))
#         elif ext in (".txt", ".text", ""):
#             with open(path, "r", encoding="utf-8-sig") as f:
#                 raw = f.read()
#             blocks = re.split(r"\n\s*\n", raw)
#             for block in blocks:
#                 block = block.strip()
#                 if not block or block.startswith("#"):
#                     continue
#                 q_match = re.search(r"(?im)^\s*Q(?:uestion)?\s*:\s*(.+)$", block)
#                 a_match = re.search(r"(?im)^\s*A(?:nswer)?\s*:\s*(.+)$", block)
#                 if q_match and a_match:
#                     parsed.append((q_match.group(1), a_match.group(1), "Imported"))
#                     continue
#                 # Single-line Q = A or Q | A format.
#                 for line in block.splitlines():
#                     line = line.strip()
#                     if not line or line.startswith("#"):
#                         continue
#                     separator = " = " if " = " in line else (" | " if " | " in line else None)
#                     if separator:
#                         q, a = line.split(separator, 1)
#                         if _clean(q) and _clean(a): parsed.append((q, a, "Imported"))
#         else:
#             raise ValueError("Supported file types are .txt and .json.")

#         if not parsed:
#             raise ValueError("No knowledge entries found. Use 'question = answer' or Q:/A: text blocks.")
#         added = 0
#         for q, a, category in parsed:
#             before = self.find_question(q)
#             self.add(q, a, category, "Import")
#             if before is None:
#                 added += 1
#         return {"imported": len(parsed), "new": added, "total": len(self.entries)}


# # Backwards-friendly alias for code that uses KnowledgeBase.
# KnowledgeBase = KnowledgeStore




"""Offline, JSON-backed knowledge store for YuiBot.

Supported imports: .txt and .json. Nothing is sent to the internet.
"""
import json
import os
import re
import uuid
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
KNOWLEDGE_FILE = os.path.join(DATA_DIR, "knowledge.json")

BUILT_IN_KNOWLEDGE = {
    "what is python": "Python is a general-purpose programming language known for readable syntax and broad use in automation, applications, web development, and data processing.",
    "what is html": "HTML is the markup language used to structure content on web pages.",
    "what is css": "CSS describes the presentation and layout of HTML documents, including colors, spacing, and responsive layouts.",
    "what is javascript": "JavaScript is a programming language commonly used to add interactivity to websites and also used in servers and other environments.",
    "what is a database": "A database is an organized collection of information that can be stored, searched, updated, and managed.",
    "what is sql": "SQL is a language used to query and manage data in relational databases.",
    "what is sqlite": "SQLite is a lightweight, file-based relational database engine.",
    "what is tkinter": "Tkinter is Python's standard interface to the Tk GUI toolkit, useful for building desktop windows and controls.",
    "what is pygame": "Pygame is a Python library for making games and multimedia applications.",
    "what is a cpu": "A CPU (central processing unit) executes instructions and performs general-purpose calculations for a computer.",
    "what is ram": "RAM is short-term working memory used by a computer while programs are running.",
    "what is cybersecurity": "Cybersecurity is the practice of protecting systems, networks, and information from unauthorized access and attacks.",
}


def _clean(value):
    return str(value or "").strip()


def _normalise_question(value):
    value = _clean(value).lower()
    value = re.sub(r"\s+", " ", value)
    return value.rstrip(" ?.!\t\r\n")


class KnowledgeStore:
    """Persistent user-editable knowledge entries."""

    def __init__(self, path=None):
        self.path = os.path.abspath(path or KNOWLEDGE_FILE)
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self.entries = []
        self.load()

    def load(self):
        if not os.path.exists(self.path):
            self.entries = []
            self.save()
            return self.get_all()
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                data = data.get("entries", [])
            if not isinstance(data, list):
                raise ValueError("Knowledge JSON must contain a list of entries.")
            clean = []
            for item in data:
                if not isinstance(item, dict):
                    continue
                question = _clean(item.get("question", item.get("key", "")))
                answer = _clean(item.get("answer", item.get("value", "")))
                if not question or not answer:
                    continue
                clean.append({
                    "id": _clean(item.get("id")) or str(uuid.uuid4()),
                    "question": question,
                    "answer": answer,
                    "category": _clean(item.get("category")) or "General",
                    "source": _clean(item.get("source")) or "Manual",
                    "created_at": _clean(item.get("created_at")) or datetime.now().isoformat(timespec="seconds"),
                    "updated_at": _clean(item.get("updated_at")) or datetime.now().isoformat(timespec="seconds"),
                })
            self.entries = clean
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            # Do not overwrite a malformed file automatically; keep the store usable.
            self.entries = []
            self.last_load_error = str(exc)
        return self.get_all()

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        temp_path = self.path + ".tmp"
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump({"version": 1, "entries": self.entries}, f, ensure_ascii=False, indent=2)
        os.replace(temp_path, self.path)

    def get_all(self):
        return [dict(item) for item in self.entries]

    def get(self, entry_id):
        for item in self.entries:
            if item["id"] == entry_id:
                return dict(item)
        return None

    def find_question(self, question):
        key = _normalise_question(question)
        for item in self.entries:
            if _normalise_question(item["question"]) == key:
                return dict(item)
        return None

    def add(self, question, answer, category="General", source="Manual"):
        question, answer = _clean(question), _clean(answer)
        if not question or not answer:
            raise ValueError("Question and answer are required.")
        existing = self.find_question(question)
        if existing:
            self.update(existing["id"], question, answer, category, source)
            return self.get(existing["id"])
        now = datetime.now().isoformat(timespec="seconds")
        item = {"id": str(uuid.uuid4()), "question": question, "answer": answer,
                "category": _clean(category) or "General", "source": _clean(source) or "Manual",
                "created_at": now, "updated_at": now}
        self.entries.append(item)
        self.save()
        return dict(item)

    def update(self, entry_id, question, answer, category="General", source=None):
        question, answer = _clean(question), _clean(answer)
        if not question or not answer:
            raise ValueError("Question and answer are required.")
        for item in self.entries:
            if item["id"] == entry_id:
                item["question"] = question
                item["answer"] = answer
                item["category"] = _clean(category) or "General"
                if source is not None:
                    item["source"] = _clean(source) or "Manual"
                item["updated_at"] = datetime.now().isoformat(timespec="seconds")
                self.save()
                return True
        return False

    def delete(self, entry_id):
        old = len(self.entries)
        self.entries = [item for item in self.entries if item["id"] != entry_id]
        if len(self.entries) != old:
            self.save()
            return True
        return False

    def search(self, keyword=""):
        needle = _clean(keyword).casefold()
        if not needle:
            return self.get_all()
        return [dict(item) for item in self.entries
                if needle in item["question"].casefold()
                or needle in item["answer"].casefold()
                or needle in item["category"].casefold()]

    def clear(self):
        self.entries = []
        self.save()

    def export_file(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"version": 1, "entries": self.entries}, f, ensure_ascii=False, indent=2)

    def import_file(self, path):
        """Import .json or plain text knowledge files.

        TXT examples accepted:
            What is Python? = Python is a programming language.
            What is HTML=HTML structures web pages.

            Q: Who created Python?
            A: Guido van Rossum created Python.

            Question: What is RAM?
            Answer: RAM is a computer's short-term working memory.

        Q/A blocks may contain multi-line answers. Separate independent blocks
        with a blank line, or start a new block with another Q:/Question: line.
        """
        ext = os.path.splitext(path)[1].lower()
        parsed = []

        if ext == ".json":
            with open(path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
            if isinstance(data, dict):
                if any(key in data for key in ("entries", "knowledge", "items")):
                    data = data.get("entries", data.get("knowledge", data.get("items", [])))
                else:
                    data = [{"question": key, "answer": value} for key, value in data.items()]
            if isinstance(data, dict):
                data = [{"question": key, "answer": value} for key, value in data.items()]
            if not isinstance(data, list):
                raise ValueError("JSON must contain a list of entries or a question-to-answer object.")
            for item in data:
                if isinstance(item, dict):
                    q = item.get("question", item.get("key", item.get("trigger", "")))
                    a = item.get("answer", item.get("value", item.get("response", "")))
                    category = item.get("category", "Imported")
                    if _clean(q) and _clean(a):
                        parsed.append((_clean(q), _clean(a), _clean(category) or "Imported"))
                elif isinstance(item, str):
                    pair = self._parse_text_pair(item)
                    if pair:
                        parsed.append((pair[0], pair[1], "Imported"))

        elif ext in (".txt", ".text", ""):
            with open(path, "r", encoding="utf-8-sig") as f:
                raw = f.read()
            parsed.extend(self._parse_text_knowledge(raw))
        else:
            raise ValueError("Supported file types are .txt and .json.")

        if not parsed:
            raise ValueError(
                "No knowledge entries found. Check that the file contains pairs like "
                "'question = answer', 'Q: question\\nA: answer', or 'Question: ...\\nAnswer: ...'."
            )

        added = 0
        updated = 0
        for q, a, category in parsed:
            before = self.find_question(q)
            self.add(q, a, category, "Import")
            if before is None:
                added += 1
            else:
                updated += 1
        return {"imported": len(parsed), "new": added, "updated": updated, "total": len(self.entries)}

    @staticmethod
    def _parse_text_pair(line):
        """Parse a single-line question/answer pair using common separators."""
        line = _clean(line)
        if not line or line.startswith("#"):
            return None
        # Prefer separators with spaces, but also accept Question=Answer.
        match = re.match(r"^(.*?)\s*(?:=|\s\|\s|\t)\s*(.+)$", line)
        if not match:
            return None
        question, answer = _clean(match.group(1)), _clean(match.group(2))
        if question and answer:
            return question, answer
        return None

    @classmethod
    def _parse_text_knowledge(cls, raw):
        """Parse loose TXT formats without requiring exact spacing or blank lines."""
        parsed = []
        current_question = None
        answer_lines = []

        def flush():
            nonlocal current_question, answer_lines
            answer = "\n".join(line.strip() for line in answer_lines).strip()
            if current_question and answer:
                parsed.append((current_question.strip(), answer, "Imported"))
            current_question = None
            answer_lines = []

        for raw_line in raw.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                # Blank lines end a complete Q/A block, but do not discard an
                # unfinished question/answer while parsing a multi-line block.
                if not line and current_question and answer_lines:
                    flush()
                continue

            q_match = re.match(r"^(?:Q|Question)\s*:\s*(.*)$", line, flags=re.IGNORECASE)
            a_match = re.match(r"^(?:A|Answer)\s*:\s*(.*)$", line, flags=re.IGNORECASE)

            if q_match:
                flush()
                current_question = q_match.group(1).strip()
                continue
            if a_match and current_question is not None:
                # Allow repeated A: lines to continue the same answer.
                answer_lines.append(a_match.group(1).strip())
                continue

            # If we're inside a Q/A block, ordinary lines continue the answer.
            if current_question is not None:
                answer_lines.append(line)
                continue

            pair = cls._parse_text_pair(line)
            if pair:
                parsed.append((pair[0], pair[1], "Imported"))

        flush()
        return [(q, a, category) for q, a, category in parsed if _clean(q) and _clean(a)]


# Backwards-friendly alias for code that uses KnowledgeBase.
KnowledgeBase = KnowledgeStore
