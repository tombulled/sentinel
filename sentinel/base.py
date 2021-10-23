import enum

sentinel = enum.auto

class Sentinel(enum.Enum):
    def _generate_next_value_(name: str, *_) -> str:
        return name

    def __str__(self) -> str:
        return f'<{self.value}>'

    def __repr__(self) -> str:
        return f'<{self.value}>'
