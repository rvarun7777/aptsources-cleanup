# -*- coding: utf-8
"""String utilities"""
from __future__ import print_function, division, absolute_import, unicode_literals

__all__ = ('startswith_token',)


def startswith_token(s, prefix, sep=None):
	"""Tests if a string is either equal to a given prefix or prefixed by it
	followed by a separator.
	"""

	if sep is None:
		return s == prefix

	prefix_len = len(prefix)
	return s.startswith(prefix) and (
		not sep or len(s) == len(prefix) or
		s.find(sep, prefix_len, prefix_len + len(sep)) == prefix_len)
