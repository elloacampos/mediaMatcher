# MediaMatcher 🎬  

A desktop tool that scans a folder of photos and videos, compares them against one or more target images (people or objects), and moves matching files to an output folder for automated media organization.

---

## 🎯 Features  
- Scan folders with photos and videos.  
- Specify one or more **target images** (e.g., particular people or objects) to search for.  
- Automatically compare each media file to the target images.  
- If a match is found, move the file to the output folder (or other configurable action).  
- Ideal for automatically filtering photos/videos where a particular person or object appears.

---

## 📦 Technologies Used  
- Language / Framework: Python.  
- File-system handling for organizing media files.

---

## 🚀 Getting Started  
### Prerequisites  
- TBD

### Installation  
1. Clone the repo:  
   ```bash
   TBD
2. Build the project:
   ```bash
   TBD

3. Configure:
- Create an input folder where your media files (photos + videos) are placed.
- Create a folder (or specify) for target images you want to match against.
- Define the output folder where the matching media files will be moved.
- Adjust configuration parameters (e.g., match tolerance, include/exclude videos, file types) as needed.
4. Run the application:
   ```bash
   TBD

5. Usage
- In the UI, select the input folder (your photos/videos).
- Select one or more target images.
- Define the output folder.
- Trigger the scan.
- The application will move all media files containing the target(s) into the output folder.

🛠 Example Use-Cases
- Vacation photo cleanup: You have a folder with thousands of holiday photos/videos. You want to filter everything in which “Alice” appears. Use a photo of Alice as target, set input = “Holiday2025”, output = “WithAlice”.
- Object filtering: You have many drone videos; you want to move all that contain a specific red car. Use an image of the red car as target, input = “DroneFootage”, output = “ContainsRedCar”.

✅ Good Practices & Tips
- Use high-quality target images (clear visibility of the person/object).
- Adjust matching tolerance based on how strongly the target appears (e.g., full-face vs small partial).
- Make a backup of your input folder before moving files, to avoid accidental data loss.
- Confirm supported file types (e.g., .jpg, .png, .mp4, .mov) and exclude unsupported ones.
- If you have very large folders (many thousands of files), consider splitting into sub-folders or filtering by date/type first for performance.

🎨 Roadmap
- ☑ Support for photos
- ☑ Support for videos
- ☐ Add advanced filtering (by date, location, media type)
- ☐ Export a report of moved files (CSV or JSON)

📬 Contact
- For questions or suggestions, please open an Issue on GitHub or reach out to elloalisboa@gmail.com
