import csv


class Chapter:
  def __init__(self, _id, title, parent_id, chapter_number):
    self.id = int(_id)
    self.title = title
    self.parent_id = int(parent_id)
    self.chapter_number = int(chapter_number)

  def __str__(self):
    return '%i, %i, %i, %s' % (self.id, self.parent_id, self.chapter_number, self.title)

  def __unicode__(self):
    return '%i, %i, %i, %s' % (self.id, self.parent_id, self.chapter_number, self.title)


def list_copy(l):
  for item in l:
    yield item


def max_chapter(chapter1, chapter2):
  if chapter1.chapter_number > chapter2.chapter_number:
   return chapter1
  else:
    return chapter2

chapters = []

with open('data.csv', 'r') as csvfile:
  data_reader = csv.reader(csvfile, delimiter=',')
  for row in data_reader:
    chapters.append(Chapter(*row))

jsonstr = '['

for chapter in list_copy(chapters):
  jsonstr += '{"ch": %i, "id": %i, "title": "%s", "pid": %i}' % (chapter.chapter_number, chapter.id, chapter.title, chapter.parent_id)
  if not chapter == chapters[-1]:
    jsonstr += ","


jsonstr += ']'


# chapters_tree = []

# # chapters = sorted(chapters, key=lambda chapter: chapter.chapter_number)

# max_chapter = reduce(max_chapter, chapters)

# for i in xrange(max_chapter.chapter_number):
#   chapters_tree.append(filter(lambda chapter: chapter.chapter_number == i + 1, chapters))
# print chapters_tree

with open('data.json', 'w') as jsonfile:
  jsonfile.write(jsonstr)
  jsonfile.flush()
