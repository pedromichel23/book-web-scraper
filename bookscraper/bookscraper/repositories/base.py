
from abc import ABC, abstractmethod


class BooksRepository(ABC):

    @abstractmethod
    def save(self, item):
        """Save a book."""
        pass

    @abstractmethod
    def close(self):
        """Close database connection."""
        pass
