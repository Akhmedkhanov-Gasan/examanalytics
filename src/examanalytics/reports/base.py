from abc import ABC, abstractmethod


class BaseReport(ABC):
    """
    Base class for all reports.
    """

    name: str

    @abstractmethod
    def generate(
        self,
        rows: list[dict[str, str]],
    ) -> list[tuple[str, int | float]]:
        """
        Generate report data.
        """
        raise NotImplementedError
