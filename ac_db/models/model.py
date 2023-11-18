import dataclasses
import inspect


@dataclasses.dataclass
class Model:
    @classmethod
    def from_dict(cls, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return cls(**{
            k: v for k, v in kwargs.items() if k in inspect.signature(cls).parameters
        })

    def to_dict(self):
        """

        :return:
        """
        return dict(dataclasses.asdict(self).items())
