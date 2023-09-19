from moviepy.editor import VideoFileClip

# Load the video
video_path = '/home/shiv/Documents/proton/coding/23413_1440p.mp4'
video = VideoFileClip(video_path)

# Define the start and end times in minutes
start_time_minutes = 16  
end_time_minutes = 23    

# Convert minutes to seconds
start_time = start_time_minutes * 60
end_time = end_time_minutes * 60

# Trim the video
trimmed_video = video.subclip(start_time, end_time)

# Save the trimmed video
output_path = '/home/shiv/Documents/proton/coding/trimmed_video.mp4'
trimmed_video.write_videofile(output_path, codec='libx264')

# Close the video file
video.close()
