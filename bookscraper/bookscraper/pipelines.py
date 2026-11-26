# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from scrapy.utils.misc import load_object

class BookscraperPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip whitespaces
        for field_name in adapter.field_names():
            if field_name != "description":
                value = adapter.get(field_name)
                if isinstance(value, (list, tuple)):
                    value = value[0] if value else ""
                if isinstance(value, str):
                    adapter[field_name] = value.strip()

        # Category and product type
        for key in ["category", "product_type"]:
            value = adapter.get(key)
            if value:
                adapter[key] = value.lower()

        # Prices
        price_keys = [
            "price",
            "price_excl_tax",
            "price_incl_tax",
            "tax"
        ]

        for key in price_keys:
            value = adapter.get(key) or ""
            value = value.replace("£", "")
            adapter[key] = float(value) if value else 0.0

        # Availability
        availability = adapter.get("availability") or ""
        parts = availability.split("(")
        if len(parts) < 2:
            adapter["availability"] = 0
        else:
            adapter["availability"] = int(parts[1].split()[0])

        # Reviews
        adapter["num_reviews"] = int(
            adapter.get("num_reviews") or 0
        )

        # Stars
        stars = adapter.get("stars") or ""
        star_values = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5
        }
        parts = stars.split()
        if len(parts) > 1:
            adapter["stars"] = star_values.get(
                parts[1].lower(), 0
            )

        return item


class SaveToDatabasePipeline:

    def __init__(self, repository):
        self.repository = repository

    @classmethod
    def from_crawler(cls, crawler):
        # Load repository class from settings
        repository_path = crawler.settings.get(
            "BOOKS_REPOSITORY"
        )
        repository_class = load_object(repository_path)

        # Load repository configuration
        repository_kwargs = crawler.settings.getdict(
            "BOOKS_REPOSITORY_KWARGS"
        )

        # Instantiate concrete repository
        repository = repository_class(**repository_kwargs)

        # Inject dependency
        return cls(repository)

    def process_item(self, item, spider):
        self.repository.save(item)
        return item

    def close_spider(self, spider):
        self.repository.close()


