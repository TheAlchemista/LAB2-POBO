import matplotlib.pyplot as plt


class Bar_chart:
  def __init__(self, tasks):
    self.tasks = tasks
    self.pbc = Prepare_bar_graph_data(self.tasks)

    self.create_plot()

  def create_plot(self):
    self.set_size()
    bar_graph = plt.bar(self.pbc.x_axis_coordinates, self.pbc.workers_in_sections, width=1 ,align='edge')
    # Set labels
    plt.xticks(self.pbc.x_axis_coordinates, self.pbc.x_axis_coordinates)

    self.annotate(bar_graph)
    plt.title("Liczba pracowników w określonych momentach.")
    plt.show(block=False)
    # plt.show()

  def set_size(self):
    plt.figure(figsize=(12, 7))

  # Makes annotations on top of the graph
  def annotate(self, bar_chart):
    for bar in bar_chart:
      height = bar.get_height()
      plt.annotate('{}'.format(height),
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom')


class Prepare_bar_graph_data:
  def __init__(self, tasks):
    self.tasks = tasks

    self.workers_in_sections = self.get_workers_in_time_section()
    self.x_axis_coordinates = self.get_xaxis_coordinates()

  def get_xaxis_coordinates(self):
    longest_time = self.get_longest_time()
    i = 0
    x_axis_coordinates = []
    while i <= longest_time:
      x_axis_coordinates.append(i)
      i += 1
    return x_axis_coordinates

  def get_workers_in_time_section(self):
    longest_time = self.get_longest_time()
    workers_in_sections = []
    i = 0
    while i <= longest_time:
      workers_in_section = 0
      for task in self.tasks:
        if(i >= task["start"] and i < task["end"]):
          workers_in_section += task["workers"]
      workers_in_sections.append(workers_in_section)
      i+=1
    return workers_in_sections

  def get_longest_time(self):
    longest_time = 0
    for task in self.tasks:
      if (task["end"] > longest_time):
        longest_time = task["end"]
      else:
        pass
    return longest_time

  def delete_last_element(self):
    self.workers_in_sections.pop()
    self.x_axis_coordinates.pop()
