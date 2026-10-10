# # import json
# # import os
# # import uuid


# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # DATA_DIR = os.path.join(BASE_DIR, "data")
# # RULES_FILE = os.path.join(DATA_DIR, "rules.json")


# # DEFAULT_RULES = [

# #     {
# #         "id": "default_greeting",
# #         "intent": "greeting",
# #         "category": "Conversation",
# #         "enabled": True,
# #         "triggers": [
# #             "hello",
# #             "hi",
# #             "hey",
# #             "good morning",
# #             "good afternoon",
# #             "good evening"
# #         ],
# #         "responses": [
# #             "Hello!",
# #             "Hey there!",
# #             "Hi! How can I help?",
# #             "Hello! Nice to see you."
# #         ]
# #     },

# #     {
# #         "id": "default_thanks",
# #         "intent": "thanks",
# #         "category": "Conversation",
# #         "enabled": True,
# #         "triggers": [
# #             "thanks",
# #             "thank you",
# #             "thank you very much",
# #             "thanks a lot"
# #         ],
# #         "responses": [
# #             "You're welcome!",
# #             "No problem!",
# #             "Anytime!",
# #             "Glad I could help!"
# #         ]
# #     },

# #     {
# #         "id": "default_goodbye",
# #         "intent": "goodbye",
# #         "category": "Conversation",
# #         "enabled": True,
# #         "triggers": [
# #             "bye",
# #             "goodbye",
# #             "see you",
# #             "see you later"
# #         ],
# #         "responses": [
# #             "Goodbye!",
# #             "See you later!",
# #             "Bye! Take care!"
# #         ]
# #     },

# #     {
# #         "id": "default_how_are_you",
# #         "intent": "how_are_you",
# #         "category": "Conversation",
# #         "enabled": True,
# #         "triggers": [
# #             "how are you",
# #             "how are you doing",
# #             "are you okay"
# #         ],
# #         "responses": [
# #             "I'm doing well!",
# #             "I'm ready to help!",
# #             "I'm good. What would you like to do?"
# #         ]
# #     },

# #     {
# #         "id": "default_who_are_you",
# #         "intent": "identity",
# #         "category": "Conversation",
# #         "enabled": True,
# #         "triggers": [
# #             "who are you",
# #             "what are you",
# #             "tell me about yourself"
# #         ],
# #         "responses": [
# #             "I'm YuiBot, an offline Python chatbot.",
# #             "I'm YuiBot. I run locally without an AI model or internet connection."
# #         ]
# #     }
# # ]


# # class RuleStore:

# #     def __init__(self, memory=None):
# #         self.memory = memory
# #         os.makedirs(DATA_DIR, exist_ok=True)

# #         if not os.path.exists(RULES_FILE):
# #             self.rules = list(DEFAULT_RULES)
# #             self.save()
# #         else:
# #             self.rules = self.load()

# #     def load(self):
# #         try:
# #             with open(RULES_FILE, "r", encoding="utf-8") as f:
# #                 data = json.load(f)

# #             if isinstance(data, list):
# #                 return data

# #         except Exception:
# #             pass

# #         return list(DEFAULT_RULES)

# #     def save(self):
# #         with open(RULES_FILE, "w", encoding="utf-8") as f:
# #             json.dump(self.rules, f, indent=4, ensure_ascii=False)

# #     def get_all(self):
# #         return list(self.rules)

# #     def get_enabled(self):
# #         return [
# #             rule
# #             for rule in self.rules
# #             if rule.get("enabled", True)
# #         ]

# #     def get(self, rule_id):
# #         for rule in self.rules:
# #             if rule.get("id") == rule_id:
# #                 return rule

# #         return None

# #     def add(
# #         self,
# #         intent,
# #         category,
# #         triggers,
# #         responses,
# #         enabled=True
# #     ):
# #         rule = {
# #             "id": str(uuid.uuid4()),
# #             "intent": intent.strip(),
# #             "category": category.strip(),
# #             "enabled": enabled,
# #             "triggers": triggers,
# #             "responses": responses
# #         }

# #         self.rules.append(rule)
# #         self.save()

# #         if self.memory:
# #             self.memory.increment_rule_created()
# #             self.memory.save_all()

# #         return rule

# #     def update(
# #         self,
# #         rule_id,
# #         intent,
# #         category,
# #         triggers,
# #         responses,
# #         enabled=True
# #     ):
# #         rule = self.get(rule_id)

# #         if rule is None:
# #             return False

# #         rule["intent"] = intent.strip()
# #         rule["category"] = category.strip()
# #         rule["triggers"] = triggers
# #         rule["responses"] = responses
# #         rule["enabled"] = enabled

# #         self.save()
# #         return True

# #     def delete(self, rule_id):
# #         original = len(self.rules)

# #         self.rules = [
# #             rule
# #             for rule in self.rules
# #             if rule.get("id") != rule_id
# #         ]

# #         changed = len(self.rules) != original

# #         if changed:
# #             self.save()

# #         return changed

# #     def search(self, keyword):
# #         keyword = keyword.lower().strip()

# #         return [
# #             rule
# #             for rule in self.rules
# #             if keyword in rule.get("intent", "").lower()
# #             or keyword in rule.get("category", "").lower()
# #             or any(
# #                 keyword in trigger.lower()
# #                 for trigger in rule.get("triggers", [])
# #             )
# #         ]

# #     def export_rules(self, path):
# #         with open(path, "w", encoding="utf-8") as f:
# #             json.dump(self.rules, f, indent=4, ensure_ascii=False)

# #     def import_rules(self, path):
# #         with open(path, "r", encoding="utf-8") as f:
# #             data = json.load(f)

# #         if not isinstance(data, list):
# #             raise ValueError("Rule file must contain a JSON list.")

# #         valid = []

# #         for rule in data:

# #             if not isinstance(rule, dict):
# #                 continue

# #             if not rule.get("intent"):
# #                 continue

# #             if not isinstance(rule.get("triggers"), list):
# #                 continue

# #             if not isinstance(rule.get("responses"), list):
# #                 continue

# #             rule.setdefault("id", str(uuid.uuid4()))
# #             rule.setdefault("category", "General")
# #             rule.setdefault("enabled", True)

# #             valid.append(rule)

# #         self.rules = valid
# #         self.save()

# #     def restore_defaults(self):
# #         self.rules = list(DEFAULT_RULES)
# #         self.save()




# import copy
# import json
# import os
# import uuid


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# RULES_FILE = os.path.join(DATA_DIR, "rules.json")


# DEFAULT_RULES = [
#     {
#         "id": "default_greeting",
#         "intent": "greeting",
#         "category": "Conversation",
#         "enabled": True,
#         "triggers": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
#         "responses": ["Hello!", "Hey there!", "Hi! How can I help?", "Hello! Nice to see you."],
#     },
#     {
#         "id": "default_thanks",
#         "intent": "thanks",
#         "category": "Conversation",
#         "enabled": True,
#         "triggers": ["thanks", "thank you", "thank you very much", "thanks a lot"],
#         "responses": ["You're welcome!", "No problem!", "Anytime!", "Glad I could help!"],
#     },
#     {
#         "id": "default_goodbye",
#         "intent": "goodbye",
#         "category": "Conversation",
#         "enabled": True,
#         "triggers": ["bye", "goodbye", "see you", "see you later"],
#         "responses": ["Goodbye!", "See you later!", "Bye! Take care!"],
#     },
#     {
#         "id": "default_how_are_you",
#         "intent": "how_are_you",
#         "category": "Conversation",
#         "enabled": True,
#         "triggers": ["how are you", "how are you doing", "are you okay"],
#         "responses": ["I'm doing well!", "I'm ready to help!", "I'm good. What would you like to do?"],
#     },
#     {
#         "id": "default_who_are_you",
#         "intent": "identity",
#         "category": "Conversation",
#         "enabled": True,
#         "triggers": ["who are you", "what are you", "tell me about yourself"],
#         "responses": [
#             "I'm YuiBot, an offline Python chatbot.",
#             "I'm YuiBot. I run locally without an AI model or internet connection.",
#         ],
#     },
# ]


# class RuleStore:
#     def __init__(self, memory=None):
#         self.memory = memory
#         os.makedirs(DATA_DIR, exist_ok=True)
#         if not os.path.exists(RULES_FILE):
#             self.rules = copy.deepcopy(DEFAULT_RULES)
#             self.save()
#         else:
#             self.rules = self.load()

#     def load(self):
#         try:
#             with open(RULES_FILE, "r", encoding="utf-8") as file:
#                 data = json.load(file)
#             if isinstance(data, list):
#                 valid = []
#                 for item in data:
#                     if not isinstance(item, dict) or not item.get("intent"):
#                         continue
#                     if not isinstance(item.get("triggers"), list):
#                         continue
#                     if not isinstance(item.get("responses"), list):
#                         continue
#                     item.setdefault("id", str(uuid.uuid4()))
#                     item.setdefault("category", "General")
#                     item.setdefault("enabled", True)
#                     valid.append(item)
#                 return valid
#         except (OSError, json.JSONDecodeError, TypeError):
#             pass
#         return copy.deepcopy(DEFAULT_RULES)

#     def save(self):
#         os.makedirs(DATA_DIR, exist_ok=True)
#         temporary_path = RULES_FILE + ".tmp"
#         with open(temporary_path, "w", encoding="utf-8") as file:
#             json.dump(self.rules, file, indent=4, ensure_ascii=False)
#         os.replace(temporary_path, RULES_FILE)

#     def get_all(self):
#         return copy.deepcopy(self.rules)

#     def get_enabled(self):
#         return [copy.deepcopy(rule) for rule in self.rules if rule.get("enabled", True)]

#     def get(self, rule_id):
#         for rule in self.rules:
#             if rule.get("id") == rule_id:
#                 return copy.deepcopy(rule)
#         return None

#     def add(self, intent, category, triggers, responses, enabled=True):
#         rule = {
#             "id": str(uuid.uuid4()),
#             "intent": intent.strip(),
#             "category": category.strip() or "General",
#             "enabled": bool(enabled),
#             "triggers": [str(item).strip() for item in triggers if str(item).strip()],
#             "responses": [str(item).strip() for item in responses if str(item).strip()],
#         }
#         self.rules.append(rule)
#         self.save()

#         # Keep optional statistics calls compatible with different ChatMemory versions.
#         if self.memory:
#             if hasattr(self.memory, "increment_rule_created"):
#                 self.memory.increment_rule_created()
#             if hasattr(self.memory, "save_all"):
#                 self.memory.save_all()
#             elif hasattr(self.memory, "save"):
#                 self.memory.save()
#         return copy.deepcopy(rule)

#     def update(self, rule_id, intent, category, triggers, responses, enabled=True):
#         for rule in self.rules:
#             if rule.get("id") == rule_id:
#                 rule["intent"] = intent.strip()
#                 rule["category"] = category.strip() or "General"
#                 rule["triggers"] = [str(item).strip() for item in triggers if str(item).strip()]
#                 rule["responses"] = [str(item).strip() for item in responses if str(item).strip()]
#                 rule["enabled"] = bool(enabled)
#                 self.save()
#                 return True
#         return False

#     def delete(self, rule_id):
#         old_count = len(self.rules)
#         self.rules = [rule for rule in self.rules if rule.get("id") != rule_id]
#         changed = len(self.rules) != old_count
#         if changed:
#             self.save()
#         return changed

#     def search(self, keyword):
#         keyword = keyword.lower().strip()
#         if not keyword:
#             return self.get_all()
#         return [
#             copy.deepcopy(rule)
#             for rule in self.rules
#             if keyword in rule.get("intent", "").lower()
#             or keyword in rule.get("category", "").lower()
#             or any(keyword in str(trigger).lower() for trigger in rule.get("triggers", []))
#         ]

#     def export_rules(self, path):
#         with open(path, "w", encoding="utf-8") as file:
#             json.dump(self.rules, file, indent=4, ensure_ascii=False)

#     def import_rules(self, path):
#         with open(path, "r", encoding="utf-8") as file:
#             data = json.load(file)
#         if not isinstance(data, list):
#             raise ValueError("Rule file must contain a JSON list.")

#         valid = []
#         for item in data:
#             if not isinstance(item, dict) or not item.get("intent"):
#                 continue
#             if not isinstance(item.get("triggers"), list):
#                 continue
#             if not isinstance(item.get("responses"), list):
#                 continue

#             rule = copy.deepcopy(item)
#             rule.setdefault("id", str(uuid.uuid4()))
#             rule.setdefault("category", "General")
#             rule.setdefault("enabled", True)
#             rule["triggers"] = [str(value).strip() for value in rule["triggers"] if str(value).strip()]
#             rule["responses"] = [str(value).strip() for value in rule["responses"] if str(value).strip()]
#             if rule["triggers"] and rule["responses"]:
#                 valid.append(rule)

#         self.rules = valid
#         self.save()

#     def restore_defaults(self):
#         self.rules = copy.deepcopy(DEFAULT_RULES)
#         self.save()



import copy
import json
import os
import uuid


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RULES_FILE = os.path.join(DATA_DIR, "rules.json")


DEFAULT_RULES = [
    {
        "id": "default_greeting",
        "intent": "greeting",
        "category": "Conversation",
        "enabled": True,
        "triggers": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "responses": ["Hello!", "Hey there!", "Hi! How can I help?", "Hello! Nice to see you."],
    },
    {
        "id": "default_thanks",
        "intent": "thanks",
        "category": "Conversation",
        "enabled": True,
        "triggers": ["thanks", "thank you", "thank you very much", "thanks a lot"],
        "responses": ["You're welcome!", "No problem!", "Anytime!", "Glad I could help!"],
    },
    {
        "id": "default_goodbye",
        "intent": "goodbye",
        "category": "Conversation",
        "enabled": True,
        "triggers": ["bye", "goodbye", "see you", "see you later"],
        "responses": ["Goodbye!", "See you later!", "Bye! Take care!"],
    },
    {
        "id": "default_how_are_you",
        "intent": "how_are_you",
        "category": "Conversation",
        "enabled": True,
        "triggers": ["how are you", "how are you doing", "are you okay"],
        "responses": ["I'm doing well!", "I'm ready to help!", "I'm good. What would you like to do?"],
    },
    {
        "id": "default_who_are_you",
        "intent": "identity",
        "category": "Conversation",
        "enabled": True,
        "triggers": ["who are you", "what are you", "tell me about yourself"],
        "responses": [
            "I'm YuiBot, an offline Python chatbot.",
            "I'm YuiBot. I run locally without an AI model or internet connection.",
        ],
    },
]


class RuleStore:
    def __init__(self, memory=None):
        self.memory = memory
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(RULES_FILE):
            self.rules = copy.deepcopy(DEFAULT_RULES)
            self.save()
        else:
            self.rules = self.load()

    def load(self):
        try:
            with open(RULES_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, list):
                valid = []
                for item in data:
                    if not isinstance(item, dict) or not item.get("intent"):
                        continue
                    if not isinstance(item.get("triggers"), list):
                        continue
                    if not isinstance(item.get("responses"), list):
                        continue
                    item.setdefault("id", str(uuid.uuid4()))
                    item.setdefault("category", "General")
                    item.setdefault("enabled", True)
                    valid.append(item)
                return valid
        except (OSError, json.JSONDecodeError, TypeError):
            pass
        return copy.deepcopy(DEFAULT_RULES)

    def save(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        temporary_path = RULES_FILE + ".tmp"
        with open(temporary_path, "w", encoding="utf-8") as file:
            json.dump(self.rules, file, indent=4, ensure_ascii=False)
        os.replace(temporary_path, RULES_FILE)

    def get_all(self):
        return copy.deepcopy(self.rules)

    def get_enabled(self):
        return [copy.deepcopy(rule) for rule in self.rules if rule.get("enabled", True)]

    def get(self, rule_id):
        for rule in self.rules:
            if rule.get("id") == rule_id:
                return copy.deepcopy(rule)
        return None

    def add(self, intent, category, triggers, responses, enabled=True):
        rule = {
            "id": str(uuid.uuid4()),
            "intent": intent.strip(),
            "category": category.strip() or "General",
            "enabled": bool(enabled),
            "triggers": [str(item).strip() for item in triggers if str(item).strip()],
            "responses": [str(item).strip() for item in responses if str(item).strip()],
        }
        self.rules.append(rule)
        self.save()

        # Keep optional statistics calls compatible with different ChatMemory versions.
        if self.memory:
            if hasattr(self.memory, "increment_rule_created"):
                self.memory.increment_rule_created()
            if hasattr(self.memory, "save_all"):
                self.memory.save_all()
            elif hasattr(self.memory, "save"):
                self.memory.save()
        return copy.deepcopy(rule)

    def update(self, rule_id, intent, category, triggers, responses, enabled=True):
        for rule in self.rules:
            if rule.get("id") == rule_id:
                rule["intent"] = intent.strip()
                rule["category"] = category.strip() or "General"
                rule["triggers"] = [str(item).strip() for item in triggers if str(item).strip()]
                rule["responses"] = [str(item).strip() for item in responses if str(item).strip()]
                rule["enabled"] = bool(enabled)
                self.save()
                return True
        return False

    def delete(self, rule_id):
        old_count = len(self.rules)
        self.rules = [rule for rule in self.rules if rule.get("id") != rule_id]
        changed = len(self.rules) != old_count
        if changed:
            self.save()
        return changed

    def search(self, keyword):
        keyword = keyword.lower().strip()
        if not keyword:
            return self.get_all()
        return [
            copy.deepcopy(rule)
            for rule in self.rules
            if keyword in rule.get("intent", "").lower()
            or keyword in rule.get("category", "").lower()
            or any(keyword in str(trigger).lower() for trigger in rule.get("triggers", []))
        ]

    def export_rules(self, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.rules, file, indent=4, ensure_ascii=False)

    def import_rules(self, path):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Rule file must contain a JSON list.")

        valid = []
        for item in data:
            if not isinstance(item, dict) or not item.get("intent"):
                continue
            if not isinstance(item.get("triggers"), list):
                continue
            if not isinstance(item.get("responses"), list):
                continue

            rule = copy.deepcopy(item)
            rule.setdefault("id", str(uuid.uuid4()))
            rule.setdefault("category", "General")
            rule.setdefault("enabled", True)
            rule["triggers"] = [str(value).strip() for value in rule["triggers"] if str(value).strip()]
            rule["responses"] = [str(value).strip() for value in rule["responses"] if str(value).strip()]
            if rule["triggers"] and rule["responses"]:
                valid.append(rule)

        self.rules = valid
        self.save()

    def restore_defaults(self):
        self.rules = copy.deepcopy(DEFAULT_RULES)
        self.save()
