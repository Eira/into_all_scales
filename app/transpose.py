"""This module create the list of scales with pattern with transposed notes."""

from app.models.models_pattern import PatternInKey, PatternInScale, PatternType, RowNotes, TransRowNotes
from app.models.models_scale import ScaleGroup
from app.scale_group import get_scale_group_from_name


def transpose(pattern: PatternType, user_scale_group: set[str] | None = None) -> list[PatternInScale]:
    """
    Transpose pattern all possible scales or to selected one.

    Return list of objects with patterns for all keys of the scale.
    """
    transposed_pattern_list = []
    scale_type_list: set[str] = set()

    if user_scale_group is None:
        scale_type_list = pattern.scale_types
    elif user_scale_group:
        scale_type_list = user_scale_group

    if not scale_type_list:
        raise RuntimeError

    for scale_type in scale_type_list:
        scale_group = get_scale_group_from_name(scale_type)

        transposed_pattern = PatternInScale(
            scale_type_name=scale_group.name,
            pattern_name=pattern.name,
            scales=_create_trans_key_list(scale_group, pattern),
        )

        transposed_pattern_list.append(transposed_pattern)

    return transposed_pattern_list


def _create_trans_quant(quant: str, key_scale: list[str]) -> str:
    """Transpose the quant in scale row to letters notes."""
    trans_note_list = []

    for note in quant:
        trans_note_list.append(key_scale[int(note) - 1])

    return ' '.join(trans_note_list)


def _create_trans_row(row: list[str], key_scale: list[str]) -> TransRowNotes:
    """Gather transposed quants to the row."""
    trans_quant_list = [_create_trans_quant(quant, key_scale) for quant in row]

    return TransRowNotes(
        quants=trans_quant_list,
    )


def _create_trans_row_list(pattern_rows: list[RowNotes], key_scale: list[str]) -> list[TransRowNotes]:
    """Gather transposed rows to lists."""
    return [_create_trans_row(row.quants, key_scale) for row in pattern_rows]


def _create_trans_key_list(scale_group: ScaleGroup, pattern: PatternType) -> list[PatternInKey]:
    """Gather lists of keys with transposed patter."""
    patterned_key_list = []

    for key_scale in scale_group.scales:
        trans_row_list = _create_trans_row_list(pattern.pattern, key_scale.scale)

        patterned_key = PatternInKey(
            key_name=key_scale.name,
            pattern=trans_row_list,
        )
        patterned_key_list.append(patterned_key)

    return patterned_key_list
