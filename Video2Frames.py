{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "41f80afa-215d-44a3-a566-5ac701eb4b75",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import cv2\n",
    "\n",
    "output_dir = 'frames1/'\n",
    "if not os.path.exists(output_dir):\n",
    "    os.makedirs(output_dir)\n",
    "    \n",
    "cap = cv2.VideoCapture('/home/shiv/Downloads/HandGuesture.mp4')\n",
    "    \n",
    "frame_count = 0\n",
    "while cap.isOpened():\n",
    "    ret, frame = cap.read()\n",
    "    if not ret:\n",
    "        break\n",
    "    \n",
    "    frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')\n",
    "    cv2.imwrite(frame_filename, frame)\n",
    "    \n",
    "    frame_count += 1\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1981f522-1c27-4afc-a84d-5f55ef1f6bec",
   "metadata": {},
   "outputs": [],
   "source": [
    "create_data('/home/shiv/Downloads/HandGuesture.mp4')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "289d9074-222b-4d3f-a71c-a7b8e08d1dda",
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
