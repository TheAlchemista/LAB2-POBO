from datetime import datetime
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
import plotly.express as px


class Gantt_chart:

  def __init__(self, tasks):
    self.tasks = tasks
    self.figure()

  # Converts to datetime
  def to_dt(self, x):
    return datetime.fromtimestamp(31536000+x*24*3600).strftime("%Y-%m-%d")

  def prepare_data(self):
    for dic in self.tasks:
      dic["start"] = self.to_dt(dic["start"])
      dic["end"] = self.to_dt(dic["end"])
    return self.tasks

  def get_labels(self):
    return np.linspace(start = 0, stop = 100, num = 110, dtype = int)

  def get_tics(self, num_tick_labels):
    return [self.to_dt(x) for x in num_tick_labels]

  def figure(self):
    df = self.prepare_data()
    fig = px.timeline(df, x_start="start", x_end="end", y="name", color="name",
        labels = {
            "name": "Operacje"
        })
    fig.update_layout(xaxis_title="Czas") #to add a title to xaxis
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    num_tick_labels = self.get_labels()
    date_ticks = self.get_tics(num_tick_labels)
    fig.update_xaxes({
      'tickvals' : date_ticks,
      'ticktext' : num_tick_labels
      })
    fig.show()
