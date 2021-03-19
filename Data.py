# Project imports:
from Helpful_functions import Helpful_functions, Additional_calculations
from Gantt_chart import Gantt_chart
from Bar_chart import Bar_chart, Prepare_bar_graph_data

import matplotlib.pyplot as plt



class Data:
  def __init__(self, hf):
    self.hf = hf
    # name, duration, depends_on, workers, start, end, initialised
    self.tasks = [
      dict(name = "A", duration = 3, depends_on = [],            workers = 2, start = 0, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "B", duration = 5,  depends_on = [],           workers = 3, start = 0, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "C", duration = 10, depends_on = ["B"],        workers = 2, start = 0, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "D", duration = 10,  depends_on = ["A"],       workers = 2, start = 0, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "E", duration = 21,  depends_on = ["A", "B"],  workers = 4, start = 0, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "F", duration = 12,  depends_on = ["C", "D"],  workers = 2, start = 0, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False)
    ]
    self.cal_start()
    self.cal_end()
    #self.hf.print_dic(self.tasks)

  def cal_start(self):
    number_of_dependencies = 0
    # Iterates over increasing number of dependencies
    while number_of_dependencies <= self.hf.get_max_number_of_dependencies(self.tasks):
      while (self.x_dep_have_been_initialised(number_of_dependencies) is False):
        self.tasks = self.cal_start_x_dep(number_of_dependencies)
      number_of_dependencies = number_of_dependencies + 1

  def cal_start_x_dep(self, number_of_dependencies):
    for dic in self.tasks:
      if len(dic["depends_on"]) == number_of_dependencies and self.dependencies_initialised(dic):
        dic["start"] = self.get_maximum_path(dic)
        dic["initialised"] = True
    return self.tasks

  def cal_end(self):
    for dic in self.tasks:
      dic["end"] = dic["start"] + dic["duration"]
    return self.tasks

  # Returns true if dependencies have been initialised
  def x_dep_have_been_initialised(self, number_of_dependencies):
    initialised = True
    for dic in self.tasks:
      if len(dic["depends_on"]) == number_of_dependencies:
        if dic["initialised"] is False:
          initialised = False
    return initialised

  # Returns true if dependencies have been initialised
  def dependencies_initialised(self, dic):
    initialised = True
    if len(dic["depends_on"]) != 0:
      for dependency in dic["depends_on"]:
        if self.hf.get_dic_with_name(dependency, self.tasks)["initialised"] is False:
          initialised = False
    return initialised

  # Assumes all dependencies have been initialised
  def get_maximum_path(self, dic):
    list_of_paths = []
    if len(dic["depends_on"]) != 0:
      for dependency in dic["depends_on"]:
        # Add to path dependency start and its duration
        list_of_paths.append(self.hf.get_dic_with_name(dependency, self.tasks)["start"] + self.hf.get_dic_with_name(dependency, self.tasks)["duration"])
      return max(list_of_paths)
    else:
      return 0


if __name__ == "__main__":
  hf = Helpful_functions()
  data = Data(hf)
  ac = Additional_calculations(data.tasks)
  
  bc = Bar_chart(data.tasks)
  
  # Needs to be last
  gc = Gantt_chart(data.tasks)
  plt.show()
