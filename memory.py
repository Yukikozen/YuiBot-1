# import json
# import os
# from datetime import datetime


# class ChatMemory:

#     def __init__(self, base_dir=None):

#         if base_dir is None:

#             base_dir = os.path.dirname(
#                 os.path.abspath(__file__)
#             )

#         self.base_dir = base_dir

#         self.data_dir = os.path.join(
#             self.base_dir,
#             "data"
#         )

#         os.makedirs(
#             self.data_dir,
#             exist_ok=True
#         )

#         self.history_file = os.path.join(
#             self.data_dir,
#             "chat_history.json"
#         )

#         self.knowledge_file = os.path.join(
#             self.data_dir,
#             "knowledge.json"
#         )

#         self.profile_file = os.path.join(
#             self.data_dir,
#             "profile.json"
#         )

#         self.statistics_file = os.path.join(
#             self.data_dir,
#             "statistics.json"
#         )

#         self.messages = []
#         self.knowledge = {}
#         self.profile = {}

#         self.statistics = {
#             "user_messages": 0,
#             "bot_messages": 0,
#             "sessions": 0
#         }

#         self.load_messages()
#         self.load_knowledge()
#         self.load_profile()
#         self.load_statistics()

#     # ==========================================================
#     # JSON
#     # ==========================================================

#     def load_json(
#         self,
#         filename,
#         default
#     ):

#         try:

#             if not os.path.exists(filename):
#                 return default

#             with open(
#                 filename,
#                 "r",
#                 encoding="utf-8"
#             ) as file:

#                 return json.load(file)

#         except Exception:

#             return default

#     def save_json(
#         self,
#         filename,
#         data
#     ):

#         try:

#             with open(
#                 filename,
#                 "w",
#                 encoding="utf-8"
#             ) as file:

#                 json.dump(
#                     data,
#                     file,
#                     indent=4,
#                     ensure_ascii=False
#                 )

#             return True

#         except Exception:

#             return False

#     # ==========================================================
#     # CHAT
#     # ==========================================================

#     def load_messages(self):

#         data = self.load_json(
#             self.history_file,
#             []
#         )

#         if isinstance(
#             data,
#             list
#         ):

#             self.messages = data

#         else:

#             self.messages = []

#     def save_messages(self):

#         return self.save_json(
#             self.history_file,
#             self.messages
#         )

#     def add_message(
#         self,
#         role,
#         content
#     ):

#         self.messages.append({
#             "role": role,
#             "content": content,
#             "timestamp": datetime.now().isoformat(
#                 timespec="seconds"
#             )
#         })

#         if role == "user":

#             self.statistics[
#                 "user_messages"
#             ] += 1

#         elif role == "assistant":

#             self.statistics[
#                 "bot_messages"
#             ] += 1

#         self.save_messages()
#         self.save_statistics()

#     def add_user_message(
#         self,
#         content
#     ):

#         self.add_message(
#             "user",
#             content
#         )

#     def add_assistant_message(
#         self,
#         content
#     ):

#         self.add_message(
#             "assistant",
#             content
#         )

#     def get_messages(self):

#         return list(
#             self.messages
#         )

#     def clear_messages(self):

#         self.messages = []

#         self.save_messages()

#     # ==========================================================
#     # KNOWLEDGE
#     # ==========================================================

#     def load_knowledge(self):

#         data = self.load_json(
#             self.knowledge_file,
#             {}
#         )

#         if isinstance(
#             data,
#             dict
#         ):

#             self.knowledge = data

#         else:

#             self.knowledge = {}

#     def save_knowledge(self):

#         return self.save_json(
#             self.knowledge_file,
#             self.knowledge
#         )

#     def set_knowledge(
#         self,
#         question,
#         answer,
#         category="General"
#     ):

#         self.knowledge[
#             question
#         ] = {
#             "answer": answer,
#             "category": category
#         }

#         self.save_knowledge()

#     def get_knowledge(self):

#         return dict(
#             self.knowledge
#         )

#     def delete_knowledge(
#         self,
#         question
#     ):

#         if question in self.knowledge:

#             del self.knowledge[
#                 question
#             ]

#             self.save_knowledge()

#             return True

#         return False

#     def clear_knowledge(self):

#         self.knowledge = {}

#         self.save_knowledge()

#     def export_knowledge(
#         self,
#         filename
#     ):

#         return self.save_json(
#             filename,
#             self.knowledge
#         )

#     def import_knowledge(
#         self,
#         filename
#     ):

#         data = self.load_json(
#             filename,
#             None
#         )

#         if not isinstance(
#             data,
#             dict
#         ):

#             return False

#         self.knowledge = data

#         self.save_knowledge()

#         return True

#     # ==========================================================
#     # PROFILE
#     # ==========================================================

#     def load_profile(self):

#         data = self.load_json(
#             self.profile_file,
#             {}
#         )

#         if isinstance(
#             data,
#             dict
#         ):

#             self.profile = data

#         else:

#             self.profile = {}

#     def save_profile(self):

#         return self.save_json(
#             self.profile_file,
#             self.profile
#         )

#     def set_profile(
#         self,
#         key,
#         value,
#         category="Personal"
#     ):

#         self.profile[
#             key
#         ] = {
#             "value": value,
#             "category": category
#         }

#         self.save_profile()

#     def get_profile(
#         self,
#         key,
#         default=None
#     ):

#         item = self.profile.get(
#             key
#         )

#         if isinstance(
#             item,
#             dict
#         ):

#             return item.get(
#                 "value",
#                 default
#             )

#         if item is not None:

#             return item

#         return default

#     def get_profile_all(self):

#         return dict(
#             self.profile
#         )

#     def delete_profile(
#         self,
#         key
#     ):

#         if key in self.profile:

#             del self.profile[
#                 key
#             ]

#             self.save_profile()

#             return True

#         return False

#     def clear_profile(self):

#         self.profile = {}

#         self.save_profile()

#     # ==========================================================
#     # SEARCH
#     # ==========================================================

#     def search_messages(
#         self,
#         query
#     ):

#         query = query.lower().strip()

#         if not query:
#             return []

#         results = []

#         for message in self.messages:

#             content = str(
#                 message.get(
#                     "content",
#                     ""
#                 )
#             )

#             if query in content.lower():

#                 results.append(
#                     message
#                 )

#         return results

#     # ==========================================================
#     # STATISTICS
#     # ==========================================================

#     def load_statistics(self):

#         data = self.load_json(
#             self.statistics_file,
#             self.statistics
#         )

#         if isinstance(
#             data,
#             dict
#         ):

#             self.statistics.update(
#                 data
#             )

#     def save_statistics(self):

#         return self.save_json(
#             self.statistics_file,
#             self.statistics
#         )

#     def new_session(self):

#         self.statistics[
#             "sessions"
#         ] += 1

#         self.save_statistics()

#     def get_statistics(self):

#         stats = dict(
#             self.statistics
#         )

#         stats[
#             "knowledge_entries"
#         ] = len(
#             self.knowledge
#         )

#         stats[
#             "memories"
#         ] = len(
#             self.profile
#         )

#         stats[
#             "conversation_messages"
#         ] = len(
#             self.messages
#         )

#         return stats

#     # ==========================================================
#     # SAVE ALL
#     # ==========================================================

#     def save(self):

#         self.save_messages()
#         self.save_knowledge()
#         self.save_profile()
#         self.save_statistics()



import json
import os
from datetime import datetime


class ChatMemory:

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

        self.history_file = os.path.join(
            self.data_dir,
            "chat_history.json"
        )

        self.knowledge_file = os.path.join(
            self.data_dir,
            "knowledge.json"
        )

        self.profile_file = os.path.join(
            self.data_dir,
            "profile.json"
        )

        self.statistics_file = os.path.join(
            self.data_dir,
            "statistics.json"
        )

        self.messages = []
        self.knowledge = {}
        self.profile = {}

        self.statistics = {
            "user_messages": 0,
            "bot_messages": 0,
            "sessions": 0
        }

        self.load_messages()
        self.load_knowledge()
        self.load_profile()
        self.load_statistics()

    # ==========================================================
    # JSON HELPERS
    # ==========================================================

    def load_json(self, filename, default):

        try:
            if not os.path.exists(filename):
                return default

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:
                return json.load(file)

        except (OSError, json.JSONDecodeError):
            return default

    def save_json(self, filename, data):

        try:
            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except (OSError, TypeError, ValueError):
            return False

    # ==========================================================
    # CHAT HISTORY
    # ==========================================================

    def load_messages(self):

        data = self.load_json(
            self.history_file,
            []
        )

        if isinstance(data, list):
            self.messages = data
        else:
            self.messages = []

    def save_messages(self):

        return self.save_json(
            self.history_file,
            self.messages
        )

    def add_message(self, role, content):

        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            )
        }

        self.messages.append(message)

        if role == "user":
            self.statistics["user_messages"] += 1

        elif role in ("assistant", "bot"):
            self.statistics["bot_messages"] += 1

        self.save_messages()
        self.save_statistics()

    def add_user_message(self, content):

        self.add_message(
            "user",
            content
        )

    def add_assistant_message(self, content):

        self.add_message(
            "assistant",
            content
        )

    def get_messages(self):

        return list(self.messages)

    def get_history(self):

        """Compatibility method used by the chat interface."""
        return self.get_messages()

    def clear_messages(self):

        self.messages = []
        return self.save_messages()

    # ==========================================================
    # KNOWLEDGE
    # ==========================================================

    def load_knowledge(self):

        data = self.load_json(
            self.knowledge_file,
            {}
        )

        if isinstance(data, dict):
            self.knowledge = data
        else:
            self.knowledge = {}

    def save_knowledge(self):

        return self.save_json(
            self.knowledge_file,
            self.knowledge
        )

    def set_knowledge(
        self,
        question,
        answer,
        category="General"
    ):

        self.knowledge[question] = {
            "answer": answer,
            "category": category
        }

        return self.save_knowledge()

    def get_knowledge(self):

        return dict(self.knowledge)

    def delete_knowledge(self, question):

        if question in self.knowledge:
            del self.knowledge[question]
            self.save_knowledge()
            return True

        return False

    def clear_knowledge(self):

        self.knowledge = {}
        return self.save_knowledge()

    def export_knowledge(self, filename):

        return self.save_json(
            filename,
            self.knowledge
        )

    def import_knowledge(self, filename):

        data = self.load_json(
            filename,
            None
        )

        if not isinstance(data, dict):
            return False

        self.knowledge = data
        return self.save_knowledge()

    # ==========================================================
    # PROFILE / USER MEMORIES
    # ==========================================================

    def load_profile(self):

        data = self.load_json(
            self.profile_file,
            {}
        )

        if isinstance(data, dict):
            self.profile = data
        else:
            self.profile = {}

    def save_profile(self):

        return self.save_json(
            self.profile_file,
            self.profile
        )

    def set_profile(
        self,
        key,
        value,
        category="Personal"
    ):

        self.profile[key] = {
            "value": value,
            "category": category
        }

        return self.save_profile()

    def get_profile(self, key, default=None):

        item = self.profile.get(key)

        if isinstance(item, dict):
            return item.get("value", default)

        if item is not None:
            return item

        return default

    def get_profile_all(self):

        return dict(self.profile)

    def delete_profile(self, key):

        if key in self.profile:
            del self.profile[key]
            self.save_profile()
            return True

        return False

    def clear_profile(self):

        self.profile = {}
        return self.save_profile()

    # ==========================================================
    # SEARCH CHAT MESSAGES
    # ==========================================================

    def search_messages(self, query):

        query = str(query).lower().strip()

        if not query:
            return []

        results = []

        for message in self.messages:

            content = str(
                message.get("content", "")
            )

            if query in content.lower():
                results.append(dict(message))

        return results

    # ==========================================================
    # STATISTICS
    # ==========================================================

    def load_statistics(self):

        data = self.load_json(
            self.statistics_file,
            self.statistics
        )

        if isinstance(data, dict):
            self.statistics.update(data)

    def save_statistics(self):

        return self.save_json(
            self.statistics_file,
            self.statistics
        )

    def new_session(self):

        self.statistics["sessions"] += 1
        return self.save_statistics()

    def get_statistics(self):

        stats = dict(self.statistics)

        stats["knowledge_entries"] = len(
            self.knowledge
        )

        stats["memories"] = len(
            self.profile
        )

        stats["conversation_messages"] = len(
            self.messages
        )

        return stats

    # ==========================================================
    # SAVE ALL DATA
    # ==========================================================

    def save(self):

        results = [
            self.save_messages(),
            self.save_knowledge(),
            self.save_profile(),
            self.save_statistics()
        ]

        return all(results)
