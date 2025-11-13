# Changelog

All notable changes to the LLM Docs Optimizer plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.3.0] - 2025-11-12 (CURRENT)

### Added - Automated Scoring
- **Automated C7Score Evaluation**: Claude-based scoring across all 5 metrics
- **Before/After Comparison**: Detailed score breakdowns showing improvement
- **Comprehensive Scoring Rubrics**: Added evaluation guidelines to c7score_metrics.md
- **Measurable Feedback**: Numeric quality assessment (e.g., 45 → 89/100)
- Scoring integrated into Step 6 of optimization workflow

### Changed - Major Updates
- **Renamed to llm-docs-optimizer** (formerly c7score-optimizer)
  - Broader positioning as general LLM documentation toolkit
  - Better discoverability and clearer purpose
  - All features retained
- **Converted to Claude Code Plugin format** for marketplace distribution
  - Created `.claude-plugin/plugin.json` manifest
  - Restructured to `skills/llm-docs-optimizer/` nested format
  - Easy installation: `/plugin marketplace add owner/llm-docs-optimizer`

### Added
- Plugin manifest (`.claude-plugin/plugin.json`)
- Marketplace manifest (`.claude-plugin/marketplace.json`) for distribution
- Marketplace-ready structure with flat plugin layout
- Updated installation documentation with two-step process

### Removed
- `skill.json` (replaced by `.claude-plugin/plugin.json`)

---

## [1.1.0] - 2025-11-12

### Added - llms.txt Generation
- **llms.txt file generation** for LLM-friendly project navigation
- Comprehensive format specification (`references/llmstxt_format.md`)
- Project type templates (`examples/sample_llmstxt.md`):
  - Python libraries
  - CLI tools
  - Web frameworks
  - Claude skills
- Complete workflow in SKILL.md:
  - Project structure analysis
  - Automatic project type detection
  - Template selection
  - URL formatting and validation
- Integration with c7score optimization
- Ask user if they want llms.txt when optimizing docs

### Changed
- Updated skill description to include llms.txt capability
- Enhanced README with llms.txt documentation
- Added triggers: "create llms.txt", "generate llms txt", "llmstxt"
- Enhanced keywords with llms-txt related terms

### Documentation
- Complete llms.txt specification with real-world examples
- Before/after examples for different project types
- Decision trees for section selection
- Anti-patterns and best practices

---

## [1.0.0] - 2025-11-11

### Added - Initial Release
- **C7Score documentation optimization**
- Complete skill implementation with structured workflow
- Documentation analysis and quality assessment
- Question-driven content restructuring
- Code snippet enhancement with context
- Python analysis script (`analyze_docs.py`)
- Comprehensive reference materials:
  - `c7score_metrics.md` - Detailed benchmark metrics
  - `optimization_patterns.md` - 20+ transformation patterns
- Support for all five c7score metrics:
  - Question-Snippet Matching (80%)
  - LLM Evaluation (10%)
  - Formatting (5%)
  - Metadata Removal (2.5%)
  - Initialization Examples (2.5%)
- README with installation and usage instructions
- MIT License
- Example documentation (before/after)

### Features
- Automatic skill activation via trigger phrases
- Multi-phase optimization workflow (analyze, optimize, review)
- Integration with Claude Code
- Extensible pattern library
- Support for markdown documentation

---

## [Unreleased] - Future Versions

### Planned for 1.4.0
- [ ] Support for additional documentation formats (RST, AsciiDoc)
- [ ] Integration with c7score API for official scoring (optional)
- [ ] Automated testing and validation
- [ ] Multi-language documentation support
- [ ] Enhanced error handling in analysis script
- [ ] Automated llms.txt validation against llmstxt.org spec

### Planned for 1.5.0
- [ ] Interactive mode for step-by-step optimization
- [ ] Custom pattern library support
- [ ] Documentation templates for common project types
- [ ] Performance improvements for large documentation sets
- [ ] llms.txt update detection and regeneration
- [ ] Submit to official Anthropic skills marketplace
- [ ] Community marketplace submissions

---

[1.3.0]: https://github.com/yourusername/llm-docs-optimizer/releases/tag/v1.3.0
[1.1.0]: https://github.com/yourusername/llm-docs-optimizer/releases/tag/v1.1.0
[1.0.0]: https://github.com/yourusername/llm-docs-optimizer/releases/tag/v1.0.0
