import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/bar_chart-{name}.png')
  plt.close()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/pie_chart-{name}.png')
  plt.close()
