# discovering-traffic-direction

Implementation of a clustering method to discover the main traffic directions of vehicles observed by a traffic camera

To run this function, use:
```
python m_cluster_tracklets.py -i <tracklets.json> -n <num_cluster> \-o <tracklets_with_clusterIDs.json>
```
Here, tracklets.json is a file that contains vehicle tracklets, obtained by running a tracking algorithm
to track vehicles in a video file. This file contains multiple tracklets, each tracklet is supposed to correspond
to one vehicle in the video. Each tracklet is associated with a numerical ID, the vehicle class (among: car,
bike, bus, truck, others), and a list of detections. Each detection is a 5-tuple, where the first entry is the
frame number of the video, and the last four entries are the x; y coordinates of the detected bounding box.
Specifically, the first 2 coordinates correspond to the x; y coordinates of the top left corner of the detected
bounding box and the next 2 coordinates correspond to the x; y coordinates of the bottom right corner of the
detected bounding box.

To visualize the result, you can use:
```
python m_visualize_tracklets.py -t <tracklets_with_clusterIDs.json> \
-iv <input_video.mp4> -ov <output_video.mp4>```
