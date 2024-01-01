from Gantt_chart import Gantt_chart
from Bar_chart import Bar_chart

import matplotlib.pyplot as plt


class Manual_graph:
  def __init__(self):

    # Example
    self.tasks = [
      dict(name = "A", duration = 1,  depends_on = [],           workers = 2, start = 0, end = 1,   initialised = False),
      dict(name = "B", duration = 1,  depends_on = [],           workers = 3, start = 0, end = 1,   initialised = False),
      dict(name = "C", duration = 1,  depends_on = ["B"],        workers = 2, start = 1, end = 2,   initialised = False),
      dict(name = "D", duration = 1,  depends_on = ["A"],        workers = 2, start = 1, end = 2,   initialised = False),
      dict(name = "E", duration = 1,  depends_on = ["A"],        workers = 4, start = 1, end = 2,   initialised = False),
      dict(name = "F", duration = 1,  depends_on = ["C", "D"],   workers = 2, start = 2, end = 3,   initialised = False)
    ]

    self.prepare_data()

    self.bar_chart = Bar_chart(self.tasks)
    # Supress to not create manual graph
    self.gc = Gantt_chart(self.tasks)

  # Calculates ends based on duration
  def prepare_data(self):
    for dic in self.tasks:
      if dic["end"] == 0:
        dic["end"] = dic["start"] + dic["duration"]

if __name__ == "__main__":
  mg = Manual_graph()
  plt.show()

