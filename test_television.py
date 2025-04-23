import unittest
from television import *

class TestTelevision(unittest.TestCase):
    def test_init(self):
        tv = Television()
        self.assertEqual(tv._Television__status, False)
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL)
        self.assertEqual(tv._Television__volume, Television.MIN_VOLUME)
        tv.power()
    def test_power(self):
        tv = Television()
        self.assertFalse(tv._Television__status, False)
        tv.power()
        self.assertTrue(tv._Television__status, True)
    def test_mute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        self.assertEqual(tv._Television__volume, 1)
        tv.mute()
        self.assertEqual(tv._Television__volume, 0)
        tv.mute()
        self.assertEqual(tv._Television__volume, 1)
    def test_chan(self):
        tv = Television()
        tv.power()
        self.assertEqual(tv._Television__channel, Television.MIN_CHANNEL)
        tv.channel_up()
        self.assertEqual(tv._Television__channel, 1)
        tv.channel_down()
        self.assertEqual(tv._Television__channel, 0)
    def test_vol(self):
        tv = Television()
        tv.power()
        self.assertEqual(tv._Television__volume, Television.MIN_VOLUME)
        tv.volume_up()
        self.assertEqual(tv._Television__volume, 1)
        tv.volume_down()
        self.assertEqual(tv._Television__volume, 0)
