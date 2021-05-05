from os import path

def check(filename: str):
  if path.exists(filename):
    print('the file exists')
  else:
    print('load the file ')

def main():
  check('word_count.tst')
  word_count = 0
  char_count = 0
  line_count = 0
  with open('word_count.tst', 'r') as infile:
    lines = infile.read().split('\n')
    line_count= len(lines)
    for line in lines:
      words = line.split()
      word_count += len(words)
      char_count += len(line)
  print(f'''number of lines: {line_count} 
  number of words: {word_count} 
  number of characters: {char_count}''')

if __name__=='__main__':
  main()
