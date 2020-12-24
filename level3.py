import random
def hangman():
  words = [
    "apple",
    "orange",
    "banana",
    "peach",
    "soybean",
    "grape",
    "strawberry",
    "pineapple",
    "cherry",
    ]
  num = random.randint(0,len(words) - 1)
  wrong_count = 0
  stage = [
    "",
    "__________          ",
    "|                   ",
    "|         |         ",
    "|         O         ",
    "|        /|\        ",
    "|        / \        ",
    "|                   ",
  ]
  key_word = list(words[num])
  board = ["_"] * len(words[num])
  outcome = False

  print(" ".join(board))
  while wrong_count < len(stage) - 1:
    print("\n")

    answer = input("1文字予想してみよう :")
    if answer in key_word:
      number = key_word.index(answer)
      board[number] = answer
      key_word[number] = "$"
    else:
      wrong_count += 1

    e = wrong_count + 1
    print(" ".join(board))
    print("\n".join(stage[0:e]))

    if "_" not in  board:
      outcome = True
      break

  if not outcome:
    print("\n".join(stage[0:wrong_count + 1]))
    print(f"あなたの負け : 正解は{words[num]}")
  else:
    print("あなたの勝ち")

hangman()