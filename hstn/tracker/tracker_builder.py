from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from hstn.core.config import cfg
from hstn.tracker.hstn_tracker import HSTNTracker

TRACKS = {
          'HSTNTracker': HSTNTracker
         }


def build_tracker(model):
    return TRACKS[cfg.TRACK.TYPE](model)
