# How to use:

Find a constructor (`__init__`) and insert your data to list of dictionaries called 
```
self.tasks
```
Every dictionary is a task.
Parameters:
- name - task name (used by depends_on)
- duration - task duration
- depends_on - list of task dependencies (tasks that need to be complieted before this task can start)
- workers - number of people working on that task, used by bar graph

## What files to run:
- File `Data.py`
    - if you want the program to calculate starts and ends of tasks execution automatically
    - tasks start in the earliest time possible
- File `Manual_graph.py`
    - allows setting custom start times
    - only creates gant chart and bar chart
    - does not do calcualtions