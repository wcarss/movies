class Movie(object):
    @classmethod
    def load(cls, config):
        return Movie(
            config.get('title'),
            config.get('cost'),
            config.get('revenue'),
            config.get('count', 0),
            config.get('sources', None)
        )

    def __init__(self, title, cost, revenue, count=0, sources=None):
        self.title = title
        self.name = title
        self.cost = cost
        self.revenue = revenue
        self.count = count
        if sources is None:
            sources = []
        self.sources = sources

    def __str__(self):
        return "{title}, expecting {revenue}, {cost}/screen".format(
            title=self.title,
            cost=self.cost,
            revenue=self.revenue
        )

    def total_revenue(self):
        return self.revenue * self.count

    def total_cost(self):
        return self.cost * self.count

    def add_source(self, source):
        self.sources.append(source)

    def sources(self):
        return self.sources
