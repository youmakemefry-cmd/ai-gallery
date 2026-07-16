# DualVisor Gallery Engine
<img width="1536" height="1024" alt="DUALVISOR" src="https://github.com/user-attachments/assets/17fd1bb3-70cc-47dc-b210-3501f0f4cfa5" />


A lightweight, zero-dependency, static-site gallery engine designed for AI artists, photographers, and creatives. Showcase your "Original vs. Variation" workflows with an interactive, glass-morphism inspired interface.

## Why this engine?
I built this because existing portfolio templates often lack a way to display non-linear AI generation processes. This engine automates the gallery creation process so you can focus on your art, not on manual HTML coding.

## Key Features
* **Interactive Comparison:** Built-in before/after slider for side-by-side analysis.
* **Progression-First UI:** Supports infinite variations per folder.
* **Automated Indexing:** No need to manually update HTML when you add new projects.
* **Lightbox Preview:** Built-in full-screen viewing mode with support for intuitive navigation and metadata display.
* **Glassmorphism UI:** Modern, clean aesthetic with blur-effects, dark theme, and high-quality responsiveness.
* **Mobile-First Design:** Fully adaptive layout that feels natural on both desktop and mobile devices.
* **Dark Mode:** Aesthetic, developer-friendly dark theme.
* **Zero Dependencies:** Pure HTML5, CSS3, and Vanilla JavaScript. Extremely fast and easy to deploy on GitHub Pages or any static host.

<a href="https://github.com/user-attachments/assets/027912e8-bcc6-451e-b4f2-3268cbe9cd27" target="_blank">
  <img src="https://github.com/user-attachments/assets/027912e8-bcc6-451e-b4f2-3268cbe9cd27" alt="Gallery Preview" width="50%" />
</a>

## Getting Started

### 1. Folder Structure
Organize your project folder with numbered subdirectories (e.g., `1`, `2`, `3`...).
Each folder should contain your source file (typically the first one) and your AI iterations.
```text
/1/
  - original.jpg
  - variation_1.png
  - variation_2.png
/2/
  ...
2. Generate the Index
Since GitHub Pages is a static host, the engine reads your folder structure from a gallery.json file. Use the provided build.py script to generate it automatically:

Place build.py in your project root.

Run the script via terminal:

Bash
python build.py
This will scan your folders and generate the gallery.json file automatically.

3. Deploy
Once you have generated your gallery.json, commit and push your changes to your GitHub repository:

Bash
git add .
git commit -m "Update gallery index"
git push
Your gallery will update instantly on your GitHub Pages link.

Customization
Compare Mode: Users can toggle "Compare Mode" to switch between a standard gallery view or the interactive slider view.

Styling: The engine is self-contained in index.html. You can easily tweak the CSS variables at the top of the file to match your brand colors.

Built for artists and developers. Feel free to fork and use this engine for your own AI portfolio.

## 📝 Blog Integration

DualVisor also includes a dedicated **JSON-based blogging system**. You can maintain your project updates by simply editing a `blog.json` file—perfect for adding devlogs, creative process notes, or news updates without touching the HTML.

## 💻 Tech Stack

* **HTML5/CSS3:** Modern grid-based layout with glass-morphism.
* **Vanilla JS:** Efficient DOM manipulation, touch events for mobile swiping, and asynchronous data fetching.
* **Python:** A helper script to automate gallery indexing.

---

*Built with passion for the AI art community.*
