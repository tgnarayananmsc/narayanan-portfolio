# T G Narayanan Portfolio Website

A Flask-based portfolio website. There is **no admin dashboard, no admin login, and no image-upload dashboard**.

## Add your project photos through GitHub

1. Open your GitHub repository.
2. Open `static/gallery/`.
3. Choose **Add file → Upload files**.
4. Upload your `.jpg`, `.jpeg`, `.png`, `.webp`, or `.gif` project photos.
5. Commit the changes. Refresh the Gallery page after the site redeploys.

The gallery automatically lists image files from `static/gallery/`. It shows photos only, without image filenames or captions.

## Run locally on Windows

1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run:

   ```powershell
   py -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt
   python app.py
   ```

4. Open `http://127.0.0.1:5000`.

There is no `start_portfolio.bat` file. All internal navigation links use the same browser tab.

## Resume

To publish your resume, place your PDF at `static/resume.pdf` and ensure the resume template links to it. Replace that file in GitHub whenever your resume changes.
