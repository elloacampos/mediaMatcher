import os
import shutil
import sys
import pathlib
import cv2
import face_recognition  # pip install face_recognition
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

"""
Loads all images in the target directory and extracts face encodings.
Returns a list of encodings.
"""
def load_target_encodings(dir_targets):
    status_label.config(text="Processing")
    encodings = []
    for fname in os.listdir(dir_targets):
        path = os.path.join(dir_targets, fname)
        if os.path.isfile(path) and fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            image = face_recognition.load_image_file(path)
            face_encs = face_recognition.face_encodings(image)
            if len(face_encs) > 0:
                encodings.append(face_encs[0])
            else:
                print(f"⚠️ Target without face detected: {path}")
    print(f"Loaded {len(encodings)} target face encodings")
    return encodings

"""
Processes an image file: detects faces, compares with targets.
If a match is found, moves the file to out_dir (directory 3) and returns True.
"""
def process_image_file(path, target_encodings, out_dir, tolerance=0.6):
    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    for fe in face_encodings:
        results = face_recognition.compare_faces(target_encodings, fe, tolerance=tolerance)
        if True in results:
            # matches a target
            fname = os.path.basename(path)
            dst = os.path.join(out_dir, fname)
            shutil.move(path, dst)
            print(f"🔍 Target found in image {path} -> moved to {dst}")
            return True
    return False

"""
Processes a video file: extracts frames every frame_step, tries to detect a match.
If a target is found, moves the entire video to out_dir.
"""
def process_video_file(path, target_encodings, out_dir, tolerance=0.6, frame_step=30): 
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print(f"Error opening video {path}")
        return False

    frame_count = 0
    found = False
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_step == 0:
            # convert BGR (OpenCV) to RGB (face_recognition)
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_small_frame, model="cnn")
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            for fe in face_encodings:
                results = face_recognition.compare_faces(target_encodings, fe, tolerance=tolerance)
                if True in results:
                    found = True
                    break
        if found:
            break
        frame_count += 1

    cap.release()
    if found:
        fname = os.path.basename(path)
        dst = os.path.join(out_dir, fname)
        shutil.move(path, dst)
        print(f"🔍 Target found in video {path} -> moved to {dst}")
        return True
    return False

def process_files():
    dir_A = filedialog.askdirectory(title="Select source directory")
    if not dir_A:
        return
    f1.config(text=f1.cget("text") + " " + dir_A)

    dir_B = filedialog.askdirectory(title="Select the folder with the target images")
    if not dir_B:
        return
    f2.config(text=f2.cget("text") + " " + dir_B)

    dir_C = filedialog.askdirectory(title="Select output directory")
    if not dir_C:
        return
    f3.config(text=f3.cget("text") + " " + dir_C)

    target_encodings = load_target_encodings(dir_B)
    os.makedirs(dir_C, exist_ok=True)

    lstFiles = os.listdir(dir_A) 
    number_files = len(lstFiles)
    print(f"{number_files} files found")

    for fname in lstFiles:
        path = os.path.join(dir_A, fname)
        print(path)
        if os.path.isfile(path):
            ext = fname.lower().split('.')[-1]
            try:
                if ext in ('jpg', 'jpeg', 'png'):
                    process_image_file(path, target_encodings, dir_C)
                elif ext in ('mp4', 'mov', 'avi', 'mkv', 'm4v'):
                    process_video_file(path, target_encodings, dir_C)
                else:
                    pass
            except Exception as e:
                print(f"❗ An error occurred while processing {path}: {e}")

    status_label.config(text="Process completed successfully!")

root = tk.Tk()
root.title("Media Matcher")
root.geometry("400x170")

f1 = tk.Label(root, text="Source directory:")
f1.pack(padx=10, pady=5, anchor="w")

f2 = tk.Label(root, text="Target images:")
f2.pack(padx=10, pady=5, anchor="w")

f3 = tk.Label(root, text="Output directory:")
f3.pack(padx=10, pady=5, anchor="w")

# Rótulo de status
status_label = tk.Label(root, text="")
status_label.pack(padx=10, pady=5, anchor="w")

btn_process = tk.Button(root, text="Start", command=process_files)
btn_process.pack(padx=10, pady=5, anchor="w")

root.mainloop()