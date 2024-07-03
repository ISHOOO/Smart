# Smart Attendance App

## Overview:
This application registers and fills student attendance smartly through Face Recognition using Computer Vision Algorithms such as Local Binary Patterns Histogram and HAAR cascade clasifier. 
It scans images of a student in real time and trains a classifier on those images to register the student. Then it predicts on a test image to fill the attendance for a given day.

## Libraries used:
**OpenCV**: An open-source computer vision and machine learning software library used for real-time image and video processing.

   ![OpenCV](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/ca79f2c5-0316-4d26-869e-861cd4097308)

**Custom Tkinter**:  Allows for the creation of customizable and visually appealing graphical user interfaces using the Tkinter library in Python.

   ![Custom Tkinter](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/12c68b23-e9d4-4b25-beb8-996317cb7f3a)

**Pandas**: A powerful data manipulation and analysis library in Python, known for its data structures like DataFrame and Series.

   ![Pandas](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/45344a48-4fb7-4753-bf40-6590a5481d42)

**Pyttsx3**: A text-to-speech conversion library in Python that works offline and supports multiple speech engines.

   ![pyttsx3](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/5818ddf5-adfc-4d0c-9acb-572ade17a8ea)

**Numpy**: A fundamental package for numerical computing in Python, providing support for arrays, matrices, and high-level mathematical functions.

   ![Numpy](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/959f2e9c-b453-44a7-af49-371e0e0f141a)

**Pillow**: A Python Imaging Library (PIL) fork that adds support for opening, manipulating, and saving various image file formats.

  ![Pillow](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/a3cf581b-800f-4878-9612-8f1b02b01762)


## Demonstrative visuals:

![Screenshot 2024-07-03 231621](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/c9d40c31-87ee-49e9-9491-48cd97a62088)

![Screenshot 2024-07-03 231640](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/f0f74b6e-7ad1-48b5-b73e-d806224c1075)

![Screenshot 2024-07-03 232726](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/c2daced5-231b-468c-9f13-752d8b15de99)

![Screenshot 2024-07-03 234750](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/92ac6626-9147-4feb-b10c-dd94be62e158)

![Screenshot 2024-07-03 232800](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/0cab2346-f237-4a43-82b1-1ca9e642d143)

![Screenshot 2024-07-03 234809](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/dd422f8f-c88e-4234-870e-8a1afeeedbbd)

![Screenshot 2024-07-03 234847](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/c74d41a6-cfcb-448d-907a-8e5673199fa2)

![sarthak info](https://github.com/ISHOOO/Smart-Attendance-App/assets/132544766/af9c873c-2d81-463a-b37c-dd3ec3c738dd)


## How to use this project 
1. Clone this repostory:
```shell
git clone "https://github.com/ISHOOO/Smart-Attendance-App"
```
2. Ensure the presence of dependencies:
```shell
pip install -r requirements.txt
```
3. Run `attendance.py`
```shell
python attendance.py
```
4. Click on the `Register a Student` button to register a new student
5. Click on `Take attendance` to fill the attendance for an already registered student.
6. Click on `View student info` to view student's registered information
7. Click on `View Attendance` to view student's attendance data.
