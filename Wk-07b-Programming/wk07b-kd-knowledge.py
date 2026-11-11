import json 
from datetime import datetime 

def load_knowledge(filename): 
  with open(filename, "r", encoding="utf-8") as file: 
    return json.load(file) 

def ask_questions(questions):#argument questions = knowledge["questions"]
  print("\n") 
  print("1 ask_question called")
  answers = {} #container for the user ansers to be returned conains eg: {'power_on': 'no', 'display_on': 'no'}
  for question in questions: 
    key = question["key"]
    print(f"1a key = {key}") 
    print(f"1b question['text'] = {question["text"]}")
    questiontext = question["text"]
    print(f"1XX questiontext :,  {questiontext}")
    
    
    answer = input(question["text"] + " (yes/no): ").strip().lower() #answer must be yes or no

    while answer not in ["no", "yes"]:
          print("Your answer must br either 'yes' or 'no'")
          answer = input(question["text"] + " (yes/no): ").strip().lower() 
          print(f"1c answer = {answer}")
         
    answers[key] = answer
    print(f"1d answers[key] = {answers[key]}") 
  return answers

def matches(rule, answers): 
  print("\n") 
  print(f"matches called:")
  print(f"rule = {rule}")
  print(f"answers = {answers}")
  for key, expected in rule["when"].items(): 
    if answers.get(key) != expected: 
      return False 
  return True

def recommend(rules, answers):
  print("\n") 
  print(f"recommend called")
  print(f"rules = {rules}")
  print(f"answers = {answers}")
  for rule in rules: 
    print(f"recommend: about to call matches")
    if matches(rule, answers): 
      return rule["advice"] 
  return "No matching rule. Ask for further help."



knowledge = load_knowledge("wk07b-knowledge.json")
print (f"XX knowledge['questions'] {knowledge["questions"]} ")
answers = ask_questions(knowledge["questions"]) 
print(f"YY answers returned from ask_questions {answers}") #returns {'power_on': 'no', 'display_on': 'no'}
advice = recommend(knowledge["rules"], answers) 
print("Recommendation:", advice)

record = {"time": datetime.now().isoformat(timespec="seconds"), "answers": answers, "advice": advice}
history = []
try:
    with open("history.json", "r") as f:
      history = json.load(f) 
except FileNotFoundError:
      pass 
history.append(record) 
with open("history.json", "w") as f:
      json.dump(history, f, indent=4)