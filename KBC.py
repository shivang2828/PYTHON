#KBC

name = input("enter your name: ")
print("Welcome to KBC", name)
questions = [
  [
    "Who is India's Prime minister?", 'Narendra Modi', 'Rahul Gandhi',
    'Arvind Kejriwal', 'Akhilesh Yadav'
  ],
  [
    "Who is India's current captain?", 'Virat Kohli', 'Rohit Sharma',
    'Hardik Pandya', 'M.S.Dhoni'
  ],
  [
    "The members of the Rajya Sabha are elected by",
    'the people',
    'Lok Sabha',
    'elected members of the legislative assembly',
    'elected members of the legislative council',
  ],
  [
    "Who scored 100 centuries?",
    'Virat Kohli',
    'Rohit Sharma',
    'Sachin Tendulkar',
    'M.S.Dhoni',
  ],
  ["How many minutes are there in an hour?", '20', '120', '60', '30'],
  [
    "Name the National bird of India?", 'Peacock', 'Sparrow', 'Eagle', 'Parrot'
  ],
  [
    "Which festival is called the festival of colours?", 'Diwali', 'Holi',
    'Eid', 'Christmas'
  ],
  [
    " Who is the first woman prime minister of India?", 'Indira Gandhi',
    'Sonia Gandhi', 'Kiran Bedi', 'Sushma Swaraj'
  ],
  ["How many states are there in India?", '12', '23', '44', '28'],
  [
    "Name the first person to walk on the Moon?", 'Neil Armstrong',
    'Rakesh Sharma', 'Kalpana Chawala', 'Sunita Williams'
  ],
]
ans = (1, 2, 3, 3, 3, 1, 2, 1, 4, 1)
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
  question = questions[i]
  print(question)
  print(f"Question for Rs. {levels[i]}")
  reply = int(input("enter your choice(1-4) or 0 to quit:"))
  if (reply == ans[i]):
    print(f"Correct ! You Won the pricepool of Rs.", (levels[i]))
  elif (reply == 0):
    print("Thankyou for participating.")
    break
  else:
    print("Incorrect ! You lose the Game.")
    break

print(f"thank you for coming", name, "you have won RS.", (levels[i]))
print("thank you for participating")
