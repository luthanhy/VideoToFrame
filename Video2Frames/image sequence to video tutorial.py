import cv2
import os

# Input video file  
input_video_path = 'C:/Users/thanh/Downloads/VideoToFrame/Video2Frames/Screen_Recording_20231011_175355_Simpia.mp4'

# Output directory for frames
output_frame_dir = 'C:/Users/thanh/Downloads/VideoToFrame/Y/'

# Ensure the output directory exists, if not, create ite
if not os.path.exists(output_frame_dir):
    os.makedirs(output_frame_dir)

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print('Error: Could not open video.')
    exit(1)

# Get the frame width, height, and frames per second (fps) of the video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Loop through the video and save each frame as an image
frame_number = 0
while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    # Construct the output frame filename
    frame_filename = f'frame_{frame_number:04d}.jpg'
    output_frame_path = os.path.join(output_frame_dir, frame_filename)

    # Save the frame as an image
    cv2.imwrite(output_frame_path, frame)

    print(f'Saved frame {frame_number}')

# Release the video capture object and close the output video writer
cap.release()

# Print the total number of frames saved
print(f'Total frames saved: {frame_number}')

# Now, let's create a video from the saved frames
# Construct the output video filename
output_video_path = 'C:/Users/thanh/Downloads/VideoToFrame/Result/output_video.mp4'

# Get the list of frame filenames
frame_files = [os.path.join(output_frame_dir, f) for f in os.listdir(output_frame_dir) if f.endswith('.jpg')]

# Sort the frame filenames based on their frame number
frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_video = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Write each frame to the output video
for frame_file in frame_files:
    frame = cv2.imread(frame_file)
    out_video.write(frame)

# Release the video writer
out_video.release()

print('Output video saved to', output_video_path)
