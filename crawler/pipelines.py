class ItemCollectorPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        with open('response.txt', 'w') as file:
            file.write(item['body'])
