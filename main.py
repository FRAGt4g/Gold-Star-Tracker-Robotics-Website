from flask import Flask, render_template, request

app = Flask('app')

class Person:
  score = 0
  name = " "

  def __init__(self, text_data):
    text_data = text_data.replace(" ", "").split("=")
  
    self.name = text_data[0]
    self.score = float(text_data[1])
    if (self.score == int(self.score)):
      self.score = int(self.score)
    


@app.route('/')
def hello_world():
  score_file = open("scores.txt", "r+")
  data = score_file.readlines()
  score_file.close()
  people = []
  for element in data:
    if not element.startswith("//"):
      people.append(Person(text_data=element))

  people.sort(key=lambda x: x.score, reverse=True)
  score_file.close()
  return render_template('index.html', name="Miles", scores=people)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
