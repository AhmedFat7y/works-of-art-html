import json
import random
import os

from logger_wrapper import LoggingWrapper, get_script_path


logger = LoggingWrapper.get_logger(__file__)

NUMBER_OF_USERS = 20
NUMBER_OF_NOVELS = 10
NUMBER_OF_GENRES = 10
MAX_NUMBR_OF_LEVELS = 7
MAX_NUMBER_OF_CHAPTERS_PER_LEVEL = 7


class DataCreator:

  def __init__(self):
    data = self.load_data()
    self.genres_data = data['genres']
    self.titles = data['titles']
    self.short_titles = filter(lambda x: ' ' not in x, self.titles)
    self.long_titles = filter(lambda x: ' ' in x, self.titles)
    self.males_names = data['males_names']
    self.females_names = data['females_names']
    self.users = []
    self.chapters = []
    self.novels = []
    self.genres = []
    self.titles_reserved = []
    self.males_names_reserved = []
    self.females_names_reserved = []

  def load_data(self):
    logger.info('Reading names and titles from file . . .')
    data_path = os.path.join(get_script_path(), 'names_and_titles.json')
    with open(data_path, 'r') as f:
      data = json.loads(f.read())
    logger.info('Done.')
    return data

  def get_title(self):
    """return title"""
    title = 'Default Title'
    # for (i in range)
    title = random.choice(self.titles)
    self.titles_reserved.append(title)
    return title

  def get_male_name(self):
    """return (first name, last name)"""
    return (random.choice(self.males_names), random.choice(self.males_names))

  def get_female_name(self):
    """return (first name, last name)"""
    return (random.choice(self.females_names), random.choice(self.males_names))

  def format_user_data(self, index, first_name, last_name):
    return """
      User_{0}:
        id: {0}
        email: {1}.{2}@gmail.com
        encrypted_password: "$2a$10$KMYs9whkhl1uLyeJSqMFLutp.K6f0zZuPp0V4A7Pgy1ihZjV71lR6"
        user: {1} {2}
    """.format(index, first_name, last_name)

  def format_genre_data(self, index, genre):
    return """
      Genre_{0}:
        id: {0}
        name: {1}
    """.format(index, genre)

  def format_novel_data(self, index, title, user_name, genres, abstract=''):
    return """
      Novel_{0}:
        id: {0}
        title: {1}
        user: {2}
        genres: {3}
        abstract: |-
          {4}
    """.format(index, title, user_name, genres, abstract)

  def format_chapter_data(self, index, title, chapter_no, parent_name, novel_name, user_name, abstract='', content=''):
    return """
      Chapter_{0}:
        id: {0}
        title: {1}
        chapter_no: {2}
        parent: {3}
        novel: {4}
        user: {5}
        abstract: |-
          {6}
        content: |-
          {7}
    """.format(index, title, chapter_no, parent_name, novel_name, user_name, abstract, content)

  def format_read_chapter_data(self, index, user_name, chapter_name):
    return """
      ReadChapter_{0}:
        id: {0}
        user: {1}
        chapter: {2}
    """.format(index, user_name, chapter_name)

  def format_liked_chapter_data(self, index, user_name, chapter_name):
    return """
      LikedChapter_{0}:
        id: {0}
        user: {1}
        chapter: {2}
    """.format(index, user_name, chapter_name)

  def create_users(self):
    logger.info('Creating %s users.' % NUMBER_OF_USERS)
    for i in xrange(NUMBER_OF_USERS):
      first_name, last_name = self.get_male_name()
      self.users.append({
        'index': i,
        'first_name': first_name,
        'last_name': last_name
      })
    logger.info('Done.')

  def create_genres(self):
    logger.info('Creating %s genres.' % len(self.genres_data))
    for i in xrange(len(self.genres_data)):
      self.genres.append({
        'index': i,
        'genre': self.genres_data[i]
      })
    logger.info('Done.')

  def create_novels(self):
    logger.info('Creating %s novels.' % NUMBER_OF_NOVELS)
    for i in xrange(NUMBER_OF_NOVELS):
      self.novels.append({
        'index': i,
        'title': self.get_title(),
        'abstract': 'Lorem ipsum Ut reprehenderit laboris magna irure magna pariatur in pariatur elit ut \
        id sed exercitation qui velit deserunt sed amet occaecat.'
      })
    logger.info('Done.')

  def create_chapters(self):
    logger.info('Creating %s chapters.' % (NUMBER_OF_NOVELS * MAX_NUMBER_OF_CHAPTERS_PER_LEVEL * MAX_NUMBR_OF_LEVELS))
    for i in xrange(NUMBER_OF_NOVELS * MAX_NUMBER_OF_CHAPTERS_PER_LEVEL * MAX_NUMBR_OF_LEVELS):
      self.chapters.append({
        'index': i,
        'title': self.get_title(),
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

  def start(self):
    logger.info('Started Creating Data for Testing . . .')
    self.create_initial_data()
    logger.info('Done.')


if __name__ == "__main__":
  data_creator = DataCreator()
  data_creator.start()
