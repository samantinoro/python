import pytest
from television import Television  # Assuming your Television class is in a file named television.py


def test_init():
    tv = Television()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'


def test_power():
    tv = Television()
    # power on
    tv.power()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    # power off
    tv.power()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'


def test_mute():
    tv = Television()
    tv.power()

    # on, volume up, then mute
    tv.volume_up()
    tv.mute()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    # on and unmuted
    tv.mute()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    # off and muted
    tv.power()
    tv.mute()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    # off and unmuted
    tv.mute()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'


def test_channel_up():
    tv = Television()

    # off, channel increased
    tv.volume_up()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    # on, channel increased
    tv.power()
    tv.channel_up()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL + 1}, Volume = {Television.MIN_VOLUME}'

    # on, increased past maximum channel
    while str(tv) != f'Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}':
        tv.channel_up()
    tv.channel_up()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'


def test_channel_down():
    tv = Television()

    # off, channel decreased
    tv.channel_down()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    # on, decreased past minimum
    tv.power()
    tv.channel_down()
    assert str(tv) == f'Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}'


def test_volume_up():
    tv = Television()

    # off, volume increased
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    #on, volume increased
    tv.power()
    tv.volume_up()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME + 1}'

    # on, muted, volume increased
    tv.mute()
    tv.volume_up()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME + 2}'


    # on, volume incrased past maximum
    while str(tv) != f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}':
        tv.volume_up()
    tv.volume_up()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}'




def test_volume_down():
    tv = Television()

    # off, volume decreased
    tv.volume_down()
    assert str(tv) == f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'

    # (increase volume to maximum)
    tv.power()
    while str(tv) != f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}':
        tv.volume_up()

    # on, volume decreased
    tv.volume_down()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME - 1}'

    # on, muted, volume decreased
    tv.mute()
    tv.volume_down()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME + 1}'

    # on, volume decreased past negative
    while str(tv) != f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}':
        tv.volume_down()
    tv.volume_down()
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}'
