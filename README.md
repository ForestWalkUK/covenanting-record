# The Covenanting Record

A journal of Reformed and Covenanting reflection, built with Jekyll and Tufte CSS,
hosted on GitHub Pages.

---

## Local Development

### Prerequisites

- Ruby (2.7+)
- Bundler (`gem install bundler`)

### Setup

```bash
git clone https://github.com/forestwalkuk/covenanting-record.git
cd covenanting-record
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/covenanting-record/ in your browser.

---

## Writing a New Journal Post

Create a file in `_posts/` named `YYYY-MM-DD-your-title.md`:

```yaml
---
layout: post
title: "Your Post Title"
date: 2026-04-12
tags: [covenant, reformation]
comments: true
---

Your content here...
```

---

## Adding a Document (with Sidebar)

Create a file in `_documents/` named `your-document.md`:

```yaml
---
layout: document
title: "Document Title"
subtitle: "Optional subtitle"
description: "Brief description shown on the Documents index."
order: 1
section: "Section Name"
comments: false
---

Your content here...
```

The `order` field controls sorting in the sidebar. The `section` field groups
documents under headings.

---

## Enabling Comments (Giscus)

1. Enable GitHub Discussions on your repository (Settings → Features → Discussions)
2. Visit https://giscus.app
3. Enter `forestwalkuk/covenanting-record` as the repository
4. Copy the generated `data-repo-id` and `data-category-id` values
5. Replace `REPLACE_WITH_REPO_ID` and `REPLACE_WITH_CATEGORY_ID` in:
   - `_layouts/post.html`
   - `_layouts/document.html`

---

## Deploying to GitHub Pages

Push to the `main` branch. GitHub Actions will build and deploy automatically.

The site will be live at: https://forestwalkuk.github.io/covenanting-record/

---

## Tufte CSS Features

In your Markdown/HTML you can use:

```html
<!-- Sidenote -->
<label for="sn-1" class="margin-toggle sidenote-number"></label>
<input type="checkbox" id="sn-1" class="margin-toggle"/>
<span class="sidenote">Your sidenote text here.</span>

<!-- Scripture quotation -->
<div class="scripture">
    <p>For God so loved the world...</p>
    <cite>John 3:16</cite>
</div>

<!-- Margin note (no number) -->
<label for="mn-1" class="margin-toggle">&#8853;</label>
<input type="checkbox" id="mn-1" class="margin-toggle"/>
<span class="marginnote">A margin note without a number.</span>
```

---

*Soli Deo Gloria*
