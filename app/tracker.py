# app/tracker.py
from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize DeepSORT
tracker = DeepSort(max_age=30)

def track_objects(detections):
    # detections = list of (x1, y1, x2, y2, class_id, conf)
    track_inputs = []
    for det in detections:
        x1, y1, x2, y2, cls, conf = det
        track_inputs.append(([x1, y1, x2-x1, y2-y1], conf, cls))

    tracks = tracker.update_tracks(track_inputs, frame=None)
    tracked = []
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, w, h = track.to_ltrb()
        tracked.append((l, t, l+w, t+h, track_id))
    return tracked
