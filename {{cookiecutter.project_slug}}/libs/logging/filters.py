from loguru import Record


def single_level_filter(record: Record, level: str | int) -> bool:
    """Filter logs by level name or numeric value"""
    try:
        if isinstance(level, str):
            return record["level"].name == level.upper()
        return record["level"].no == level
    except (KeyError, AttributeError):
        return False
