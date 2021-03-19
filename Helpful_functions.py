class Additional_calculations:

  def __init__(self, tasks):
    self.tasks = tasks
    self.print_critical_path_length()

  def get_critical_path_length(self):
    list_of_paths = []
    for dic in self.tasks:
      list_of_paths.append(dic["end"])
    return max(list_of_paths)

  def print_critical_path_length(self):
    print("Critical path: " + str(self.get_critical_path_length()))


class Helpful_functions():
  def print_dic(self, list_of_dictionaries):
    for dic in list_of_dictionaries:
      print("-------------")
      for key, value in dic.items():
        print(key + ": " + str(value))

  def print_paths(self, paths):
    for path in paths:
      self.print_path(path)

  def print_path(self, path):
    print("-------")
    print("Tasks: " + str(path.task_names))
    print("Nodes: " + str(path.nodes))
    print(path.all_dependencies)
    print(path.done_with_time)

  def get_dic_with_name(self, name, tasks):
    for dic in tasks:
      if dic["name"] == name:
        return dic

  def get_max_number_of_dependencies(self, tasks):
    list_of_numbers_of_dependencies = []
    for dic in tasks:
      list_of_numbers_of_dependencies.append(len(dic["depends_on"]))
    return max(list_of_numbers_of_dependencies)

  def concatenate_lists(self, list1, list2):
    for element in list2:
      list1.append(element)
    return list1
