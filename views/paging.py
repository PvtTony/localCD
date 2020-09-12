class Page(object):
    def __init__(self):
        self.data = []
        self.total = 0
        self.current_page = 1
        self.page_size = 0

    @property
    def total_pages(self):
        return self.total // self.page_size + 1


class PageRequest(object):
    def __init__(self):
        self.page = 1
        self.page_size = 0

    @property
    def limit(self):
        return self.page_size

    @property
    def offset(self):
        return (self.page - 1) * self.page_size
