# Black & White Film Portfolio

A single-page photography site: dark "contact-sheet" theme, masonry grid, click-to-enlarge
lightbox, plus short About and Contact sections. No build step, no dependencies — just static
files you can host free on GitHub Pages.

```
index.html      ← the whole site (HTML + CSS + JS in one file)
images/         ← your photos go here
README.md       ← this file
make_placeholders.py   ← script that generated the stand-in images (you can delete it)
```

---

## 1. Preview it right now

Double-click `index.html` to open it in your browser. Everything works locally except the
custom font, which loads from the internet (it falls back to a clean monospace if offline).

---

## 2. Make it yours

There are **5 edit spots**, each labeled with a comment like `EDIT #2` inside the files.
Open `index.html` in any text editor and search for `EDIT`.

| Spot | What it controls | Where |
|------|------------------|-------|
| EDIT #1 | Page title, browser-tab text, your name top-left | top of `index.html` |
| EDIT #2 | Hero — your name, statement, format/process notes | `<section class="hero">` |
| EDIT #3 | About paragraphs | `<section id="about">` |
| EDIT #4 | Contact — real email + Instagram handle | `<section id="contact">` |
| EDIT #5 | **Your photo list** | the `PHOTOS` array in `<script>` |

### Adding your photos (EDIT #5)

1. Drop your scans into the `images/` folder (you can delete the `frame-XX.jpg` placeholders).
2. In `index.html`, find the `PHOTOS` list and add one line per photo:

```js
{ src:"images/your-scan.jpg", title:"Crossing", stock:"Tri-X 400", format:"35mm", year:"2024" },
```

- **Order in the list = order on the page.**
- `title` can be `"Untitled"`. `stock`, `format`, and `year` show up as the caption notation.
- Photos display in grayscale by design. If you ever want to show one in its true tones,
  remove `filter:grayscale(100%)` from the `.frame .imgwrap img` and `.lb img` CSS rules.

### A note on file size

Film scans can be huge. For fast loading, export your web copies at roughly **1600–2000 px on
the long edge** and save as JPEG quality ~80. (The placeholders are ~1500 px / ~320 KB each as
a reference.) Keep the originals elsewhere.

---

## 3. Put it on GitHub Pages (free hosting)

You have two options. **Option A** gives you the cleanest URL.

### Option A — your main site: `yourusername.github.io`

1. On GitHub, create a **new repository** named exactly `yourusername.github.io`
   (use your real GitHub username, all lowercase).
2. Upload `index.html` and the `images/` folder to it
   (the **Add file → Upload files** button works fine — drag the folder in).
3. Wait ~1 minute, then visit **https://yourusername.github.io** — you're live.

### Option B — a project site (any repo name)

1. Create or open any repository and upload the files there.
2. Go to **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Set the branch to `main` and the folder to `/ (root)`, then **Save**.
5. After a minute, the page shows your URL: **https://yourusername.github.io/repo-name/**

Whenever you change a file and push/upload it, the live site updates automatically in a minute or two.

### Optional — your own domain

If you buy a domain (e.g. `kylephoto.com`), add a file named `CNAME` containing just that domain,
then point the domain's DNS at GitHub Pages following GitHub's
"Managing a custom domain" guide. Not required — the `.github.io` URL works forever.

---

## Quick reference

- Edit content → search `EDIT` in `index.html`
- Add photos → drop in `images/`, add a line to `PHOTOS`
- Go live → push to GitHub, enable Pages
