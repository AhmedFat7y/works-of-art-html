import json
import random
import os
import re

from logger_wrapper import LoggingWrapper, get_script_path


logger = LoggingWrapper.get_logger(__file__)

NUMBER_OF_USERS = 20
NUMBER_OF_NOVELS = 10
NUMBER_OF_GENRES = 10
MIN_NUMBR_OF_LEVELS = 4
MAX_NUMBR_OF_LEVELS = 7
MIN_NUMBER_OF_CHAPTERS_PER_LEVEL = 4
MAX_NUMBER_OF_CHAPTERS_PER_LEVEL = 7
MIN_LIKES_PER_CHAPTER = 50
MAX_LIKES_PER_CHAPTER = 130
regex = re.compile(r"[ ,\t\n/'-]")
OUTPUT_DIR = 'fixtures/'
DEFAULT_CREATION_DATE = '---\n' + """DEFAULTS: &DEFAULTS
  created_at: <%= 3.weeks.ago.to_s(:db) %>"""


def format_list(l):
  return reduce(lambda x, y: x + ',' + y, l)


def get_relative_path(file_name):
  return os.path.join(get_script_path(), file_name)

if not os.path.exists(get_relative_path(OUTPUT_DIR)):
  os.makedirs(get_relative_path(OUTPUT_DIR))


class DataCreator:

  def __init__(self):
    data = self.load_data()
    self.genres_data = data['genres']
    self.titles = data['titles']
    self.short_titles = filter(lambda x: ' ' not in x, self.titles)
    self.long_titles = filter(lambda x: ' ' in x, self.titles)
    self.males_names = data['males_names']
    self.females_names = data['females_names']
    self.chapters_reserved = ['Default Chapter']
    self.users = []
    self.chapters = []
    self.novels = []
    self.genres = []
    self.liked_chapters = []
    self.read_chapters = []
    self.titles_reserved = ['Default Title']
    self.males_names_reserved = ['Default Name']
    self.females_names_reserved = ['Default Name']

  def load_data(self):
    logger.info('Reading names and titles from file . . .')
    data_path = get_relative_path('names_and_titles.json')
    with open(data_path, 'r') as f:
      data = json.loads(f.read())
    logger.info('Done.')
    return data

  def get_title(self):
    """return title"""
    title = 'Default Title'
    while title in self.titles_reserved:
      if len(self.titles_reserved) > 130:
        title = '{0} & {1}'.format(random.choice(self.short_titles), random.choice(self.short_titles))
      else:
        title = random.choice(self.titles)
    self.titles_reserved.append(title)
    return title

  def get_male_name(self):
    """return (first name, last name)"""
    name = 'Default Name'
    while name in self.males_names_reserved:
      name = (random.choice(self.males_names), random.choice(self.males_names))
    return name

  def get_female_name(self):
    """return (first name, last name)"""
    name = 'Default Name'
    while name in self.females_names_reserved:
      name = (random.choice(self.females_names), random.choice(self.males_names))
    return name

  def format_user_data(self, name, index, first_name, last_name):
    return """{0}:
      user_name: {2} {3}
      email: {2}.{3}@gmail.com
      encrypted_password: "$2a$10$KMYs9whkhl1uLyeJSqMFLutp.K6f0zZuPp0V4A7Pgy1ihZjV71lR6"
      <<: *DEFAULTS""".format(name, index, first_name, last_name)

  def format_genre_data(self, index, genre):
    return """{1}:
      name: {1}
      <<: *DEFAULTS""".format(index, genre)

  def format_novel_data(self, name, index, title, user_name, genres, abstract=''):
    genres_str = format_list(genres)
    return """{0}:
      title: {2}
      user: {3}
      genres: {4}
      <<: *DEFAULTS
      abstract: |-
        {5}""".format(name, index, title, user_name, genres_str, abstract)

  def format_chapter_data(self, name, index, title, chapter_no, parent_name, novel_name, user_name, abstract='', content=''):
    return """{0}:
      title: {2}
      chapter_no: {3}
      parent: {4}
      novel: {5}
      user: {6}
      <<: *DEFAULTS
      abstract: |-
        {7}
      content: |-
        {8}""".format(name, index, title, chapter_no, parent_name, novel_name, user_name, abstract, content)

  def format_read_chapter_data(self, index, user_name, chapter_name):
    return """ReadChapter_{0}:
      user: {1}
      chapter: {2}
      <<: *DEFAULTS""".format(index, user_name, chapter_name)

  def format_liked_chapter_data(self, index, user_name, chapter_name):
    return """LikedChapter_{0}:
      id: {0}
      user: {1}
      chapter: {2}
      <<: *DEFAULTS""".format(index, user_name, chapter_name)

  def create_users(self):
    logger.info('Creating %s users.' % NUMBER_OF_USERS)
    for i in xrange(NUMBER_OF_USERS):
      first_name, last_name = self.get_male_name()
      self.users.append({
        'index': (i + 1),
        'name': regex.sub('_', first_name + ' ' + last_name),
        'first_name': first_name,
        'last_name': last_name
      })
    logger.info('Done.')

  def create_genres(self):
    logger.info('Creating %s genres.' % len(self.genres_data))
    for i in xrange(len(self.genres_data)):
      self.genres.append({
        'index': (i + 1),
        'name': regex.sub('_', self.genres_data[i]),
        'genre': self.genres_data[i]
      })
    logger.info('Done.')

  def create_novels(self):
    logger.info('Creating %s novels.' % NUMBER_OF_NOVELS)
    for i in xrange(NUMBER_OF_NOVELS):
      novel_genres = []
      for j in range(4):
        novel_genres.append(random.choice(self.genres_data))
      title = self.get_title()
      self.novels.append({
        'index': (i + 1),
        'title': title,
        'name': regex.sub('_', title),
        'genres': novel_genres,
        'abstract': 'Lorem ipsum Ut reprehenderit laboris magna irure magna pariatur in pariatur elit ut \
        id sed exercitation qui velit deserunt sed amet occaecat.'
      })
    logger.info('Done.')

  def create_chapters(self):
    logger.info('Creating %s chapters.' % (NUMBER_OF_NOVELS * MAX_NUMBER_OF_CHAPTERS_PER_LEVEL * MAX_NUMBR_OF_LEVELS))
    for i in xrange(NUMBER_OF_NOVELS * MAX_NUMBER_OF_CHAPTERS_PER_LEVEL * MAX_NUMBR_OF_LEVELS):
      title = self.get_title()
      self.chapters.append({
        'index': (i + 1),
        'title': title,
        'name': regex.sub('_', title),
        'abstract': 'Lorem ipsum Ut reprehenderit laboris magna irure magna pariatur in pariatur elit ut \
          id sed exercitation qui velit deserunt sed amet occaecat.',
        'content': 'Lorem ipsum Mollit sed in consectetur sunt reprehenderit pariatur dolore ut aliquip velit dolore elit anim Duis irure exercitation magna aliqua incididunt in irure exercitation labore aliquip aliqua ea non est in culpa dolore sed occaecat deserunt in velit dolor ex qui consectetur et commodo elit ex id velit pariatur cupidatat nostrud fugiat reprehenderit dolore cillum eiusmod velit qui irure est in consectetur aliqua aute consequat deserunt ut laboris ex quis tempor eiusmod fugiat occaecat anim amet pariatur aliquip adipisicing culpa ad in laborum ex anim est ad consequat magna mollit Duis anim nisi eiusmod consectetur non in eiusmod sint consectetur laborum do do occaecat aute dolore sit ad occaecat sit cupidatat enim commodo minim fugiat magna ut labore deserunt tempor ut ad dolor id minim veniam irure cillum laborum irure ea irure magna dolor sint fugiat do dolor dolore eiusmod commodo anim in quis pariatur laboris occaecat ut fugiat laboris esse et Ut enim qui elit mollit eiusmod tempor culpa aute ullamco laboris in dolor proident occaecat veniam cillum Ut dolore cillum incididunt magna in magna commodo ut nulla dolore irure aute voluptate occaecat do dolore qui adipisicing deserunt velit pariatur ut ut officia nostrud velit magna eu pariatur qui aute ea dolor nisi incididunt dolore ea non sed commodo consectetur veniam ullamco proident ex est tempor ad occaecat dolor eiusmod consectetur culpa ea Excepteur nisi officia cupidatat enim anim dolor sint velit laborum ullamco amet esse in aliqua dolore qui esse ut laborum esse nostrud eiusmod veniam et occaecat.'
      })
    logger.info('Done.')

  def create_initial_data(self):
    self.create_users()
    self.create_genres()
    self.create_novels()
    self.create_chapters()

  def add_users_to_novels(self):
    for novel in self.novels:
      user = random.choice(self.users)
      novel['user'] = user['name']

  def add_users_to_chapters(self):
    for chapter in self.chapters:
      user = random.choice(self.users)
      chapter['user'] = user['name']

  def add_users_to_likes(self):
    for i in xrange(len(self.chapters)):
      chapter = self.chapters[i]
      for j in xrange(random.randint(MIN_LIKES_PER_CHAPTER, MAX_LIKES_PER_CHAPTER)):
        self.liked_chapters.append({
          'index': i * j + j + 1,
          'chapter': chapter['name'],
          'user': random.choice(self.users)['name']
        })

  def add_users_to_reads(self):
    for i in xrange(len(self.chapters)):
      chapter = self.chapters[i]
      self.read_chapters.append({
        'index': (i + 1),
        'chapter': chapter['name'],
        'user': random.choice(self.users)['name']
      })

  def add_chapters_to_novels(self):
    previous_level_chapters = []
    current_level_chapters = []
    for novel in self.novels:
      for i in xrange(random.randint(MIN_NUMBR_OF_LEVELS, MAX_NUMBR_OF_LEVELS)):
        chapter_number = (i + 1)
        previous_level_chapters = current_level_chapters
        current_level_chapters = []
        for j in xrange(random.randint(MIN_NUMBER_OF_CHAPTERS_PER_LEVEL, MAX_NUMBER_OF_CHAPTERS_PER_LEVEL)):
          chapter = self.get_chapter()
          current_level_chapters.append(chapter)
          chapter['novel'] = novel['name']
          chapter['chapter_no'] = chapter_number
          if len(previous_level_chapters) == 0:
            chapter['parent'] = ''
          else:
            chapter['parent'] = random.choice(previous_level_chapters)['name']

  def link_data(self):
    self.add_users_to_novels()
    self.add_users_to_chapters()
    self.add_users_to_reads()
    self.add_users_to_likes()
    self.add_chapters_to_novels()

  def get_chapter(self):
    chapter = 'Default Chapter'
    while chapter in self.chapters_reserved and len(self.chapters_reserved) != len(self.chapters):
      chapter = random.choice(self.chapters)
    return chapter

  def write_users(self):
    path = get_relative_path(OUTPUT_DIR + 'users.yml')
    with open(path, 'w') as f:
      f.write(DEFAULT_CREATION_DATE + '\n')
      for user in self.users:
        # (self, name, index, first_name, last_name)
        user_str = self.format_user_data(user['name'], user['index'], user['first_name'], user['last_name'])
        f.write(user_str + '\n')

  def write_genres(self):
    path = get_relative_path(OUTPUT_DIR + 'genres.yml')
    with open(path, 'w') as f:
      f.write(DEFAULT_CREATION_DATE + '\n')
      for genre in self.genres:
        # (self, index, genre)
        genre_str = self.format_genre_data(genre['index'], genre['genre'])
        f.write(genre_str + '\n')

  def write_novels(self):
    path = get_relative_path(OUTPUT_DIR + 'novels.yml')
    with open(path, 'w') as f:
      f.write(DEFAULT_CREATION_DATE + '\n')
      for novel in self.novels:
        # (self, name, index, title, user_name, genres, abstract='')
        novel_str = self.format_novel_data(
          novel['name'],
          novel['index'],
          novel['title'],
          novel['user'],
          novel['genres'],
          novel['abstract']
        )
        f.write(novel_str + '\n')

  def write_chapters(self):
    path = get_relative_path(OUTPUT_DIR + 'chapters.yml')
    with open(path, 'w') as f:
      f.write(DEFAULT_CREATION_DATE + '\n')
      for chapter in self.chapters:
        # (self, name, index, title, chapter_no, parent_name, novel_name, user_name, abstract='', content='')
        if 'chapter_no' not in chapter:
          continue
        chapter_str = self.format_chapter_data(
          chapter['name'],
          chapter['index'],
          chapter['title'],
          chapter['chapter_no'],
          chapter['parent'],
          chapter['novel'],
          chapter['user'],
          chapter['abstract'],
          chapter['content'],
        )
        f.write(chapter_str + '\n')

  def write_read_chapters(self):
    path = get_relative_path(OUTPUT_DIR + 'read_chapters.yml')
    with open(path, 'w') as f:
      f.write(DEFAULT_CREATION_DATE + '\n')
      for read_chapter in self.read_chapters:
        # (self, index, user_name, chapter_name):
        read_chapter_str = self.format_read_chapter_data(read_chapter['index'], read_chapter['user'], read_chapter['chapter'])
        f.write(read_chapter_str + '\n')

  def write_liked_chapters(self):
    path = get_relative_path(OUTPUT_DIR + 'liked_chapters.yml')
    with open(path, 'w') as f:
      f.write(DEFAULT_CREATION_DATE + '\n')
      for liked_chapter in self.liked_chapters:
        # (self, index, user_name, chapter_name):
        liked_chapter_str = self.format_liked_chapter_data(liked_chapter['index'], liked_chapter['user'], liked_chapter['chapter'])
        f.write(liked_chapter_str + '\n')

  def write_output(self):
    self.write_users()
    self.write_genres()
    self.write_novels()
    self.write_chapters()
    self.write_liked_chapters()
    self.write_read_chapters()

  def start(self):
    logger.info('Started Creating Data for Testing . . .')
    self.create_initial_data()
    self.link_data()
    self.write_output()
    logger.info('Done.')


if __name__ == "__main__":
  data_creator = DataCreator()
  data_creator.start()
