"""
This is a dummy file for HW5 of CSE353 Machine Learning, Fall 2020
You need to provide implementation for this file

By: Minh Hoai Nguyen (minhhoai@cs.stonybrook.edu)
Created: 26-Oct-2020
Last modified: 26-Oct-2020
"""

import random
import numpy as np
from sklearn.cluster import KMeans
class TrackletClustering(object):
    """
    You need to implement the methods of this class.
    Do not change the signatures of the methods
    """

    def __init__(self, num_cluster):
        self.num_cluster = num_cluster
        self.database = []
        self.model = 0
    def add_tracklet(self, tracklet):
        "Add a new tracklet into the database"
        tracks = tracklet['tracks']
        first_track = tracks[0]
        first_track_center = [(first_track[1] + first_track[3]) / 2, (first_track[2] + first_track[4]) / 2]
        last_track = tracks[-1]
        last_track_center = [(last_track[1] + last_track[3]) / 2, (last_track[2] + last_track[4]) / 2]
        tracklet_representation = np.concatenate((first_track_center, last_track_center))
        self.database.append(tracklet_representation)
        pass

    def build_clustering_model(self):
        "Perform clustering algorithm"
        # print(self.database)
        X = np.array(self.database)
        # print(X)
        self.model = KMeans(n_clusters=self.num_cluster, random_state=0).fit(X)
        pass

    def get_cluster_id(self, tracklet):
        """
        Assign the cluster ID for a tracklet. This funciton must return a non-negative integer <= num_cluster
        It is possible to return value 0, but it is reserved for special category of abnormal behavior (for Question 2.3)
        """
        tracks = tracklet['tracks']
        first_track = tracks[0]
        first_track_center = [(first_track[1] + first_track[3]) / 2, (first_track[2] + first_track[4]) / 2]
        last_track = tracks[-1]
        last_track_center = [(last_track[1] + last_track[3]) / 2, (last_track[2] + last_track[4]) / 2]
        tracklet_representation = np.concatenate((first_track_center, last_track_center))
        X = np.array([tracklet_representation])
        cluster_id = self.model.predict(X)
        return int(cluster_id[0])+1
