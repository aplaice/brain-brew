from dataclasses import dataclass
from typing import Optional, Union

from brain_brew.build_tasks.crowd_anki.headers_from_crowdanki import headers_default_values
from brain_brew.representation.build_config.representation_base import RepresentationBase
from brain_brew.representation.yaml.deck_part_holder import DeckPartHolder
from brain_brew.representation.yaml.headers_repr import Headers


@dataclass
class HeadersToCrowdAnki:
    @dataclass
    class Representation(RepresentationBase):
        deck_part: str

    @classmethod
    def from_repr(cls, data: Union[Representation, dict, str]):
        rep: cls.Representation
        if isinstance(data, cls.Representation):
            rep = data
        elif isinstance(data, dict):
            rep = cls.Representation.from_dict(data)
        else:
            rep = cls.Representation(deck_part=data)  # Support single string being passed in

        return cls(
            headers=DeckPartHolder.from_deck_part_pool(rep.deck_part).deck_part,
        )

    headers: Headers

    def execute(self) -> dict:
        headers = self.headers_to_crowd_anki(self.headers.data_without_name)

        return headers

    @staticmethod
    def headers_to_crowd_anki(headers_data: dict):
        return {**headers_default_values, **headers_data}

