import unittest

class Bookaholics():
  def __init__(self):
    self.booklists = []
    self.add_list('To Be Read') # Initialize with a standard list

  def get_list_names(self):
    list_names = []
    for booklist in self.booklists:
      list_names.append(booklist.name)
    return list_names

  def add_list(self, list_name):
    if list_name in self.get_list_names():
      return f'List {list_name} already exists'
    new_list = Booklist(list_name)
    self.booklists.append(new_list)
    return new_list

class Booklist():
  def __init__(self, name):
    self.name = name
    self.books = []
  
  def get_books(self):
    return self.books

class TestMethods(unittest.TestCase):
  # Tests adding a list that already exists
  def test_duplicate(self):
    B = Bookaholics()
    new_list_name = 'To Be Read'
    self.assertEqual(B.add_list(new_list_name), f'List {new_list_name} already exists')

  def test_success(self):
    B = Bookaholics()
    new_list_name = 'Finished Reading'
    
    # Make sure add_list() returns a member of the Booklist class
    self.assertIsInstance(B.add_list(new_list_name), Booklist)
  
if __name__ == '__main__':
    unittest.main()
