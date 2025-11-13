# Example: llms.txt Generation for Different Project Types

This document shows examples of llms.txt files generated for different types of projects, demonstrating how to structure the file based on project characteristics.

---

## Example 1: Python Library (Data Processing)

### Project Context
A Python library called "DataFlow" for stream data processing with multiple output formats.

### Generated llms.txt

```markdown
# DataFlow

> DataFlow is a Python library for processing data streams with real-time transformations
> and multiple output formats. It provides efficient stream processing with lazy evaluation
> and built-in error handling.

Key features:
- Fast stream processing with lazy evaluation
- Support for CSV, JSON, Parquet, and custom formats
- Built-in error handling and recovery
- Zero-dependency core library
- Extensible plugin system

## Documentation

- [Quick Start Guide](https://github.com/example/dataflow/blob/main/docs/quickstart.md): Get up and running in 5 minutes
- [Core Concepts](https://github.com/example/dataflow/blob/main/docs/concepts.md): Understanding streams, transformations, and processing
- [Configuration Guide](https://github.com/example/dataflow/blob/main/docs/configuration.md): All configuration options explained

## API Reference

- [Stream API](https://github.com/example/dataflow/blob/main/docs/api/stream.md): Stream creation and manipulation methods
- [Transformations](https://github.com/example/dataflow/blob/main/docs/api/transforms.md): Built-in transformation functions
- [Exports](https://github.com/example/dataflow/blob/main/docs/api/exports.md): Output format specifications

## Examples

- [Basic Usage](https://github.com/example/dataflow/blob/main/examples/basic.md): Simple stream processing examples
- [Common Patterns](https://github.com/example/dataflow/blob/main/examples/patterns.md): Filtering, mapping, and aggregation
- [Error Handling](https://github.com/example/dataflow/blob/main/examples/errors.md): Handling failures and recovery
- [Advanced Usage](https://github.com/example/dataflow/blob/main/examples/advanced.md): Parallel processing and custom plugins

## Development

- [Contributing Guide](https://github.com/example/dataflow/blob/main/CONTRIBUTING.md): How to contribute to DataFlow
- [Development Setup](https://github.com/example/dataflow/blob/main/docs/development.md): Setting up local development environment
- [Testing](https://github.com/example/dataflow/blob/main/docs/testing.md): Running and writing tests

## Optional

- [DataFlow Blog](https://dataflow.example.com/blog/): Latest updates and tutorials
- [Changelog](https://github.com/example/dataflow/blob/main/CHANGELOG.md): Version history and release notes
- [Performance Benchmarks](https://github.com/example/dataflow/blob/main/docs/performance.md): Benchmark results and optimization tips
```

### Why This Structure?

- **Blockquote**: Clearly explains what DataFlow is and its main value proposition
- **Key Features**: Bullet list highlights important capabilities
- **Documentation**: Essential guides for getting started and understanding core concepts
- **API Reference**: Organized by major components (Stream, Transformations, Exports)
- **Examples**: Progressive from basic to advanced, includes error handling
- **Development**: Resources for contributors
- **Optional**: Secondary resources like blog and benchmarks

---

## Example 2: CLI Tool (Developer Tool)

### Project Context
A command-line tool called "BuildKit" for managing build processes and deployment pipelines.

### Generated llms.txt

```markdown
# BuildKit

> BuildKit is a CLI tool for managing build processes, running tests, and deploying
> applications across multiple environments. It provides a unified interface for common
> development workflows.

BuildKit follows these principles:
- Convention over configuration
- Fast feedback loops
- Environment parity
- Reproducible builds

## Getting Started

- [Installation](https://buildkit.dev/docs/install.md): Installing BuildKit on macOS, Linux, and Windows
- [Quick Start](https://buildkit.dev/docs/quickstart.md): Your first BuildKit project in 5 minutes
- [Core Concepts](https://buildkit.dev/docs/concepts.md): Understanding tasks, pipelines, and environments

## Commands

- [build](https://buildkit.dev/docs/commands/build.md): Build your project with automatic dependency detection
- [test](https://buildkit.dev/docs/commands/test.md): Run tests with parallel execution
- [deploy](https://buildkit.dev/docs/commands/deploy.md): Deploy to staging or production
- [watch](https://buildkit.dev/docs/commands/watch.md): Watch for changes and rebuild automatically
- [All Commands](https://buildkit.dev/docs/commands/): Complete command reference

## Configuration

- [buildkit.yml](https://buildkit.dev/docs/config.md): Configuration file reference
- [Environment Variables](https://buildkit.dev/docs/env.md): Environment-specific configuration
- [Plugins](https://buildkit.dev/docs/plugins.md): Extending BuildKit with custom plugins

## Examples

- [Node.js Projects](https://buildkit.dev/examples/nodejs.md): Building and deploying Node.js apps
- [Python Projects](https://buildkit.dev/examples/python.md): Python application workflows
- [Monorepos](https://buildkit.dev/examples/monorepo.md): Managing multiple packages
- [CI/CD Integration](https://buildkit.dev/examples/ci.md): Using BuildKit in CI/CD pipelines

## Optional

- [BuildKit Blog](https://buildkit.dev/blog/): Tutorials and case studies
- [Plugin Directory](https://buildkit.dev/plugins/): Community plugins
- [Troubleshooting](https://buildkit.dev/docs/troubleshooting.md): Common issues and solutions
```

### Why This Structure?

- **Principles**: Shows design philosophy upfront
- **Getting Started**: Installation and quickstart are priority for CLI tools
- **Commands**: Individual command documentation (most important for CLI tools)
- **Configuration**: Clear section for config files and customization
- **Examples**: Language/framework-specific guides
- **Optional**: Community resources and troubleshooting

---

## Example 3: Web Framework

### Project Context
A web framework called "FastWeb" for building modern web applications.

### Generated llms.txt

```markdown
# FastWeb

> FastWeb is a modern web framework for building full-stack applications with Python.
> It provides server-side rendering, API routes, and built-in database support with
> zero configuration required.

FastWeb features:
- File-based routing with automatic code splitting
- Server-side rendering (SSR) and static site generation (SSG)
- Built-in API routes and middleware
- Real-time capabilities with WebSockets
- TypeScript-first with excellent type inference

## Documentation

- [Getting Started](https://fastweb.dev/docs/getting-started.md): Create your first FastWeb app
- [Routing](https://fastweb.dev/docs/routing.md): File-based routing and dynamic routes
- [Data Fetching](https://fastweb.dev/docs/data.md): Loading data on server and client
- [Rendering](https://fastweb.dev/docs/rendering.md): SSR, SSG, and client-side rendering
- [API Routes](https://fastweb.dev/docs/api.md): Building REST and GraphQL APIs

## Guides

- [Authentication](https://fastweb.dev/guides/auth.md): User authentication and authorization
- [Database Integration](https://fastweb.dev/guides/database.md): Working with databases
- [Deployment](https://fastweb.dev/guides/deployment.md): Deploying to production
- [Testing](https://fastweb.dev/guides/testing.md): Unit and integration testing
- [Performance](https://fastweb.dev/guides/performance.md): Optimization best practices

## API Reference

- [Configuration](https://fastweb.dev/api/config.md): fastweb.config.js options
- [CLI](https://fastweb.dev/api/cli.md): Command-line interface reference
- [Components](https://fastweb.dev/api/components.md): Built-in components
- [Hooks](https://fastweb.dev/api/hooks.md): React-style hooks API
- [Utilities](https://fastweb.dev/api/utils.md): Helper functions and utilities

## Examples

- [Blog](https://fastweb.dev/examples/blog.md): Building a blog with markdown
- [E-commerce](https://fastweb.dev/examples/ecommerce.md): Product catalog and checkout
- [Dashboard](https://fastweb.dev/examples/dashboard.md): Admin dashboard with charts
- [Real-time Chat](https://fastweb.dev/examples/chat.md): WebSocket-based chat app

## Integrations

- [Databases](https://fastweb.dev/integrations/databases.md): PostgreSQL, MySQL, MongoDB
- [CSS Frameworks](https://fastweb.dev/integrations/css.md): Tailwind, Bootstrap, etc.
- [Analytics](https://fastweb.dev/integrations/analytics.md): Google Analytics, Plausible
- [CMS](https://fastweb.dev/integrations/cms.md): Headless CMS integrations

## Optional

- [FastWeb Blog](https://fastweb.dev/blog/): Tutorials and announcements
- [Showcase](https://fastweb.dev/showcase/): Sites built with FastWeb
- [Community](https://fastweb.dev/community/): Discord, GitHub discussions
- [Changelog](https://fastweb.dev/changelog/): Version history
```

### Why This Structure?

- **Framework Features**: Lists core capabilities upfront
- **Documentation**: Core framework concepts and features
- **Guides**: Task-oriented how-to guides (authentication, deployment, etc.)
- **API Reference**: Technical reference for configuration and APIs
- **Examples**: Complete application examples
- **Integrations**: Third-party tool integration guides
- **Optional**: Community and showcase resources

---

## Example 4: Claude Skill

### Project Context
A Claude skill for optimizing documentation (this project!).

### Generated llms.txt

```markdown
# c7score-optimizer

> A Claude skill that optimizes project documentation and README files to score highly
> on Context7's c7score benchmark, making docs more effective for AI-assisted coding tools.
> Also generates llms.txt files for projects.

The skill provides:
- Documentation analysis and quality assessment
- Question-driven content restructuring
- Code snippet enhancement with context
- llms.txt file generation
- Python analysis script for automated scanning

## Documentation

- [README](https://github.com/example/c7score-optimizer/blob/main/README.md): Overview, installation, and usage
- [Skill Definition](https://github.com/example/c7score-optimizer/blob/main/SKILL.md): Complete skill workflow and instructions
- [Changelog](https://github.com/example/c7score-optimizer/blob/main/CHANGELOG.md): Version history and updates

## Reference Materials

- [C7Score Metrics](https://github.com/example/c7score-optimizer/blob/main/references/c7score_metrics.md): Understanding the c7score benchmark
- [Optimization Patterns](https://github.com/example/c7score-optimizer/blob/main/references/optimization_patterns.md): 20+ transformation patterns
- [llms.txt Format](https://github.com/example/c7score-optimizer/blob/main/references/llmstxt_format.md): Complete llms.txt specification

## Examples

- [README Optimization](https://github.com/example/c7score-optimizer/blob/main/examples/sample_readme.md): Before/after documentation transformation
- [llms.txt Generation](https://github.com/example/c7score-optimizer/blob/main/examples/sample_llmstxt.md): Generated llms.txt examples

## Development

- [Analysis Script](https://github.com/example/c7score-optimizer/blob/main/scripts/analyze_docs.py): Python tool for documentation scanning
- [Contributing](https://github.com/example/c7score-optimizer/blob/main/CONTRIBUTING.md): How to contribute improvements

## Optional

- [Context7 c7score](https://www.context7.ai/c7score): Official c7score benchmark
- [llmstxt.org](https://llmstxt.org/): Official llms.txt specification
- [Claude Code Docs](https://docs.claude.com/claude-code): Claude Code documentation
```

### Why This Structure?

- **Skill Capabilities**: Clear explanation of what the skill does
- **Documentation**: Essential files (README, SKILL.md, CHANGELOG)
- **Reference Materials**: Detailed specifications and patterns
- **Examples**: Practical before/after demonstrations
- **Development**: Tools and contribution guides
- **Optional**: External resources and official documentation

---

## Key Patterns Across All Examples

### 1. Strong Opening
Every example has:
- Clear H1 with project name
- Informative blockquote explaining what it is
- Key features/principles in bullets

### 2. Logical Section Progression
Common pattern:
1. **Getting Started / Documentation** (high priority)
2. **API / Commands / Core Features** (high priority)
3. **Guides / Examples** (practical applications)
4. **Development / Contributing** (for contributors)
5. **Optional** (secondary resources)

### 3. Descriptive Links
All links include:
- Clear, action-oriented titles
- Helpful descriptions after colons
- Context about what each resource contains

### 4. Full URLs
All examples use complete URLs with protocol:
- ✅ `https://example.com/docs/guide.md`
- ❌ `/docs/guide.md`
- ❌ `../guide.md`

### 5. Markdown-First
Prefer linking to `.md` files:
- ✅ `docs/guide.md`
- ⚠️ `docs/guide.html` (acceptable if no .md available)

---

## Decision Tree: What Sections to Include?

### For Libraries/Packages
- **Must have**: Documentation, API Reference, Examples
- **Should have**: Getting Started, Development
- **Nice to have**: Guides, Integrations, Optional

### For CLI Tools
- **Must have**: Getting Started, Commands, Examples
- **Should have**: Configuration, Development
- **Nice to have**: Plugins, Troubleshooting, Optional

### For Frameworks
- **Must have**: Documentation, Guides, API Reference, Examples
- **Should have**: Integrations, Getting Started
- **Nice to have**: Showcase, Optional

### For Skills/Plugins
- **Must have**: Documentation, Reference Materials
- **Should have**: Examples, Development
- **Nice to have**: Optional (external resources)

---

## Common Customizations by Project Type

### Open Source Project
Add to Optional:
- Contributing guide
- Code of conduct
- Governance
- Roadmap

### Commercial Product
Add sections:
- Pricing/Plans
- Support
- Enterprise features
- Migration guides

### Educational Resource
Add sections:
- Tutorials
- Video courses
- Exercises
- Certification

### Research Project
Add sections:
- Papers
- Datasets
- Experiments
- Citations

---

## Anti-Patterns to Avoid

### ❌ Too Granular
```markdown
## Installation
- [macOS Install](url)
- [Linux Install](url)
- [Windows Install](url)
- [Docker Install](url)
```
Better: One "Installation" link covering all platforms

### ❌ No Descriptions
```markdown
- [Guide](url)
- [Docs](url)
- [API](url)
```
Better: Add helpful context after colons

### ❌ Outdated Links
```markdown
- [Guide](https://example.com/v1/guide.md)
```
Better: Link to latest version or version-agnostic URLs

### ❌ Relative URLs
```markdown
- [Guide](../docs/guide.md)
```
Better: Use full URLs with protocol

### ❌ Too Much Content
Don't paste entire documentation. Link to it.

---

Use these examples as templates when generating llms.txt files for different project types!
