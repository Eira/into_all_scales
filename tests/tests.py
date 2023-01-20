from index import get_scales_group, get_pattern, get_scale_formula, main, create_pattern, get_scale_group_from_name
from models import ScaleGroup, Key, Pattern, ScaleFormula, RowNotes


def test_create_pattern_happy_path():
    pattern_name = 'test pattern'
    scale_types = 'scale 1,scale 2'  # todo решить проблему с пробелами
    pattern = '123,24,5 5,42,321'

    res = create_pattern(pattern_name, scale_types, pattern)

    assert res == Pattern(
        name='test pattern',
        scale_types=['scale 1', 'scale 2'],
        pattern=[
            RowNotes(
                quants=['123', '24', '5'],
            ),
            RowNotes(
                quants=['5', '42', '321'],
            ),
        ],
    )


def test_get_pattern():
    pattern_name = 'test scale'

    res = get_pattern(pattern_name)

    assert res == Pattern(
        name='test scale',
        scale_types=['scale 1', 'scale 2'],
        pattern=[
            RowNotes(
                quants=['123', '24', '5'],
            ),
            RowNotes(
                quants=['5', '42', '321'],
            ),
        ]
    )


def test_get_scale_formula():
    scale_name = 'minor'

    res = get_scale_formula(scale_name)

    assert res == ScaleFormula(
        name='minor',
        formula=[2, 1, 2, 2, 1, 2, 2],
    )


def test_get_scales_group_happy_path():
    scale_formula = ScaleFormula(
        name='major',
        formula=[2, 2, 1, 2, 2, 2, 1],
    )
    res = get_scales_group(scale_formula)

    assert res == ScaleGroup(
        name='major',
        scales=[
            Key(
                name='C',
                scale=['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
            ),
            Key(
                name='Db',
                scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'],
            ),
            Key(
                name='D',
                scale=['D', 'E', 'Gb', 'G', 'A', 'B', 'Db', 'D'],
            ),
            Key(
                name='Eb',
                scale=['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'],
            ),
            Key(
                name='E',
                scale=['E', 'Gb', 'Ab', 'A', 'B', 'Db', 'Eb', 'E'],
            ),
            Key(
                name='F',
                scale=['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F'],
            ),
            Key(
                name='Gb',
                scale=['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F', 'Gb'],
            ),
            Key(
                name='G',
                scale=['G', 'A', 'B', 'C', 'D', 'E', 'Gb', 'G'],
            ),
            Key(
                name='Ab',
                scale=['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'],
            ),
            Key(
                name='A',
                scale=['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab', 'A'],
            ),
            Key(
                name='Bb',
                scale=['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
            ),
            Key(
                name='B',
                scale=['B', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'B'],
            ),
        ]
    )


def test_get_scale_group_from_name_smoke():
    scale_name = 'minor'
    res = get_scale_group_from_name(scale_name)

    assert res is not None


def test_main_smoke():
    pattern_name = 'Pattern Up and down'
    main(pattern_name)
