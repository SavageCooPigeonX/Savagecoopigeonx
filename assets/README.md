# Assets Directory

## 📁 Structure

```
assets/
├── images/           # Image files for documentation
│   ├── diagrams/     # System diagrams and flowcharts
│   ├── logos/        # Project logos and branding
│   ├── screenshots/  # Screenshot documentation
│   └── concepts/     # Conceptual illustrations
└── README.md        # This file
```

## 🖼️ Image Guidelines

### Supported Formats
- **PNG**: Preferred for logos, diagrams, and screenshots
- **JPG/JPEG**: Good for photographs and complex images
- **SVG**: Ideal for scalable graphics and simple illustrations
- **WebP**: Modern format for web optimization

### Naming Convention
Use descriptive, lowercase names with hyphens:
- `system-architecture-diagram.png`
- `protocol-flow-chart.svg`
- `ui-screenshot-main-dashboard.jpg`
- `concept-ai-consciousness-network.png`

### Image Placement Examples

#### Basic Image
```markdown
![Alt text](./assets/images/example.png)
```

#### Image with Caption
```markdown
<figure>
  <img src="./assets/images/system-diagram.png" alt="System Architecture" width="600">
  <figcaption><em>Figure 1: SAVAGECOOPIGEONX System Architecture Overview</em></figcaption>
</figure>
```

#### Responsive Image
```markdown
<img src="./assets/images/diagram.png" alt="Description" style="max-width: 100%; height: auto;">
```

## 📝 Adding Images to Articles

1. **Place images** in appropriate subdirectory under `assets/images/`
2. **Reference images** using relative paths from the markdown file
3. **Always include** descriptive alt text for accessibility
4. **Consider file size** - optimize images for web viewing
5. **Use captions** for complex diagrams or important visuals

## 🎨 Visual Enhancement Ideas

- System architecture diagrams
- Protocol flow charts
- Concept illustrations
- Timeline graphics
- Network topology maps
- AI consciousness visualization
- Process flow diagrams
- Status dashboards
- Mind maps of key concepts

---

*Add visual elements to make complex concepts more accessible and engaging.*