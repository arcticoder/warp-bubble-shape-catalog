# Jekyll Setup Instructions

This repository contains a Jekyll-based documentation site.

## Prerequisites

1. **Ruby** (version 2.7 or higher)
2. **Bundler** gem
3. **Jekyll** gem

## Installation

1. Install Ruby and Bundler if not already installed
2. Install Jekyll dependencies:
   ```bash
   bundle install
   ```

## Running the Site Locally

To preview the site locally:

```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`

## Building for Production

To build the static site:

```bash
bundle exec jekyll build
```

The generated site will be in the `_site/` directory.

## Site Structure

- `index.md` - Homepage with overview
- `profiles.md` - Mathematical profile descriptions
- `scripts.md` - Python script documentation  
- `visuals.md` - Plots and visualizations
- `_config.yml` - Jekyll configuration
- `_layouts/default.html` - Custom layout with MathJax support

## MathJax Support

The site includes MathJax for rendering LaTeX mathematics. Use standard LaTeX syntax:

- Inline math: `$f(x) = x^2$`
- Display math: `$$f(x) = \frac{1}{2}x^2$$`

## Deployment

This Jekyll site can be deployed to:

- **GitHub Pages**: Push to a GitHub repository with Pages enabled
- **Netlify**: Connect your repository for automatic deployment
- **Vercel**: Deploy directly from Git
- **Traditional hosting**: Upload the `_site/` folder contents



## Data and Scripts

All Python scripts and generated data remain functional:

- `scripts/` - Python utilities
- `data/` - Generated datasets and plots
- Generated visualizations are embedded in the Jekyll site
