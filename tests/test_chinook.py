import pytest
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, not_
from sqlalchemy.orm import Session

URI = "sqlite:///../chinook.sqlite"


@pytest.fixture(scope='module')
def engine():
    engine = create_engine(URI, echo=False)
    yield engine


@pytest.fixture(scope='module')
def base(engine):
    base = automap_base()
    base.prepare(engine, reflect=True)
    yield base


@pytest.fixture(scope='module')
def session(engine):
    session = Session(engine)
    yield session
    session.close()


@pytest.fixture(scope='module')
def Genre(base):
    return base.classes.Genre


@pytest.fixture(scope='module')
def Track(base):
    return base.classes.Track


@pytest.mark.parametrize('table',
                         ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType',
                          'Playlist', 'PlaylistTrack', 'Track'])
def test_check_if_all_tables_exist(table, engine):
    assert table in engine.table_names(), f'Table {table} is not in DB.'


def test_if_nr_of_rows_in_ciselnik_genre_is_25(session, Genre):
    assert session.query(Genre).count() == 25


def test_if_every_track_has_valid_genre_specified(session, Track):
    assert session.query(Track).filter(
        not_(Track.GenreId.between(1, 25))).count() == 0, f'There is track with wrong genre id'
