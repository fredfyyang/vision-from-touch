from moviepy.video.io.VideoFileClip import VideoFileClip
import os

# List of video file names
file_names = ["wood1_1.mp4", "wood2_1.mp4", "wood3_1.mp4", "wood4_1.mp4", "stone1_1.mp4", "stone2_1.mp4", "stone3_1.mp4", "stone4_1.mp4"]

# Determine the shortest duration among all videos
min_duration = min([VideoFileClip(f).duration for f in file_names])

# Create a new directory to save the edited videos
os.makedirs("edited_videos", exist_ok=True)

# Function to resize the videos
def resize_video(file_name, duration):
    with VideoFileClip(file_name) as video:
        # Calculate the end time in terms of frames
        end_frame_time = min(duration, video.duration)
        end_frame = int(end_frame_time * video.fps)

        # Trim the video according to frames
        new_video = video.subclip(0, end_frame_time).set_duration(end_frame / video.fps)

        new_video.write_videofile(os.path.join("edited_videos", file_name), fps=video.fps, audio_codec='aac')

# Resize each video in the list
for file_name in file_names:
    resize_video(file_name, min_duration)

