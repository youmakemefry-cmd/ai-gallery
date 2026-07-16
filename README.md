
DualVisor AI Gallery Enhanced

<img width="1774" height="887" alt="DUALVISOR-splashWIDE" src="https://github.com/user-attachments/assets/c31038fc-b7f6-4b1d-ae34-29abda10bd21" />

Welcome to **DualVisor**, a clean, modern, and highly interactive web gallery designed specifically for digital artists, AI creators, and designers. 

Whether you are working with AI image generation, photo restoration, or digital retouching, DualVisor gives you the perfect stage to showcase your work. It focuses entirely on what matters most: your images and the creative process behind them.

---

## ✨ What Makes It Special?

* **Interactive Slide-to-Compare:** Let your audience experience the transformation. With our smooth, touch-friendly split-screen slider, anyone can easily slide back and forth to see the exact changes between your original image and the enhanced AI version.
* **Smart Folder Organization:** No more messy grids. DualVisor automatically organizes your artwork into beautiful, structured folders. It makes browsing through large collections of various concepts feel effortless and neat.
* **Adaptive & Responsive Layouts:** Designed to look stunning on any screen. Whether your viewers are on a massive 4K desktop monitor or browsing on their mobile phones, the gallery dynamically adjusts to keep your images perfectly framed without awkward cropping.
* **Built-in Blog & Contact Hub:** Share the stories behind your creations. DualVisor includes a beautifully integrated blog to publish your thoughts, updates, or prompt guides, alongside a simple contact page to help you connect with your audience and clients.
* **Aesthetics First:** Inspired by modern dark-mode interfaces, the gallery uses subtle neon accents and smooth animations that make the entire experience feel premium, immersive, and incredibly satisfying to interact with.

<img width="1536" height="1024" alt="dualvisor-screen-mobile" src="https://github.com/user-attachments/assets/17fd1bb3-70cc-47dc-b210-3501f0f4cfa5" />

## Key Features
* **Interactive Comparison:** Built-in before/after slider for side-by-side analysis.
* **Progression-First UI:** Supports infinite variations per folder.
* **Automated Indexing:** No need to manually update HTML when you add new projects.
* **Lightbox Preview:** Built-in full-screen viewing mode with support for intuitive navigation and metadata display.
* **Glassmorphism UI:** Modern, clean aesthetic with blur-effects, dark theme, and high-quality responsiveness.
* **Mobile-First Design:** Fully adaptive layout that feels natural on both desktop and mobile devices.
* **Dark Mode:** Aesthetic, developer-friendly dark theme.
* **Zero Dependencies:** Pure HTML5, CSS3, and Vanilla JavaScript. Extremely fast and easy to deploy on GitHub Pages or any static host.

<table>
  <tr>
    <td width="40%">
      <a href="https://github.com/user-attachments/assets/027912e8-bcc6-451e-b4f2-3268cbe9cd27" target="_blank">
        <img src="https://github.com/user-attachments/assets/027912e8-bcc6-451e-b4f2-3268cbe9cd27" alt="Gallery Preview 2" style="height: 100%;" />
      </a>
    </td>
        <td width="40%">
      <a href="https://github.com/user-attachments/assets/1f16f203-0815-48db-8d60-b325692c3d7e" target="_blank">
        <img src="https://github.com/user-attachments/assets/1f16f203-0815-48db-8d60-b325692c3d7e" alt="Gallery Preview 1" style="height: 100%;" />
      </a>
    </td>
    <td width="15%">
      <a href="https://github.com/user-attachments/assets/e40dba0d-c89c-420e-998c-44a3a764e281" target="_blank">
        <img src="https://github.com/user-attachments/assets/e40dba0d-c89c-420e-998c-44a3a764e281" alt="Gallery Preview 3" style="height: 50%;" />
      </a>
    </td>
  </tr>
</table>

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
