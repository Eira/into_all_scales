from typing import List

from app.models.models_pattern import PatternInKey, PatternInScale, RowNotes, TransRowNotes
from app.models.models_scale import Key, ScaleGroup
from app.transpose import (_create_trans_quant, _create_trans_row,
                           _create_trans_row_list, transpose, _create_trans_key_list)


def test_create_trans_quant_smoke():
    quant = '234'
    key_scale = ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'B', 'C']

    res = _create_trans_quant(quant, key_scale)

    assert res is not None


def test_create_trans_row_smoke():
    row = ['123', '234', '345', '456', '567', '678']
    key_scale = ['Cb', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = _create_trans_row(row, key_scale)

    assert res is not None


def test_create_trans_row_list_smoke():
    pattern_rows = [RowNotes(quants=['123', '234', '345', '456', '567', '678']), RowNotes(quants=['765', '654', '543', '432', '321'])]
    key_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = _create_trans_row_list(pattern_rows, key_scale)

    assert res is not None


def test_create_trans_key_list_smoke(fixture_test_pattern):
    scale_group = ScaleGroup(name='Major', scales=[Key(name='C', scale=['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']), Key(name='Db', scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db']), Key(name='D', scale=['D', 'E', 'Gb', 'G', 'A', 'B', 'Db', 'D']), Key(name='Eb', scale=['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb']), Key(name='E', scale=['E', 'Gb', 'Ab', 'A', 'B', 'Db', 'Eb', 'E']), Key(name='F', scale=['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F']), Key(name='Gb', scale=['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F', 'Gb']), Key(name='G', scale=['G', 'A', 'B', 'C', 'D', 'E', 'Gb', 'G']), Key(name='Ab', scale=['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab']), Key(name='A', scale=['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab', 'A']), Key(name='Bb', scale=['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb']), Key(name='B', scale=['B', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'B'])])
    res = _create_trans_key_list(scale_group, fixture_test_pattern)

    assert res == [PatternInKey(key_name='C',
              pattern=[TransRowNotes(quants=['C D E',
                                             'D E F',
                                             'E F G',
                                             'F G A',
                                             'G A B',
                                             'A B C']),
                       TransRowNotes(quants=['B A G',
                                             'A G F',
                                             'G F E',
                                             'F E D',
                                             'E D C'])]),
 PatternInKey(key_name='Db',
              pattern=[TransRowNotes(quants=['Db Eb F',
                                             'Eb F Gb',
                                             'F Gb Ab',
                                             'Gb Ab Bb',
                                             'Ab Bb C',
                                             'Bb C Db']),
                       TransRowNotes(quants=['C Bb Ab',
                                             'Bb Ab Gb',
                                             'Ab Gb F',
                                             'Gb F Eb',
                                             'F Eb Db'])]),
 PatternInKey(key_name='D',
              pattern=[TransRowNotes(quants=['D E Gb',
                                             'E Gb G',
                                             'Gb G A',
                                             'G A B',
                                             'A B Db',
                                             'B Db D']),
                       TransRowNotes(quants=['Db B A',
                                             'B A G',
                                             'A G Gb',
                                             'G Gb E',
                                             'Gb E D'])]),
 PatternInKey(key_name='Eb',
              pattern=[TransRowNotes(quants=['Eb F G',
                                             'F G Ab',
                                             'G Ab Bb',
                                             'Ab Bb C',
                                             'Bb C D',
                                             'C D Eb']),
                       TransRowNotes(quants=['D C Bb',
                                             'C Bb Ab',
                                             'Bb Ab G',
                                             'Ab G F',
                                             'G F Eb'])]),
 PatternInKey(key_name='E',
              pattern=[TransRowNotes(quants=['E Gb Ab',
                                             'Gb Ab A',
                                             'Ab A B',
                                             'A B Db',
                                             'B Db Eb',
                                             'Db Eb E']),
                       TransRowNotes(quants=['Eb Db B',
                                             'Db B A',
                                             'B A Ab',
                                             'A Ab Gb',
                                             'Ab Gb E'])]),
 PatternInKey(key_name='F',
              pattern=[TransRowNotes(quants=['F G A',
                                             'G A Bb',
                                             'A Bb C',
                                             'Bb C D',
                                             'C D E',
                                             'D E F']),
                       TransRowNotes(quants=['E D C',
                                             'D C Bb',
                                             'C Bb A',
                                             'Bb A G',
                                             'A G F'])]),
 PatternInKey(key_name='Gb',
              pattern=[TransRowNotes(quants=['Gb Ab Bb',
                                             'Ab Bb B',
                                             'Bb B Db',
                                             'B Db Eb',
                                             'Db Eb F',
                                             'Eb F Gb']),
                       TransRowNotes(quants=['F Eb Db',
                                             'Eb Db B',
                                             'Db B Bb',
                                             'B Bb Ab',
                                             'Bb Ab Gb'])]),
 PatternInKey(key_name='G',
              pattern=[TransRowNotes(quants=['G A B',
                                             'A B C',
                                             'B C D',
                                             'C D E',
                                             'D E Gb',
                                             'E Gb G']),
                       TransRowNotes(quants=['Gb E D',
                                             'E D C',
                                             'D C B',
                                             'C B A',
                                             'B A G'])]),
 PatternInKey(key_name='Ab',
              pattern=[TransRowNotes(quants=['Ab Bb C',
                                             'Bb C Db',
                                             'C Db Eb',
                                             'Db Eb F',
                                             'Eb F G',
                                             'F G Ab']),
                       TransRowNotes(quants=['G F Eb',
                                             'F Eb Db',
                                             'Eb Db C',
                                             'Db C Bb',
                                             'C Bb Ab'])]),
 PatternInKey(key_name='A',
              pattern=[TransRowNotes(quants=['A B Db',
                                             'B Db D',
                                             'Db D E',
                                             'D E Gb',
                                             'E Gb Ab',
                                             'Gb Ab A']),
                       TransRowNotes(quants=['Ab Gb E',
                                             'Gb E D',
                                             'E D Db',
                                             'D Db B',
                                             'Db B A'])]),
 PatternInKey(key_name='Bb',
              pattern=[TransRowNotes(quants=['Bb C D',
                                             'C D Eb',
                                             'D Eb F',
                                             'Eb F G',
                                             'F G A',
                                             'G A Bb']),
                       TransRowNotes(quants=['A G F',
                                             'G F Eb',
                                             'F Eb D',
                                             'Eb D C',
                                             'D C Bb'])]),
 PatternInKey(key_name='B',
              pattern=[TransRowNotes(quants=['B Db Eb',
                                             'Db Eb E',
                                             'Eb E Gb',
                                             'E Gb Ab',
                                             'Gb Ab Bb',
                                             'Ab Bb B']),
                       TransRowNotes(quants=['Bb Ab Gb',
                                             'Ab Gb E',
                                             'Gb E Eb',
                                             'E Eb Db',
                                             'Eb Db B'])])]


def test_transpose_happy_path(fixture_test_pattern):
    res = transpose(fixture_test_pattern)

    assert isinstance(res, List)
    assert isinstance(res[0], PatternInScale)
    assert res[0].scale_type_name == 'Major'
    assert res[1].scale_type_name == 'Natural minor'
    assert res[0].pattern_name == 'Triplets'
    assert res[0].scales == [PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['C D E', 'D E F', 'E F G', 'F G A', 'G A B', 'A B C']), TransRowNotes(quants=['B A G', 'A G F', 'G F E', 'F E D', 'E D C'])]), PatternInKey(key_name='Db', pattern=[TransRowNotes(quants=['Db Eb F', 'Eb F Gb', 'F Gb Ab', 'Gb Ab Bb', 'Ab Bb C', 'Bb C Db']), TransRowNotes(quants=['C Bb Ab', 'Bb Ab Gb', 'Ab Gb F', 'Gb F Eb', 'F Eb Db'])]), PatternInKey(key_name='D', pattern=[TransRowNotes(quants=['D E Gb', 'E Gb G', 'Gb G A', 'G A B', 'A B Db', 'B Db D']), TransRowNotes(quants=['Db B A', 'B A G', 'A G Gb', 'G Gb E', 'Gb E D'])]), PatternInKey(key_name='Eb', pattern=[TransRowNotes(quants=['Eb F G', 'F G Ab', 'G Ab Bb', 'Ab Bb C', 'Bb C D', 'C D Eb']), TransRowNotes(quants=['D C Bb', 'C Bb Ab', 'Bb Ab G', 'Ab G F', 'G F Eb'])]), PatternInKey(key_name='E', pattern=[TransRowNotes(quants=['E Gb Ab', 'Gb Ab A', 'Ab A B', 'A B Db', 'B Db Eb', 'Db Eb E']), TransRowNotes(quants=['Eb Db B', 'Db B A', 'B A Ab', 'A Ab Gb', 'Ab Gb E'])]), PatternInKey(key_name='F', pattern=[TransRowNotes(quants=['F G A', 'G A Bb', 'A Bb C', 'Bb C D', 'C D E', 'D E F']), TransRowNotes(quants=['E D C', 'D C Bb', 'C Bb A', 'Bb A G', 'A G F'])]), PatternInKey(key_name='Gb', pattern=[TransRowNotes(quants=['Gb Ab Bb', 'Ab Bb B', 'Bb B Db', 'B Db Eb', 'Db Eb F', 'Eb F Gb']), TransRowNotes(quants=['F Eb Db', 'Eb Db B', 'Db B Bb', 'B Bb Ab', 'Bb Ab Gb'])]), PatternInKey(key_name='G', pattern=[TransRowNotes(quants=['G A B', 'A B C', 'B C D', 'C D E', 'D E Gb', 'E Gb G']), TransRowNotes(quants=['Gb E D', 'E D C', 'D C B', 'C B A', 'B A G'])]), PatternInKey(key_name='Ab', pattern=[TransRowNotes(quants=['Ab Bb C', 'Bb C Db', 'C Db Eb', 'Db Eb F', 'Eb F G', 'F G Ab']), TransRowNotes(quants=['G F Eb', 'F Eb Db', 'Eb Db C', 'Db C Bb', 'C Bb Ab'])]), PatternInKey(key_name='A', pattern=[TransRowNotes(quants=['A B Db', 'B Db D', 'Db D E', 'D E Gb', 'E Gb Ab', 'Gb Ab A']), TransRowNotes(quants=['Ab Gb E', 'Gb E D', 'E D Db', 'D Db B', 'Db B A'])]), PatternInKey(key_name='Bb', pattern=[TransRowNotes(quants=['Bb C D', 'C D Eb', 'D Eb F', 'Eb F G', 'F G A', 'G A Bb']), TransRowNotes(quants=['A G F', 'G F Eb', 'F Eb D', 'Eb D C', 'D C Bb'])]), PatternInKey(key_name='B', pattern=[TransRowNotes(quants=['B Db Eb', 'Db Eb E', 'Eb E Gb', 'E Gb Ab', 'Gb Ab Bb', 'Ab Bb B']), TransRowNotes(quants=['Bb Ab Gb', 'Ab Gb E', 'Gb E Eb', 'E Eb Db', 'Eb Db B'])])]


def test_transpose_user_scales_happy_path(fixture_test_pattern):
    scale_group_list = ['Natural minor', 'Major']

    res = transpose(fixture_test_pattern, scale_group_list)

    assert isinstance(res, List)
    assert isinstance(res[0], PatternInScale)
    assert res[0].scale_type_name == 'Natural minor'
    assert res[1].scale_type_name == 'Major'
    assert res[0].pattern_name == 'Triplets'
    assert res[1].scales == [PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['C D E', 'D E F', 'E F G', 'F G A', 'G A B', 'A B C']), TransRowNotes(quants=['B A G', 'A G F', 'G F E', 'F E D', 'E D C'])]), PatternInKey(key_name='Db', pattern=[TransRowNotes(quants=['Db Eb F', 'Eb F Gb', 'F Gb Ab', 'Gb Ab Bb', 'Ab Bb C', 'Bb C Db']), TransRowNotes(quants=['C Bb Ab', 'Bb Ab Gb', 'Ab Gb F', 'Gb F Eb', 'F Eb Db'])]), PatternInKey(key_name='D', pattern=[TransRowNotes(quants=['D E Gb', 'E Gb G', 'Gb G A', 'G A B', 'A B Db', 'B Db D']), TransRowNotes(quants=['Db B A', 'B A G', 'A G Gb', 'G Gb E', 'Gb E D'])]), PatternInKey(key_name='Eb', pattern=[TransRowNotes(quants=['Eb F G', 'F G Ab', 'G Ab Bb', 'Ab Bb C', 'Bb C D', 'C D Eb']), TransRowNotes(quants=['D C Bb', 'C Bb Ab', 'Bb Ab G', 'Ab G F', 'G F Eb'])]), PatternInKey(key_name='E', pattern=[TransRowNotes(quants=['E Gb Ab', 'Gb Ab A', 'Ab A B', 'A B Db', 'B Db Eb', 'Db Eb E']), TransRowNotes(quants=['Eb Db B', 'Db B A', 'B A Ab', 'A Ab Gb', 'Ab Gb E'])]), PatternInKey(key_name='F', pattern=[TransRowNotes(quants=['F G A', 'G A Bb', 'A Bb C', 'Bb C D', 'C D E', 'D E F']), TransRowNotes(quants=['E D C', 'D C Bb', 'C Bb A', 'Bb A G', 'A G F'])]), PatternInKey(key_name='Gb', pattern=[TransRowNotes(quants=['Gb Ab Bb', 'Ab Bb B', 'Bb B Db', 'B Db Eb', 'Db Eb F', 'Eb F Gb']), TransRowNotes(quants=['F Eb Db', 'Eb Db B', 'Db B Bb', 'B Bb Ab', 'Bb Ab Gb'])]), PatternInKey(key_name='G', pattern=[TransRowNotes(quants=['G A B', 'A B C', 'B C D', 'C D E', 'D E Gb', 'E Gb G']), TransRowNotes(quants=['Gb E D', 'E D C', 'D C B', 'C B A', 'B A G'])]), PatternInKey(key_name='Ab', pattern=[TransRowNotes(quants=['Ab Bb C', 'Bb C Db', 'C Db Eb', 'Db Eb F', 'Eb F G', 'F G Ab']), TransRowNotes(quants=['G F Eb', 'F Eb Db', 'Eb Db C', 'Db C Bb', 'C Bb Ab'])]), PatternInKey(key_name='A', pattern=[TransRowNotes(quants=['A B Db', 'B Db D', 'Db D E', 'D E Gb', 'E Gb Ab', 'Gb Ab A']), TransRowNotes(quants=['Ab Gb E', 'Gb E D', 'E D Db', 'D Db B', 'Db B A'])]), PatternInKey(key_name='Bb', pattern=[TransRowNotes(quants=['Bb C D', 'C D Eb', 'D Eb F', 'Eb F G', 'F G A', 'G A Bb']), TransRowNotes(quants=['A G F', 'G F Eb', 'F Eb D', 'Eb D C', 'D C Bb'])]), PatternInKey(key_name='B', pattern=[TransRowNotes(quants=['B Db Eb', 'Db Eb E', 'Eb E Gb', 'E Gb Ab', 'Gb Ab Bb', 'Ab Bb B']), TransRowNotes(quants=['Bb Ab Gb', 'Ab Gb E', 'Gb E Eb', 'E Eb Db', 'Eb Db B'])])]
