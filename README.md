# AI Progression Gallery Engine
<a href="https://github.com/user-attachments/assets/cb032e0b-0f26-4be3-b993-2939928c39e3" target="_blank">
  <img src="https://github.com/user-attachments/assets/cb032e0b-0f26-4be3-b993-2939928c39e3" alt="Gallery Preview" width="50%" />
</a>

A lightweight, dark-themed portfolio engine designed to showcase iterative AI generation work. Instead of just showing static results, this engine highlights the "progression"—allowing viewers to compare the original output with various AI variations using an interactive before/after slider.

## Why this engine?
I built this because existing portfolio templates often lack a way to display non-linear AI generation processes. This engine automates the gallery creation process so you can focus on your art, not on manual HTML coding.

## Key Features
*   **Interactive Comparison:** Built-in before/after slider for side-by-side analysis.
*   **Progression-First UI:** Supports infinite variations per folder.
*   **Automated Indexing:** No need to manually update HTML when you add new projects.
*   **Mobile Responsive:** Fully adaptive design for phone and desktop viewing.
*   **Dark Mode:** Aesthetic, developer-friendly dark theme.

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
