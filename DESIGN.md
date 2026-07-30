# Design — Project Identity

> This document is project-long-lived. Tokens are not changed without
> the Architect's approval. Developers MUST use these tokens
> instead of improvising their own colors/spacings.

## Style Direction

Dramatisches Rot-Schwarz mit warmen Goldakzenten – wie ein exklusiver Backstage-Bereich mit Samtvorhängen und Scheinwerferlicht. Edle Serifen-Typografie und bilddominierte Karten lassen die Garderobe wie eine VIP-Kollektion wirken.

## Colors

- `--color-bg`: **#0D0B0B**
- `--color-bg_elevated`: **#1A1616**
- `--color-bg_card`: **#201B1B**
- `--color-fg`: **#F5F0EB**
- `--color-fg_muted`: **#A89E94**
- `--color-accent`: **#C41E3A**
- `--color-accent_hover`: **#E0243F**
- `--color-gold`: **#D4A843**
- `--color-gold_hover`: **#E8C25A**
- `--color-gold_light`: **#F5E6B8**
- `--color-border`: **#3A3230**
- `--color-border_focus`: **#C41E3A**
- `--color-success`: **#2E8B57**
- `--color-danger`: **#C41E3A**
- `--color-overlay`: **rgba(0,0,0,0.75)**
- `--color-spotlight`: **rgba(212,168,67,0.08)**

## Typography

- `font_family`: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- `heading_family`: 'Playfair Display', 'Times New Roman', Georgia, serif
- `heading_weight`: 700
- `body_weight`: 400
- `size_scale`: xs: 0.75rem; sm: 0.875rem; base: 1rem; lg: 1.125rem; xl: 1.5rem; 2xl: 2rem; 3xl: 2.75rem

## Spacing Scale

- `--space-0`: 4px
- `--space-1`: 8px
- `--space-2`: 12px
- `--space-3`: 16px
- `--space-4`: 24px
- `--space-5`: 32px
- `--space-6`: 48px
- `--space-7`: 64px

## Border-Radii

- `--radius-sm`: 4px
- `--radius-md`: 8px
- `--radius-lg`: 16px
- `--radius-pill`: 999px

## Components

### Button/Primary

Hintergrund: linear-gradient(135deg, #D4A843, #C49A36). Textfarbe: #0D0B0B. Schrift: Inter, weight 600, 0.875rem. Padding: 12px 24px. Border: none. Radius: md (8px). Min-Höhe: 44px (Touch). Cursor: pointer. Hover: linear-gradient(135deg, #E8C25A, #D4A843), box-shadow 0 4px 20px rgba(212,168,67,0.35). Active: transform scale(0.97), brightness 0.9. Disabled: opacity 0.4, cursor not-allowed, kein Hover-Effekt. Fokus: outline 2px solid #F5E6B8, outline-offset 2px. Übergang: all 0.2s ease.

### Button/Secondary

Hintergrund: transparent. Textfarbe: #F5F0EB. Rand: 1.5px solid #D4A843. Schrift: Inter, weight 500, 0.875rem. Padding: 12px 24px. Radius: md (8px). Min-Höhe: 44px. Hover: Hintergrund rgba(212,168,67,0.1), border #E8C25A. Active: transform scale(0.97). Disabled: opacity 0.4. Fokus: outline 2px solid #D4A843, outline-offset 2px.

### Button/Danger

Hintergrund: #C41E3A. Textfarbe: #F5F0EB. Schrift: Inter, weight 500, 0.875rem. Padding: 12px 24px. Radius: md (8px). Min-Höhe: 44px. Hover: Hintergrund #E0243F, box-shadow 0 4px 16px rgba(196,30,58,0.4). Active: transform scale(0.97). Disabled: opacity 0.4.

### Card/Garment

Hintergrund: #201B1B. Border: 1px solid #3A3230. Radius: lg (16px). Overflow: hidden. Bildbereich: Seitenverhältnis 3:4, object-fit cover, Hintergrund #1A1616 mit dezentem gold-Spotlight-Verlauf als Platzhalter. Textbereich: padding 16px. Titel: Playfair Display, weight 600, 1.125rem, Farbe #F5F0EB. Kategorie-Badge: inline, Hintergrund rgba(196,30,58,0.2), Text #C41E3A, Schrift Inter 0.75rem, weight 500, padding 2px 10px, radius pill. Hover: border #D4A843, box-shadow 0 8px 32px rgba(0,0,0,0.5), transform translateY(-2px), Übergang all 0.3s ease. Aktionen (Edit/Löschen): absolut positioniert oben rechts, erscheinen nur bei Hover (opacity 0→1).

### Input

Hintergrund: #1A1616. Textfarbe: #F5F0EB. Placeholder: #A89E94. Rand: 1.5px solid #3A3230. Radius: md (8px). Padding: 12px 16px. Schrift: Inter, 0.875rem. Min-Höhe: 44px. Fokus: border #C41E3A, box-shadow 0 0 0 3px rgba(196,30,58,0.25), outline none. Fehler: border #C41E3A, box-shadow 0 0 0 3px rgba(196,30,58,0.15). Disabled: opacity 0.5, cursor not-allowed. Label: Schrift Inter, weight 500, 0.75rem, Farbe #A89E94, margin-bottom 6px, Texttransform uppercase, letter-spacing 0.05em.

### FilterPill

Hintergrund: transparent. Textfarbe: #A89E94. Rand: 1px solid #3A3230. Schrift: Inter, weight 500, 0.8125rem. Padding: 6px 16px. Radius: pill (999px). Min-Höhe: 36px. Cursor: pointer. Hover: border #C41E3A, Textfarbe #F5F0EB. Aktiv (ausgewählt): Hintergrund #C41E3A, border #C41E3A, Textfarbe #F5F0EB, weight 600. Übergang: all 0.2s ease.

### Modal

Overlay: rgba(0,0,0,0.75), backdrop-filter blur(4px). Modal-Box: Hintergrund #1A1616, border 1px solid #3A3230, radius lg (16px), padding 32px, max-width 480px, width calc(100% - 32px). Schatten: 0 24px 80px rgba(0,0,0,0.7). Titel: Playfair Display, weight 700, 1.5rem, Farbe #F5F0EB, margin-bottom 24px. Schließen-Button: Icon X, Farbe #A89E94, position absolut oben rechts 16px, hover Farbe #F5F0EB. Animation: fadeIn 0.2s ease, slideUp 0.25s ease.

### Nav/TopBar

Hintergrund: #0D0B0B mit 80% Deckkraft, backdrop-filter blur(12px). Border-bottom: 1px solid #3A3230. Höhe: 64px. Padding: 0 24px. Logo/App-Name: Playfair Display, weight 700, 1.5rem, Farbe #F5F0EB, goldener Unterstrich-Akzent 2px (#D4A843). Navigation-Links: Inter, weight 500, 0.875rem, Farbe #A89E94, Abstand 32px. Hover: Farbe #F5F0EB. Aktiv: Farbe #D4A843. User-Menü: Avatar-Kreis 36px, Hintergrund #C41E3A, Initialen in #F5F0EB. Sticky: position sticky, top 0, z-index 50.

### AuthCard

Zentriert auf Seite (Login/Registrierung). Max-width: 420px. Hintergrund: #1A1616, border 1px solid #3A3230, radius lg (16px), padding 40px. Schatten: 0 24px 80px rgba(0,0,0,0.6). Titel: Playfair Display, weight 700, 2rem, Farbe #F5F0EB, text-align center, margin-bottom 8px. Subtitel: Inter, 0.875rem, Farbe #A89E94, text-align center, margin-bottom 32px. Goldener Trennstrich: 40px breit, 2px hoch, #D4A843, margin 0 auto 32px. Link/Wechsel zwischen Login↔Registrierung: Farbe #D4A843, hover underline.

### EmptyState

Zentriert im Content-Bereich. Icon/Illustration: stilisierter Kleiderbügel in #3A3230, 64px. Titel: Playfair Display, weight 600, 1.5rem, Farbe #F5F0EB. Beschreibung: Inter, 1rem, Farbe #A89E94, max-width 360px. CTA-Button: Primary Button (s.o.). Abstand: 24px zwischen Elementen.

### FileUpload

Dropzone: Hintergrund #1A1616, border 2px dashed #3A3230, radius md (8px), padding 32px, text-align center. Icon: Kamera/Upload in #A89E94, 32px. Text: Inter 0.875rem, Farbe #A89E94. Hover/Aktiv: border #D4A843, Hintergrund rgba(212,168,67,0.05). Vorschau: Bild 120x160px, radius sm (4px), border 1px solid #3A3230. Entfernen-Button: X-Icon, Farbe #C41E3A, hover #E0243F.

## Layout Principles

- Container max-width: 1200px, horizontal zentriert, padding 16px an den Seiten (Mobile) / 32px (Desktop).
- Breakpoints: Mobile < 640px, Tablet 640–1024px, Desktop ≥ 1024px.
- Garderoben-Grid: 1 Spalte (Mobile), 2 Spalten (Tablet), 3 Spalten (Desktop), gap 24px. Auf großen Screens (≥1400px) 4 Spalten.
- Kategorie-Filter: horizontal scrollbar auf Mobile (overflow-x: auto, hide scrollbar), zentriert auf Desktop. Padding 8px 0, margin-bottom 24px.
- Seitenlayout: TopBar (fixed) + Hauptbereich (padding-top 64px + 32px). Hauptbereich min-height: calc(100vh - 64px).
- Formulare: Labels oben, Inputs darunter, vertikaler Abstand 20px zwischen Feldern. Submit-Button mit margin-top 24px, volle Breite auf Mobile.
- Card-Hover: sanfte Erhöhung (translateY -2px) mit gold-glow Schatten – vermittelt Exklusivität und Entdeckungsfreude.
- Gold-Akzente sparsam einsetzen: nur für primäre CTAs, aktive Navigation, Trennlinien und Card-Hover – nicht inflationär.
