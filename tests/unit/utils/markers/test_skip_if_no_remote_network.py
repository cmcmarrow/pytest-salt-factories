# -*- coding: utf-8 -*-
"""
    tests.unit.utils.markers.test_skip_if_no_remote_network
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test the "skip_if_no_remote_network" marker helper
"""
import socket

import mock

import saltfactories.utils.markers as markers


def test_has_remote_network():
    assert markers.skip_if_no_remote_network() is None


def test_no_remote_network():
    mock_socket = mock.MagicMock()
    mock_socket.connect = mock.MagicMock(side_effect=socket.error)
    with mock.patch("socket.socket", return_value=mock_socket):
        skip_reason = markers.skip_if_no_remote_network()
        assert skip_reason is not None
        assert skip_reason == "No internet network connection was detected"
