# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionProvideSkillset(Action):
#     def name(self):
#         return "action_provide_skillset"

#     def run(self, dispatcher, tracker, domain):
#         response = "I am skilled in Python, C, C++, Embedded C, MATLAB, Simulink, Verilog-HDL, VHDL, and JavaScript."
#         dispatcher.utter_message(text=response)
#         return []

# class ActionProvideExperience(Action):
#     def name(self):
#         return "action_provide_experience"

#     def run(self, dispatcher, tracker, domain):
#         response = ("I have interned at Xenhester Innovation Pvt. Ltd., India, working on automation solutions, "
#                     "and also at Synergy Transformers Pvt. Ltd., analyzing transformer manufacturing processes.")
#         dispatcher.utter_message(text=response)
#         return []
