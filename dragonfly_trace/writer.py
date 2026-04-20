# coding=utf-8
"""Methods to write Dragonfly Models to Trane TRACE."""
from __future__ import division


def model_to_trace_700_matrix(
    model, use_multiplier=True, exclude_plenums=False, merge_method=None,
    si_units=False
):
    """Generate a CSV matrix with TRACE 700 load simulation attributes of a Model.

    The resulting matrix can be written to a CSV and then copied into
    the tables that appear in the Component Tree view of TRACE 700. The
    order and organization of rooms in the resulting matrix should match that
    of the gbXML produced from the same model.

    Args:
        model: A dragonfly Model for which a TRACE 700 CSV matrix will be returned.
        use_multiplier: If True, the multipliers on this Model's Stories will be
            passed along to the CSV. If False, full geometry objects will be written
            for each and every floor in the building that are represented through
            multipliers and all resulting multipliers will be 1. (Default: True).
        exclude_plenums: Boolean to indicate whether ceiling/floor plenum depths
            assigned to Room2Ds should be ignored during translation. This
            results in each Room2D translating to a single Honeybee Room at
            the full floor_to_ceiling_height instead of a base Room with (a)
            plenum Room(s). (Default: False).
        merge_method: An optional text string to describe how the Room2Ds should
            be merged into individual Rooms during the translation. Specifying a
            value here can be an effective way to reduce the number of Room
            volumes in the resulting model and, ultimately, yield a faster
            simulation time in the destination engine with fewer results
            to manage. Note that Room2Ds will only be merged if they form a
            continuous volume. Otherwise, there will be multiple Rooms per
            zone or story, each with an integer added at the end of their
            identifiers. Choose from the following options:

            * None - No merging of Room2Ds will occur
            * Zones - Room2Ds in the same zone will be merged
            * PlenumZones - Only plenums in the same zone will be merged
            * Stories - Rooms in the same story will be merged
            * PlenumStories - Only plenums in the same story will be merged
        
        si_units: Boolean to note whether the units of the values in the resulting
            matrix are in SI (True) instead of IP (False). (Default: False).
    """
