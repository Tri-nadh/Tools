{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "aea3aaa9-bad4-4688-92bc-c260e93e0d28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Moviepy - Building video /home/shiv/Documents/proton/coding/trimmed_video.mp4.\n",
      "MoviePy - Writing audio in trimmed_videoTEMP_MPY_wvf_snd.mp3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                \r"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MoviePy - Done.\n",
      "Moviepy - Writing video /home/shiv/Documents/proton/coding/trimmed_video.mp4\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                \r"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Moviepy - Done !\n",
      "Moviepy - video ready /home/shiv/Documents/proton/coding/trimmed_video.mp4\n"
     ]
    }
   ],
   "source": [
    "from moviepy.editor import VideoFileClip\n",
    "\n",
    "# Load the video\n",
    "video_path = '/home/shiv/Documents/proton/coding/23413_1440p.mp4'\n",
    "video = VideoFileClip(video_path)\n",
    "\n",
    "# Define the start and end times in minutes\n",
    "start_time_minutes = 16  \n",
    "end_time_minutes = 23    \n",
    "\n",
    "# Convert minutes to seconds\n",
    "start_time = start_time_minutes * 60\n",
    "end_time = end_time_minutes * 60\n",
    "\n",
    "# Trim the video\n",
    "trimmed_video = video.subclip(start_time, end_time)\n",
    "\n",
    "# Save the trimmed video\n",
    "output_path = '/home/shiv/Documents/proton/coding/trimmed_video.mp4'\n",
    "trimmed_video.write_videofile(output_path, codec='libx264')\n",
    "\n",
    "# Close the video file\n",
    "video.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bb9cd93-11cb-4637-b2f9-ef02387a964a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
