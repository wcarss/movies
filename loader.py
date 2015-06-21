from movie import Movie
import json

def main():
  ms = load()

def total(movies):
  total_revenue = 0
  total_cost = 0
  for movie in movies:
    total_revenue += movie.revenue * movie.count
    total_cost += movie.cost * movie.count

  return {'revenue': total_revenue, 'cost': total_cost}


def counts(movies):
  local_movies = movies[:]
  local_movies.sort(key=lambda x: -x.cost)
  for movie in local_movies:
    print "{name}: {count} at {cost},  making {revenue},  yielding  ${total_revenue},  costing ${total_cost}".format(
      name=movie.name.rjust(25, " "),
      count=str(movie.count).ljust(2),
      total_revenue=str(movie.revenue*movie.count).rjust(4),
      total_cost=str(movie.cost*movie.count).rjust(4),
      cost=str(movie.cost).rjust(3),
      revenue=str(movie.revenue).rjust(3)
    )


def load(fn=None):
  if fn == None:
    print "filename required."
    return
  else:
    with open(fn, "r") as f:
      try:
        movies = json.load(f)['movies']
      except KeyError:
        print "json file must have a top level key 'movies'"
        return

  accessor = {}
  ms = []
  for m in movies:
     ms.append(Movie.load(m))
     accessor[m['title']] = ms[-1]

  calculate(ms)
  return ms, accessor


def calculate(ms):
  counts(ms)
  totals = total(ms)
  print "Totalling: ${revenue} revenue, costing ${cost}".format(
    revenue=totals['revenue'],
    cost=totals['cost']
  ).rjust(25, " ")

def write(ms):
  name = raw_input("Please enter a filename: ")
  json_ms = []
  for m in ms:
    json_m = {
      'title': m.title,
      'revenue': m.revenue,
      'cost': m.cost,
      'count': m.count
    }
    json_ms.append(json_m)

  with open(name, "w") as f:
    f.write(json.dumps({'movies': json_ms}, indent=4))

if __name__ == "__main__":
  main()


m, a = load("june_19th.json")
