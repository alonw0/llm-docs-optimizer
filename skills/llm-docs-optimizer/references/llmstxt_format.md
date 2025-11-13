# llms.txt Format Specification

This document provides a complete reference for creating llms.txt files according to the official specification at https://llmstxt.org/

## Overview

**llms.txt** is a standardized markdown file format designed to provide LLM-friendly content summaries and documentation. It solves a critical problem: context windows are too small to handle most websites in their entirety.

### Purpose

- Provides brief background information, guidance, and links to detailed markdown files
- Optimized for consumption by language models and AI agents
- Used at inference time when users explicitly request information
- Helps LLMs navigate documentation, understand projects, and access the right resources
- Enables chatbots with search functionality to retrieve relevant information efficiently

### Why Markdown?

The specification uses markdown rather than XML/JSON because "we expect many of these files to be read by language models and agents" while still being "readable using standard programmatic-based tools."

## File Structure

The format follows a specific structural hierarchy:

1. **H1 heading** (`# Title`) - **REQUIRED**
2. **Blockquote summary** (`> text`) - Optional but recommended
3. **Descriptive content** (paragraphs, bullet lists) - Optional
4. **H2-delimited sections** (`## Section Name`) with file lists - Optional

### Basic Template

```markdown
# Project Name

> Brief summary of what this project does and why it exists.

- Key principle or feature
- Another important concept
- Third key point

## Documentation

- [Main Guide](https://example.com/docs/guide.md): Getting started guide
- [API Reference](https://example.com/docs/api.md): Complete API documentation

## Examples

- [Basic Usage](https://example.com/examples/basic.md): Simple examples
- [Advanced Patterns](https://example.com/examples/advanced.md): Complex use cases

## Optional

- [Blog](https://example.com/blog/): Latest news and updates
- [Community](https://example.com/community/): Join discussions
```

## Required Elements

### H1 Title (Required)

The project or site name - this is the **ONLY mandatory element**.

```markdown
# Project Name
```

## Optional Elements

### Blockquote Summary (Recommended)

Brief project description with key information necessary for understanding the rest of the file.

```markdown
> Project Name is a Python library for data processing. It provides efficient
> stream transformations and supports multiple output formats.
```

### Descriptive Content (Optional)

Any markdown content **EXCEPT headings**. Use paragraphs, bullet lists, etc.

```markdown
Key features:
- Fast stream processing with lazy evaluation
- Built-in error handling and recovery
- Zero-dependency core library
- Extensible plugin system

Project Name follows these principles:
1. Simplicity over complexity
2. Performance by default
3. Developer experience first
```

**Important:** Do NOT use H2, H3, or other headings in descriptive content. Only H1 (title) and H2 (section headers) are allowed.

### File List Sections (Optional)

H2-headed sections containing links to resources.

```markdown
## Section Name

- [Link Title](https://full-url): Optional description or notes about the resource
- [Another Link](https://url): More details here
```

## Link Format Requirements

Each file list entry must follow this exact pattern:

```markdown
- [Link Title](https://full-url): Optional description
```

### Rules:

1. Use markdown bullet lists (`-`)
2. Include markdown hyperlinks `[name](url)`
3. Optionally add `:` followed by notes about the file
4. Links should point to markdown versions of documentation (preferably `.md` files)
5. Use full URLs, not relative paths

### Examples:

```markdown
## Documentation

- [Quick Start](https://docs.example.com/quickstart.md): Get up and running in 5 minutes
- [Configuration Guide](https://docs.example.com/config.md): All configuration options explained
- [API Reference](https://docs.example.com/api.md): Complete API documentation with examples
```

## Special Sections

### Optional Section

The **"Optional"** section has special meaning: content here can be skipped when shorter context is needed.

```markdown
## Optional

- [Blog](https://example.com/blog/): Latest news about the project
- [Case Studies](https://example.com/cases/): Real-world usage examples
- [Video Tutorials](https://example.com/videos/): Visual learning resources
```

Use this section for:
- Secondary resources
- Community links
- Blog posts and news
- Extended tutorials
- Background reading

## Common Section Names

### Documentation-focused Projects

```markdown
## Documentation
- Core docs, guides, tutorials

## API Reference
- Function references, method documentation

## Examples
- Code samples, patterns, recipes

## Guides
- How-to guides, best practices

## Development
- Contributing, setup, testing

## Optional
- Blog, community, extended resources
```

### Tool/CLI Projects

```markdown
## Getting Started
- Installation, quickstart

## Commands
- CLI reference, usage examples

## Configuration
- Config files, options

## Examples
- Common workflows, patterns

## Optional
- Advanced usage, plugins
```

### Framework Projects

```markdown
## Core Concepts
- Architecture, principles

## Documentation
- Guides, tutorials

## API Reference
- Component APIs, hooks

## Examples
- Starter templates, patterns

## Plugins/Integrations
- Extensions, third-party tools

## Optional
- Blog, showcase, community
```

## File Placement

### Repository Location

Place at **`/llms.txt`** in the repository root, alongside `README.md`.

### Web Serving

For websites, serve at the root path `/llms.txt` (e.g., `https://example.com/llms.txt`).

### Companion Files

You can create expanded versions:
- `llms-ctx.txt` - Expanded content without URLs
- `llms-ctx-full.txt` - Expanded content with URLs

For referenced pages, create markdown versions:
- `page.html` → `page.html.md`
- Or use `index.html.md` for pages without filenames

## Best Practices

### Content Guidelines

1. **Be Concise**: Use clear, brief language
2. **Avoid Jargon**: Explain technical terms or link to explanations
3. **Information Hierarchy**: Most important content first
4. **Test with LLMs**: Verify that language models can understand your content
5. **Keep Updated**: Maintain accuracy as your project evolves

### Link Best Practices

1. **Descriptive Titles**: Use meaningful link text (not "click here")
2. **Helpful Notes**: Add context after colons to explain what each resource contains
3. **Stable URLs**: Link to permanent, versioned documentation
4. **Markdown Files**: Prefer `.md` files over HTML when possible
5. **Complete URLs**: Use full URLs with protocol (https://)

### Organizational Strategy

1. **Start with Essentials**: Put most important docs first
2. **Logical Grouping**: Group related resources under descriptive H2 headings
3. **Progressive Detail**: Basic → Intermediate → Advanced
4. **Optional Last**: Secondary resources go in the "Optional" section
5. **Consistent Format**: Use the same link format throughout

## Examples from the Wild

### Real-World Implementations

- **Astro**: https://docs.astro.build/llms.txt
- **FastHTML**: https://www.fastht.ml/docs/llms.txt
- **Shopify**: https://shopify.dev/llms.txt
- **Strapi**: https://docs.strapi.io/llms.txt
- **Modal**: https://modal.com/llms.txt

### Example: FastHTML Style

```markdown
# FastHTML

> FastHTML is a Python library for building web applications using pure Python.

FastHTML follows these principles:
- Write HTML in Python with no JavaScript required
- Use standard Python patterns and idioms
- Deploy anywhere Python runs

## Documentation

- [Tutorial](https://docs.fastht.ml/tutorial.md): Step-by-step introduction
- [Reference](https://docs.fastht.ml/reference.md): Complete API reference
- [Examples](https://docs.fastht.ml/examples.md): Common patterns and recipes

## Optional

- [FastHTML Blog](https://fastht.ml/blog/): Latest updates
```

### Example: Framework Style

```markdown
# Astro

> Astro is an all-in-one web framework for building fast, content-focused websites.

- Uses island architecture for better performance
- Server-first design with minimal client JavaScript
- Supports React, Vue, Svelte, and other UI frameworks
- Zero JavaScript by default

## Documentation Sets

- [Getting Started](https://docs.astro.build/getting-started.md): Installation and first project
- [Core Concepts](https://docs.astro.build/core-concepts.md): Islands, components, routing
- [Complete Docs](https://docs.astro.build/llms-full.txt): Full documentation set

## API Reference

- [Configuration](https://docs.astro.build/reference/configuration.md): astro.config.mjs options
- [CLI Commands](https://docs.astro.build/reference/cli.md): Command-line reference
- [Integrations API](https://docs.astro.build/reference/integrations.md): Building integrations

## Optional

- [Astro Blog](https://astro.build/blog/): Development news
- [Showcase](https://astro.build/showcase/): Sites built with Astro
```

## Allowed Markdown Elements

### Supported

- `#` H1 for title (required)
- `##` H2 for section headers
- `>` Blockquotes for summary
- `-` Bullet lists
- `[text](url)` Markdown links
- `:` Colon separator for notes after links
- Plain paragraphs
- Numbered lists (`1.`, `2.`, etc.)

### Not Used/Forbidden

- H3, H4, H5, H6 headings in descriptive content
- XML, JSON, or other structured formats
- Complex markdown tables
- Images (focus on text content)
- Code blocks (link to them instead)

## Tools and Integration

### CLI Tool

`llms_txt2ctx` - Command-line tool for processing and expanding llms.txt files

### Framework Plugins

- **VitePress**: https://github.com/okineadev/vitepress-plugin-llms
- **Docusaurus**: https://github.com/rachfop/docusaurus-plugin-llms
- **Drupal**: https://www.drupal.org/project/llm_support
- **PHP**: https://github.com/raphaelstolt/llms-txt-php

### Directories

- https://llmstxt.site/ - Directory of available llms.txt files
- https://directory.llmstxt.cloud/ - Community directory

## Common Mistakes to Avoid

1. **Using Relative URLs**: Always use full URLs with protocol
2. **Too Much Content**: Keep it concise, link to details
3. **Missing Descriptions**: Add helpful notes after link colons
4. **No Structure**: Use H2 sections to organize links
5. **Outdated Links**: Keep URLs current as docs evolve
6. **Complex Formatting**: Stick to simple markdown
7. **No Summary**: Always include a blockquote summary
8. **Wrong File Location**: Must be at repository root as `/llms.txt`

## Validation Checklist

Before publishing your llms.txt:

- ✅ File is named exactly `llms.txt` (lowercase)
- ✅ File is at repository root
- ✅ Has H1 title as first element
- ✅ Has blockquote summary
- ✅ Uses only H1 and H2 headings
- ✅ All links use full URLs
- ✅ Links use proper markdown format `[text](url)`
- ✅ Descriptive notes added after colons where helpful
- ✅ Sections logically organized
- ✅ Essential content comes before optional
- ✅ Links point to markdown files when possible
- ✅ Content is concise and clear
- ✅ Tested with an LLM for comprehension

## Additional Resources

- **Official Site**: https://llmstxt.org/
- **GitHub**: https://github.com/answerdotai/llms-txt
- **Issues**: https://github.com/AnswerDotAI/llms-txt/issues/new
- **Community**: Discord channel (check official site for link)

## Version

This reference is based on the llms.txt specification as of November 2025. Check https://llmstxt.org/ for the latest updates.
