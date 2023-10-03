print("Text reader:")
while 1:
  string = input()
  if string == "#":
    continue
  elif string == "done":
    print("Done!")
    break
  else:
    print(string)