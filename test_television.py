import pytest
from television import Television  # Assuming your Television class is in a file named television.py


def test_init():
    tv = Television()
    assert str(tv) == f'Power = False, Channel = 0, Volume = 0'


def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == f'Power = True, Channel = 0, Volume = 0'

    tv.power()
    assert str(tv) == f'Power = False, Channel = 0, Volume = 0'


def test_mute():
    tv = Television()
    tv.power()
    # on, volume up, then mute
    tv.volume_up()
    tv.mute()
    assert str(tv) == f'Power = True, Channel = 0, Volume = 0'

    # on and unmuted
    tv.mute()
    assert str(tv) == f'Power = True, Channel = 0, Volume = 0'

    # off and muted
    tv.power()
    tv.mute()
    assert str(tv) == f'Power = False, Channel = 0, Volume = 0'

    # off and unmuted
    tv.mute()
    assert str(tv) == f'Power = False, Channel = 0, Volume = 0'


def test_channel_up():
    tv = Television()

    # off, channel increased
    tv.volume_up()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = 0'

    # on, channel increased
    tv.power()
    tv.channel_up()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL + 1}, Volume = 0'

    # on, increased past maximum channel
    while str(tv) != f'Power = True, Channel = {Television.MAX_CHANNEL}, Volume = 0':
        tv.channel_up()
    tv.channel_up()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0'


def test_channel_down():
    tv = Television()

    # off, channel decreased
    tv.channel_down()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = 0'

    # on, decreased past minimum
    tv.power()
    tv.channel_down()
    assert str(tv) == f'Power = True, Channel = {Television.MAX_CHANNEL}, Volume = 0'

    # on, decreased from maximum to minimum channel (extra check)
    while str(tv) != f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0':
        tv.channel_down()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0'


def test_volume_up():
    tv = Television()

    # off, volume increased
    assert str(tv) == f'Power = False, Channel = 0, Volume = {Television.MIN_VOLUME}'

    #on, volume increased
    tv.power()
    tv.volume_up()
    assert str(tv) == f'Power = True, Channel = 0, Volume = {Television.MIN_VOLUME + 1}'

    # on, muted, volume increased
    tv.mute()
    tv.volume_up()
    assert str(tv) == f'Power = True, Channel = 0, Volume = {Television.MIN_VOLUME + 2}'


    # checks that it can reach the maximum
    while str(tv) != f'Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}':
        tv.volume_up()
    assert str(tv) == f'Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}'

    # checks that it can go up but not past
    for i in range(3):
        tv.volume_up()
    assert str(tv) == f'Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}'


def test_volume_down():
    tv = Television()
    tv.power()

    # turn all the way up, then check that it can go down
    while str(tv) != f'Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}':
        tv.volume_up()
    while str(tv) != f'Power = True, Channel = 0, Volume = {Television.MIN_VOLUME}':
        tv.volume_down()
    assert str(tv) == f'Power = True, Channel = 0, Volume = 0'

    # makes sure it cannot go negative
    tv.volume_down()
    assert str(tv) == f'Power = True, Channel = 0, Volume = 0'
