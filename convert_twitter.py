# each output line should be:
# INPUT<tab>RESPONSE
with open('twitter_tab_format.txt', 'w') as f:
  prev_line = None
  # data source: https://github.com/Phylliida/Dialogue-Datasets
  for line in open('TwitterLowerAsciiCorpus.txt'):
    line = line.rstrip()

    if prev_line and line:
      f.write("%s\t%s\n" % (prev_line, line))
      
    prev_line = line
