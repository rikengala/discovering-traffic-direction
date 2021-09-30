"""
This is a dummy file for HW5 of CSE353 Machine Learning, Fall 2020
You need to provide implementation for this file

By: Minh Hoai Nguyen (minhhoai@cs.stonybrook.edu)
Created: 26-Oct-2020
Last modified: 26-Oct-2020
"""

import random


class TrackletClustering(object):
    """
    You need to implement the methods of this class.
    Do not change the signatures of the methods
    """

    def __init__(self, num_cluster):
        self.num_cluster = num_cluster

    def add_tracklet(self, tracklet):
        "Add a new tracklet into the database"
        pass

    def build_clustering_model(self):
        "Perform clustering algorithm"
        pass

    def get_cluster_id(self, tracklet):
        """
        Assign the cluster ID for a tracklet. This funciton must return a non-negative integer <= num_cluster
        It is possible to return value 0, but it is reserved for special category of abnormal behavior (for Question 2.3)
        """

        return random.randint(0, self.num_cluster)
