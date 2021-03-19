from Gantt_chart import Gantt_chart
from Bar_chart import Bar_chart

import matplotlib.pyplot as plt


class Manual_graph:
  def __init__(self):
    self.tasks = [
      dict(name = "A", duration = 3, depends_on = [],            workers = 2, start = 5, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "B", duration = 5,  depends_on = [],           workers = 3, start = 0, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "C", duration = 10, depends_on = ["B"],        workers = 2, start = 5, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "D", duration = 10,  depends_on = ["A"],       workers = 2, start = 8, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "E", duration = 21,  depends_on = ["A", "B"],  workers = 4, start = 18, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False),
      dict(name = "F", duration = 12,  depends_on = ["C", "D"],  workers = 2, start = 39, end = 0, NWR = 0, NWZ = 0, NPR = 0, NPZ = 0, initialised = False)
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
