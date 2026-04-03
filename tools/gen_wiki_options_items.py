# -*- coding: utf-8 -*-
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _SCRIPT_DIR.parent
_MACRO_MANAGER_CANDIDATES = (
    Path(r"D:/workspace/2025/novo/ClassicUO/src/ClassicUO.Client/Game/Managers/MacroManager.cs"),
    _REPO_ROOT / "ClassicUO" / "src" / "ClassicUO.Client" / "Game" / "Managers" / "MacroManager.cs",
)

_SKIP_MACRO_TYPE = frozenset({"None"})
_SKIP_MACRO_SUBTYPE = frozenset(
    {"MSC_NONE", "MscTotalCount", "INVALID_0", "INVALID_1", "INVALID_2", "INVALID_3"}
)


def _find_macro_manager_path():
    for p in _MACRO_MANAGER_CANDIDATES:
        if p.is_file():
            return p
    return None


def _parse_csharp_enum(lines, enum_name):
    needle = f"enum {enum_name}"
    start = next((i for i, line in enumerate(lines) if needle in line), None)
    if start is None:
        return []
    k = start
    while k < len(lines) and "{" not in lines[k]:
        k += 1
    if k >= len(lines):
        return []
    out = []
    for line in lines[k + 1 :]:
        st = line.strip()
        if st == "}":
            break
        if not st or st.startswith("#"):
            continue
        before = st.split("//", 1)[0].strip()
        if not before:
            continue
        before = before.rstrip(",").strip()
        if not before:
            continue
        if "=" in before:
            ident = before.split("=", 1)[0].strip()
        else:
            ident = before.split()[0]
        if ident and (ident[0].isalpha() or ident.startswith("_")):
            out.append(ident)
    return out


def _load_macro_enums():
    path = _find_macro_manager_path()
    if path is None:
        return None, [], []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    return path, _parse_csharp_enum(lines, "MacroType"), _parse_csharp_enum(lines, "MacroSubType")


def ph(tab, name):
    return (
        f'<div class="wiki-media-placeholder wiki-media-placeholder--item wiki-media-placeholder--video">'
        f"Video — Options · {tab} · {name}</div>"
    )


def item(tab, title, desc):
    return (
        f'<div class="wiki-opt-item">\n'
        f"<p><strong>{title}</strong> — {desc}</p>\n"
        f"{ph(tab, title)}\n"
        f"</div>\n"
    )


def sec(h):
    return f'<h3>{h}</h3>\n'


def page(pid, title, intro, sections):
    body = "".join(sections)
    return (
        f'      <details class="wiki-article" id="{pid}">\n'
        f'        <summary><span class="wiki-article-title">{title}</span></summary>\n'
        f'        <div class="wiki-article-body">\n'
        f"        <p>{intro}</p>\n"
        f"{body}"
        f"        </div>\n"
        f"      </details>\n\n"
    )


def main():
    out = []
    out.append(
        page(
            "wiki-opt-general",
            "General (Options)",
            "ClassicUO <code>BuildGeneral()</code> — movement, corpses, mobiles, gumps, drag-select, circle of transparency, terrain.",
            [
                sec("General"),
                item(
                    "General",
                    "Highlight game objects",
                    "Outlines interactive objects under the cursor for easier targeting.",
                ),
                item(
                    "General",
                    "Enable pathfinding",
                    "Click-to-walk uses the client pathfinder through obstacles.",
                ),
                item(
                    "General",
                    "Shift + pathfinding",
                    "Require holding Shift for pathfind clicks so normal clicks stay precise.",
                ),
                item(
                    "General",
                    "Single click pathfind",
                    "One click triggers pathfinding instead of double-click walk.",
                ),
                item(
                    "General",
                    "Always run",
                    "Default movement uses run speed where the server allows.",
                ),
                item(
                    "General",
                    "Always run unless hidden",
                    "Walk while hidden; run otherwise.",
                ),
                item(
                    "General",
                    "Auto open doors",
                    "Automatically open doors when you walk into them.",
                ),
                item(
                    "General",
                    "Smooth doors",
                    "Animate door opening/closing instead of instant state swap.",
                ),
                item(
                    "General",
                    "Fast rotation",
                    "Faster character facing changes.",
                ),
                item(
                    "General",
                    "Auto open corpses",
                    "Opens corpse containers when you step on them.",
                ),
                item(
                    "General",
                    "Corpse open range",
                    "Numeric max distance (tiles) for auto-open corpse.",
                ),
                item(
                    "General",
                    "Skip empty corpses",
                    "Do not open corpses that have no loot.",
                ),
                item(
                    "General",
                    "Corpse open options",
                    "Combo: when to skip — none / not targeting / not hidden / both.",
                ),
                item(
                    "General",
                    "No color for out-of-range objects",
                    "Dims or removes tint on objects beyond interaction range.",
                ),
                item(
                    "General",
                    "Sallos easy grab",
                    "Easier grab/drag behaviour for items (Orion/Sallos style).",
                ),
                item(
                    "General",
                    "Show houses content",
                    "Shows items inside houses when supported by client version.",
                ),
                item(
                    "General",
                    "Smooth boat movement",
                    "Interpolates boat motion on supported shards.",
                ),
                sec("Mobiles"),
                item(
                    "General · Mobiles",
                    "Show mobile HP",
                    "Displays HP on mobiles; pair with mode (percentage / line / both).",
                ),
                item(
                    "General · Mobiles",
                    "Mobile HP mode",
                    "Combo: percentage text, bar line, or both.",
                ),
                item(
                    "General · Mobiles",
                    "Show HP when",
                    "Combo: always / below max / smart hiding rules.",
                ),
                item(
                    "General · Mobiles",
                    "Highlight poisoned",
                    "Tint poisoned mobiles; set poison hue.",
                ),
                item(
                    "General · Mobiles",
                    "Highlight paralyzed",
                    "Tint paralyzed mobiles; set paralyze hue.",
                ),
                item(
                    "General · Mobiles",
                    "Highlight invulnerable",
                    "Tint invulnerable mobiles; set invuln hue.",
                ),
                item(
                    "General · Mobiles",
                    "Show incoming mobile names",
                    "Overhead/name for mobiles entering screen.",
                ),
                item(
                    "General · Mobiles",
                    "Show incoming corpse names",
                    "Notification-style name for new corpses.",
                ),
                item(
                    "General · Mobiles",
                    "Aura under feet",
                    "Combo: none / warmode / Ctrl+Shift / always.",
                ),
                item(
                    "General · Mobiles",
                    "Party aura custom color",
                    "Enable party member foot aura and pick hue.",
                ),
                sec("Gumps & context"),
                item(
                    "General · Gumps",
                    "Disable game menu (top bar)",
                    "Hides the ClassicUO top menu bar.",
                ),
                item(
                    "General · Gumps",
                    "Hold Alt to close anchored gumps",
                    "Alt-click behaviour on anchored UI.",
                ),
                item(
                    "General · Gumps",
                    "Hold Alt to move gumps",
                    "Move gumps while Alt is held.",
                ),
                item(
                    "General · Gumps",
                    "Right-click closes anchored group",
                    "Closes all gumps in an anchor chain with one right-click.",
                ),
                item(
                    "General · Gumps",
                    "Standard skills gump",
                    "Use classic skills window layout.",
                ),
                item(
                    "General · Gumps",
                    "Use old status gump",
                    "Legacy status layout (hidden on some builds e.g. Outlands).",
                ),
                item(
                    "General · Gumps",
                    "Party invite gump",
                    "Show party invitation dialog.",
                ),
                item(
                    "General · Gumps",
                    "Custom HP bars",
                    "Use ClassicUO custom health bar gumps.",
                ),
                item(
                    "General · Gumps",
                    "Custom HP bar black background",
                    "Solid black backing for custom bars.",
                ),
                item(
                    "General · Gumps",
                    "Save HP bars on logout",
                    "Restore bar positions next session.",
                ),
                item(
                    "General · Gumps",
                    "Close HP bar when",
                    "Combo: never / out of range / mobile dead.",
                ),
                item(
                    "General · Gumps",
                    "Grid loot",
                    "Combo for looting into grid vs legacy — none / grid only / both.",
                ),
                item(
                    "General · Gumps",
                    "Shift for context menu",
                    "Require Shift+click for context menus.",
                ),
                item(
                    "General · Gumps",
                    "Shift to split stack",
                    "Require Shift when splitting item piles.",
                ),
                sec("Miscellaneous"),
                item(
                    "General · Misc",
                    "Circle of transparency",
                    "Enable circular transparency around player; radius slider.",
                ),
                item(
                    "General · Misc",
                    "Circle of transparency type",
                    "Combo: full / gradient / modern style.",
                ),
                item(
                    "General · Misc",
                    "Hide screenshot stored message",
                    "Suppress system message after saving a screenshot.",
                ),
                item(
                    "General · Misc",
                    "Object alpha fading",
                    "Fade objects in/out when they appear or leave.",
                ),
                item(
                    "General · Misc",
                    "Text alpha fading",
                    "Fade overhead/journal-style text.",
                ),
                item(
                    "General · Misc",
                    "Drag-select (mass health bars)",
                    "Drag a rectangle to select many mobiles and spawn bars; modifier key combo.",
                ),
                item(
                    "General · Misc",
                    "Drag-select — select players key",
                    "Ctrl / Shift / disabled for player selection pass.",
                ),
                item(
                    "General · Misc",
                    "Drag-select — select monsters key",
                    "Ctrl / Shift / disabled for monster pass.",
                ),
                item(
                    "General · Misc",
                    "Drag-select — nameplates key",
                    "Ctrl / Shift / disabled for nameplate pass.",
                ),
                item(
                    "General · Misc",
                    "Drag-select start position X / Y",
                    "Sliders for rectangle origin on screen.",
                ),
                item(
                    "General · Misc",
                    "Drag-select anchored health bars",
                    "Spawned bars from drag-select participate in anchoring.",
                ),
                item(
                    "General · Misc",
                    "Show stats changed message",
                    "System message when STR/DEX/INT changes.",
                ),
                item(
                    "General · Misc",
                    "Show skills changed message",
                    "Notify on skill gains/changes; delta threshold slider.",
                ),
                sec("Terrain & statics"),
                item(
                    "General · Terrain",
                    "Hide roof tiles",
                    "Do not draw upper-floor roofs (classic UO visibility trick).",
                ),
                item(
                    "General · Terrain",
                    "Hide vegetation",
                    "Hide grass/foliage statics for clarity.",
                ),
                item(
                    "General · Terrain",
                    "Mark cave tiles",
                    "Highlight cave floor edges.",
                ),
                item(
                    "General · Terrain",
                    "Fields drawing",
                    "Combo: normal / static / tile mode for field spells.",
                ),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-sounds",
            "Sounds (Options)",
            "ClassicUO <code>BuildSounds()</code>.",
            [
                item("Sounds", "Enable sounds", "Master toggle for game SFX."),
                item("Sounds", "Enable music", "In-game music playback."),
                item("Sounds", "Login music", "Music on login screen (global setting)."),
                item("Sounds", "Sound volume", "Slider 0–100 for SFX."),
                item("Sounds", "Music volume", "Slider 0–100 for in-game music."),
                item("Sounds", "Login music volume", "Slider for login theme."),
                item("Sounds", "Footsteps", "Play footstep samples."),
                item("Sounds", "Combat music", "Switch to combat music when in fight."),
                item(
                    "Sounds",
                    "Sounds/music in background",
                    "Continue audio when the window loses focus.",
                ),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-video",
            "Video (Options)",
            "ClassicUO <code>BuildVideo()</code> — FPS, game window, zoom, lights, misc, shadows.",
            [
                sec("Performance"),
                item("Video", "FPS limit", "Slider caps frames per second."),
                item(
                    "Video",
                    "Reduce FPS when inactive",
                    "Lower FPS while the window is in background.",
                ),
                item(
                    "Video",
                    "VSync",
                    "Sync to monitor refresh (caps FPS to display rate).",
                ),
                sec("Game window"),
                item("Video", "Always full-size game window", "Maximize play area within client window."),
                item("Video", "Borderless window", "Remove OS window frame."),
                item(
                    "Video",
                    "Custom border frame (borderless)",
                    "Draw a custom frame when borderless.",
                ),
                item("Video", "Lock game window", "Prevent moving/resizing the play area."),
                item("Video", "Game window position X / Y", "Pixel offset of the world view."),
                item("Video", "Game window width / height", "Size of the world view in pixels."),
                sec("Zoom"),
                item("Video", "Default zoom", "Slider picks default scale index."),
                item("Video", "Mouse wheel zoom", "Ctrl+wheel (or configured) changes zoom."),
                item(
                    "Video",
                    "Release Ctrl restores scale",
                    "Return zoom after releasing Ctrl if enabled.",
                ),
                sec("Lights"),
                item("Video", "Alternative lights", "Use alternate lighting renderer."),
                item("Video", "Custom light level", "Override global darkness; slider + type."),
                item("Video", "Light level type", "Absolute vs minimum light interpretation."),
                item("Video", "Dark nights", "Stronger night darkness."),
                item("Video", "Colored lights", "Tint light sources."),
                sec("Misc"),
                item("Video", "Death screen", "Full-screen effect on death."),
                item("Video", "Black & white when dead", "Desaturate world while ghost."),
                item(
                    "Video",
                    "Run mouse in separate thread",
                    "Input polling on another thread (global).",
                ),
                item("Video", "Aura on mouse target", "Show aura on target under cursor."),
                item("Video", "Animated water", "Animate water tiles."),
                sec("Shadows"),
                item("Video", "Enable shadows", "Draw mobile shadows."),
                item("Video", "Shadow statics", "Also shadow large statics."),
                item("Video", "Terrain shadow level", "Slider for ground shadow strength."),
            ],
        )
    )

    mm_path, macro_types, macro_subs = _load_macro_enums()
    macro_intro = (
        "ClassicUO <code>OptionsGump</code> macro list plus <code>MacroControl</code> editor; "
        "action types match <code>MacroManager</code> enums."
    )
    if mm_path is not None:
        macro_intro += (
            f' Parsed from <code class="wiki-path">{mm_path}</code>.'
        )
    macro_sections = [
        sec("Macro list (Options gump)"),
        item("Macros", "New macro", "Opens dialog to name and create a macro."),
        item("Macros", "Delete macro", "Removes selected macro after confirmation."),
        item(
            "Macros",
            "Macro list",
            "Select a macro to edit; drag list entries to create a macro button on screen.",
        ),
        sec("Macro editor (selected macro)"),
        item("Macros", "Hotkey box", "Assign key, mouse button, wheel, or controller binding."),
        item(
            "Macros",
            "Create macro button",
            "Places a draggable macro activation button on the game UI.",
        ),
        item(
            "Macros",
            "Macro button editor",
            "Opens the in-game editor for macro button appearance and layout.",
        ),
        item("Macros", "Add", "Appends a new macro action line."),
        item("Macros", "Remove", "Removes the last macro action line."),
        item(
            "Macros",
            "Macro actions (scroll list)",
            "Scrollable list of action rows; each row is one step in the macro.",
        ),
        item(
            "Macros",
            "Per-line primary combobox",
            "Selects <code>MacroType</code> for each line.",
        ),
        item(
            "Macros",
            "Per-line secondary UI",
            "Sub-combobox, targets, text, or delay fields depending on the selected type.",
        ),
        sec("MacroType (primary combobox)"),
    ]
    for n in macro_types:
        if n in _SKIP_MACRO_TYPE:
            continue
        macro_sections.append(
            item(
                "Macros · MacroType",
                n,
                f"Primary macro action <code>{n}</code>.",
            )
        )
    macro_sections.append(sec("MacroSubType (secondary combobox)"))
    for n in macro_subs:
        if n in _SKIP_MACRO_SUBTYPE:
            continue
        macro_sections.append(
            item(
                "Macros · MacroSubType",
                n,
                f"Secondary option <code>{n}</code> when the line needs a sub-selection.",
            )
        )
    if not macro_types and not macro_subs:
        if mm_path is None:
            macro_sections.append(
                item(
                    "Macros",
                    "MacroType / MacroSubType",
                    "Point <code>_MACRO_MANAGER_CANDIDATES</code> in "
                    "<code>tools/gen_wiki_options_items.py</code> at your ClassicUO "
                    "<code>MacroManager.cs</code> and re-run the generator.",
                )
            )
        else:
            macro_sections.append(
                item(
                    "Macros",
                    "Enum parse",
                    "Could not parse <code>MacroType</code> / <code>MacroSubType</code> from MacroManager.cs.",
                )
            )

    out.append(
        page(
            "wiki-opt-macros",
            "Macros (Options)",
            macro_intro,
            macro_sections,
        )
    )

    out.append(
        page(
            "wiki-opt-tooltips",
            "Tooltips (Options)",
            "ClassicUO <code>BuildTooltip()</code> — delay, zoom, font, opacity, override menu button.",
            [
                item(
                    "Tooltips",
                    "Delay before tooltip",
                    "Milliseconds before object tooltips appear.",
                ),
                item("Tooltips", "Tooltip zoom", "Scale tooltip text/graphics."),
                item("Tooltips", "Tooltip background opacity", "Fade tooltip panel."),
                item("Tooltips", "Tooltip font", "Pick font face for tooltips."),
                item("Tooltips", "Tooltip font hue", "Color index for tooltip text."),
                item(
                    "Tooltips",
                    "Tooltip override (button)",
                    "Opens Dust765 tooltip override gump when present in fork.",
                ),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-fonts",
            "Fonts (Options)",
            "ClassicUO <code>BuildFonts()</code>.",
            [
                item("Fonts", "Override all fonts", "Force one font across UI."),
                item("Fonts", "Override font Unicode mode", "Unicode vs bitmap selection for override."),
                item("Fonts", "Chat font selector", "Font used in chat/overhead where applicable."),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-speech",
            "Speech (Options)",
            "ClassicUO <code>BuildSpeech()</code> — chat colors, speech delay, journal.",
            [
                item("Speech", "Scale speech delay", "Slider scales time between speech lines."),
                item("Speech", "Save journal to file", "Persist journal to disk."),
                item("Speech", "Speech color", "Hue for normal speech."),
                item("Speech", "Emote color", "Hue for emote messages."),
                item("Speech", "Yell color", "Hue for yell channel."),
                item("Speech", "Whisper color", "Hue for whispers."),
                item("Speech", "Party message color", "Hue for party chat."),
                item("Speech", "Guild message color", "Hue for guild chat."),
                item("Speech", "Alliance message color", "Hue for alliance chat."),
                item("Speech", "Chat message color", "Hue for general chat."),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-combat",
            "Combat & spells (Options)",
            "ClassicUO <code>BuildCombat()</code>.",
            [
                item("Combat", "Hold Tab for combat", "Tab toggles/combat mode behaviour."),
                item("Combat", "Query before attack", "Confirm criminal actions."),
                item("Combat", "Query before beneficial on criminal", "Confirm heals/buffs that flag."),
                item("Combat", "Spell overhead format", "Enable formatted spell text over caster."),
                item("Combat", "Spell overhead hue", "Color spell names in overhead."),
                item("Combat", "Spellbook single click", "Cast from UI with one click."),
                item("Combat", "Buff duration on bar", "Show timers on buff icons."),
                item("Combat", "Fast spell assignment", "Quicker drag-to-hotkey assignment."),
                item("Combat", "Innocent notoriety hue", "Mobile name/label color."),
                item("Combat", "Friend hue", "Friend notoriety color."),
                item("Combat", "Criminal hue", "Criminal color."),
                item("Combat", "Can attack hue", "Attackable gray color."),
                item("Combat", "Murderer hue", "Murderer color."),
                item("Combat", "Enemy hue", "Enemy color."),
                item("Combat", "Beneficial spell hue", "Overhead beneficial spell color."),
                item("Combat", "Harmful spell hue", "Overhead harmful spell color."),
                item("Combat", "Neutral spell hue", "Neutral spell color."),
                item("Combat", "Spell format string", "Text template for spell overhead."),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-counters",
            "Counters (Options)",
            "ClassicUO <code>BuildCounters()</code> — on-screen item counters.",
            [
                item("Counters", "Enable counters", "Show counter bar gump."),
                item("Counters", "Highlight on use", "Flash counter when item is used."),
                item("Counters", "Highlight on amount change", "Flash when count changes."),
                item("Counters", "Abbreviated amount", "Short format for large numbers."),
                item(
                    "Counters",
                    "Abbreviated amount threshold",
                    "Numeric field — abbreviate counts above this value.",
                ),
                item(
                    "Counters",
                    "Highlight red when below",
                    "Checkbox plus amount field — flash when count drops under threshold.",
                ),
                item("Counters", "Counter cell size", "Slider for each counter cell pixel size."),
                item("Counters", "Counter rows", "Input — rows in counter grid."),
                item("Counters", "Counter columns", "Input — columns in counter grid."),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-infobar",
            "InfoBar (Options)",
            "ClassicUO <code>BuildInfoBar()</code>.",
            [
                item("InfoBar", "Show info bar", "Toggle the info bar gump."),
                item(
                    "InfoBar",
                    "Show HP in title bar",
                    "Mirror HP (or stats) into the window title.",
                ),
                item(
                    "InfoBar",
                    "Data highlight type",
                    "Combo: text color vs colored bars for values.",
                ),
                item("InfoBar", "Add item", "Append a new info bar row."),
                item(
                    "InfoBar",
                    "Info bar row editor",
                    "Per row: label, color, and data source (HP, mana, etc.).",
                ),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-actionbar",
            "Action Bar (Options)",
            "ClassicUO <code>BuildActionBar()</code> in <code>OptionsGump.ActionBar.cs</code>.",
            [
                item("Action Bar", "Show action bar", "Master toggle for spell/item bar gump."),
                item(
                    "Action Bar",
                    "Add slot",
                    "Adds another spell slot row (up to max).",
                ),
                item(
                    "Action Bar",
                    "Per-slot spell drop zone",
                    "Drag spell icon into slot; hotkey box; Self/Last target; remove.",
                ),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-containers",
            "Containers (Options)",
            "ClassicUO <code>BuildContainers()</code> — non-grid container behaviour.",
            [
                item(
                    "Containers",
                    "Backpack style",
                    "Combo: default / suede / polar bear / ghoul (shard version gated).",
                ),
                item("Containers", "Container scale", "Slider scales classic container gumps."),
                item("Containers", "Scale items in container", "Resize item art inside gump."),
                item("Containers", "Use large container gumps", "Bigger art when supported."),
                item("Containers", "Double click to loot", "Loot on double-click inside container."),
                item("Containers", "Relative drag-and-drop", "DnD items relative to grab point."),
                item(
                    "Containers",
                    "Highlight container when selected",
                    "Emphasize gump under cursor.",
                ),
                item("Containers", "Hue container gumps", "Tint gump chrome."),
                item(
                    "Containers",
                    "Override container location",
                    "Checkbox plus combo: near parent / top-right / last dragged / remember each.",
                ),
                item(
                    "Containers",
                    "Rebuild containers",
                    "Button regenerates container definition file.",
                ),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-experimental",
            "Experimental (Options)",
            "ClassicUO <code>BuildExperimental()</code> — unstable features.",
            [
                item(
                    "Experimental",
                    "Disable default UO hotkeys",
                    "Turns off built-in keybinds for testing custom setups.",
                ),
                item(
                    "Experimental",
                    "Disable arrow keys for movement",
                    "Arrow keys no longer walk the player.",
                ),
                item("Experimental", "Disable Tab", "Tab key does nothing."),
                item(
                    "Experimental",
                    "Disable message history (Ctrl+Q/W)",
                    "Stops journal history hotkeys.",
                ),
                item(
                    "Experimental",
                    "Disable click-to-automove",
                    "Prevents classic single-click auto walk.",
                ),
            ],
        )
    )

    out.append(
        page(
            "wiki-opt-ignore",
            "Ignore List",
            "Button on Options sidebar opens <code>IgnoreManagerGump</code> (not a scroll page).",
            [
                item(
                    "Ignore List",
                    "Open ignore manager",
                    "Adds/edits ignored players and speech filters.",
                ),
            ],
        )
    )

    Path = __import__("pathlib").Path
    Path("tools/wiki_options_fragment.html").write_text("".join(out), encoding="utf-8")
    print("wrote tools/wiki_options_fragment.html", len(out), "pages")

    dust_intro = (
        "Dust765 <code>BuildDust()</code> (Options page 16). Each control below matches a row in the client; add screenshots or short clips per line."
    )
    d = [
        sec("Art / Hue Changes"),
        item("Dust", "Color stealth", "Tint stealth graphic; hue; neon Off/White/Pink/Ice/Fire."),
        item(
            "Dust",
            "Color energy bolt",
            "Bolt hue and neon; art Normal / alternate explo / bagball.",
        ),
        item(
            "Dust",
            "Gold art style",
            "Normal / cannonball / previous coin; optional hue for alternates.",
        ),
        item(
            "Dust",
            "Enlarge jewelry",
            "Scale rings and bracelets on paperdoll and in grid containers.",
        ),
        item(
            "Dust",
            "Tree art",
            "Normal / stump / tile; optional hue for stump or tile.",
        ),
        item(
            "Dust",
            "Blocker art",
            "Normal / stump / tile for blocking tiles; optional hue.",
        ),
        item("Dust", "Moongate recolor", "Recolor 0xF6C; preset neon or custom hue."),
        item(
            "Dust",
            "Scale monsters",
            "Ctrl+Shift on monster, +/- to resize locally (visual only).",
        ),
        sec("Title Bar"),
        item("Dust", "Window title style", "CUO native vs UOS/Orion-like title."),
        item(
            "Dust",
            "Title bar stats",
            "HP/MP/ST in title; mode Text / Percent / Progress bars (mutually exclusive).",
        ),
        sec("Visual Helpers"),
        item(
            "Dust",
            "Highlight tiles at range",
            "Ring around player; slider 1–20; hue picker.",
        ),
        item(
            "Dust",
            "Highlight tiles at range (spell)",
            "Separate ring for spell range; slider; hue.",
        ),
        item("Dust", "Preview fields", "Show field spell footprints early."),
        item("Dust", "Color own aura by HP", "Self aura tint follows health."),
        item(
            "Dust",
            "Glowing weapons",
            "Neon on weapons; Off/White/Pink/Ice/Fire/Custom + hue.",
        ),
        item(
            "Dust",
            "Highlight last target",
            "Outline LT; Off/White/Pink/Ice/Fire/Custom + hue.",
        ),
        item(
            "Dust",
            "Highlight friends / guild",
            "Outline friendly guild mobiles; presets + custom hue.",
        ),
        item(
            "Dust",
            "Last target poisoned",
            "Neon modes including Special + hue.",
        ),
        item(
            "Dust",
            "Last target paralyzed",
            "Neon modes including Special + hue.",
        ),
        item(
            "Dust",
            "Last target stunned",
            "Neon modes including Special + hue.",
        ),
        item(
            "Dust",
            "Last target mortalled",
            "Neon modes including Special + hue.",
        ),
        sec("Health Bar"),
        item("Dust", "Highlight LT on health bar", "Outline last target on bar gump."),
        item("Dust", "Highlight health bar by state", "State-based bar emphasis."),
        sec("Cursor"),
        item("Dust", "Spells on cursor", "Show spell icon at cursor; offset X/Y fields."),
        item("Dust", "Color game cursor when targeting", "Tint targeting cursor."),
        item(
            "Dust",
            "Show target range indicator",
            "Range circle overlay while targeting.",
        ),
        sec("Overhead / Underfoot"),
        item("Dust", "Display range in overhead", "Tile distance in overhead text."),
        sec("Old Health Lines"),
        item("Dust", "Use old health lines", "Classic under-character HP line."),
        item(
            "Dust",
            "Mana/stamina underlines (self/party)",
            "Extra ticks under HP line.",
        ),
        item("Dust", "Bigger underlines", "Thicker underline graphic."),
        item(
            "Dust",
            "Underline transparency",
            "Slider 1–10 for self/party underline alpha.",
        ),
        sec("Misc"),
        item(
            "Dust",
            "Offscreen targeting (listed)",
            "Shown in UI; may have no effect (legacy).",
        ),
        item(
            "Dust",
            "Set target out of range (listed)",
            "Shown in UI; may have no effect (legacy).",
        ),
        item(
            "Dust",
            "Razor target → last target string",
            "Checkbox plus custom cliloc/text field.",
        ),
        item(
            "Dust",
            "Black outline statics",
            "High-contrast static outline (see wiki warnings).",
        ),
        item("Dust", "Ignore stamina check", "Client-side stamina bypass where applied."),
        item("Dust", "Block Wall of Stone", "Draw blocking helper for WoS."),
        item("Dust", "Block WoS Fel only", "Limit WoS block to Felucca."),
        item("Dust", "WoS art ID", "Numeric field for substitute art."),
        item("Dust", "Force WoS to pre-AoS art", "Art override flag."),
        item("Dust", "Block energy field", "Draw blocking helper for fields."),
        item("Dust", "Block energy field Fel only", "Fel-only for EF block."),
        item("Dust", "Energy field art ID", "Substitute art index."),
        item("Dust", "Force EF to pre-AoS art", "Art override flag."),
        sec("Misc2"),
        item("Dust", "Wireframe view", "Known broken in builds."),
        item("Dust", "Hue impassable tiles", "Tint blocked tiles; hue picker."),
        item(
            "Dust",
            "Transparent houses",
            "Checkbox + Z slider + transparency slider.",
        ),
        item("Dust", "Invisible houses", "Checkbox + Z slider."),
        item(
            "Dust",
            "Floor cutoff for invisible/transparent",
            "Do not hide below this Z.",
        ),
        item(
            "Dust",
            "Draw mobiles with surface overhead",
            "Layering tweak for surface text.",
        ),
        item(
            "Dust",
            "Ignorelist for circle of transparency",
            "Respect ignore entries in CoT.",
        ),
        item(
            "Dust",
            "Death marker on world map",
            "Shows death location ~5 minutes.",
        ),
        item(
            "Dust",
            "Auto avoid obstacles and mobiles",
            "Pathing assist around blockers.",
        ),
        item("Dust", "Force gargoyle walk", "Prefer walk over flight animation."),
        sec("STATUS GUMP"),
        item("Dust", "Razor Enhanced status gump", "RE-style stats layout."),
        sec("MISC3"),
        item("Dust", "Show all layers on mobiles", "Every equipment layer visible."),
        item("Dust", "Show all layers on paperdoll", "Full layer stack on doll."),
        item(
            "Dust",
            "Color paperdoll by durability",
            "Yellow/red slots when low durability.",
        ),
        item("Dust", "Paperdoll layers X offset", "Field; reopen paperdoll after change."),
        item("Dust", "Override container open range", "Extend how far you may open bags."),
        sec("Journal"),
        item("Dust", "Max journal entries", "Slider 200–2000 retained lines."),
        item("Dust", "Journal opacity", "Slider 0–100."),
        item("Dust", "Journal background hue", "Hue picker for journal chrome."),
        item("Dust", "Journal border style", "Combo from resizable journal styles."),
        item("Dust", "Hide journal borders", "Checkbox."),
        item("Dust", "Hide journal timestamp", "Checkbox."),
        sec("Nameplates"),
        item(
            "Dust",
            "Nameplates act as health bars",
            "Checkbox; HP bar opacity slider.",
        ),
        item(
            "Dust",
            "Hide nameplate at full HP",
            "Checkbox; warmode-only sub-option.",
        ),
        item("Dust", "Nameplate border opacity", "Slider."),
        item("Dust", "Nameplate background opacity", "Slider."),
        sec("Mobiles"),
        item("Dust", "Damage hue — self", "Overhead damage numbers."),
        item("Dust", "Damage hue — others", "Picker."),
        item("Dust", "Damage hue — pets", "Picker."),
        item("Dust", "Damage hue — allies", "Picker."),
        item("Dust", "Damage hue — last attacker", "Picker."),
        item("Dust", "Overhead text width", "Slider 100–600 wrap."),
        item("Dust", "Below-mobile health line scale", "Slider 1–5."),
        item(
            "Dust",
            "Open health bar for last attack",
            "Auto-open bar for last attacked mobile.",
        ),
        sec("Misc (extended)"),
        item("Dust", "Disable system chat", "Route system to journal only patterns."),
        item(
            "Dust",
            "Journal messages only in journal",
            "Keep certain lines out of overhead.",
        ),
        item("Dust", "Hidden body alpha", "Slider + hue for stealthed bodies."),
        item("Dust", "Visible player alpha", "Constant alpha while visible."),
        item("Dust", "Improved buff gump", "Checkbox + buff bar hue."),
        item("Dust", "Main game window background hue", "Modern color picker."),
        item(
            "Dust",
            "Health indicator border",
            "Checkbox; threshold %; width field.",
        ),
        item("Dust", "Spell icon scale", "Slider 50–300%."),
        item(
            "Dust",
            "Spell icon hotkey text",
            "Checkbox + hotkey text hue.",
        ),
        item(
            "Dust",
            "Alt + scroll gump opacity",
            "Adjust anchored gump alpha with Alt+wheel.",
        ),
        item("Dust", "Modern shop gump", "Alternate vendor UI."),
        item(
            "Dust",
            "Skill progress on change",
            "Checkbox + format string field.",
        ),
        item(
            "Dust",
            "Close anchored health bars with auto-close",
            "Tied to auto-close rules.",
        ),
        item("Dust", "Auto loot button", "Opens AutoLoot options gump."),
        item(
            "Dust",
            "Nearby item modal",
            "Checkbox + configurable hotkey for pickup helper.",
        ),
        item(
            "Dust",
            "Combat tracking",
            "Button opens combat tracking timeline gump.",
        ),
    ]
    Path("tools/wiki_dust765_fragment.html").write_text(
        page("wiki-opt-dust", "Dust (Options)", dust_intro, d)
        + page(
            "wiki-opt-765",
            "765 (Options)",
            "Dust765 <code>Build765()</code> (page 17). Bind macro names in Macros tab or use chat where noted.",
            [
                sec("Features Macros"),
                item(
                    "765",
                    "Macro: HighlightTileAtRange toggle",
                    "Toggles tile highlight from Dust tab.",
                ),
                item("765", "Macro: ToggleTransparentHouses", "Houses transparency on/off."),
                item("765", "Macro: ToggleInvisibleHouses", "House invisibility on/off."),
                item("765", "Macro: UCCLinesToggleLT", "UCC lines last-target channel."),
                item("765", "Macro: UCCLinesToggleHM", "UCC lines hunting mode."),
                item("765", "Macro: AutoMeditate", "Background meditate loop."),
                item("765", "Macro: Using AIBOT", "AI-bot flag toggle."),
                item("765", "Macro: ToggleECBuffGump", "EC-style buff gump."),
                item("765", "Macro: ToggleECDebuffGump", "EC-style debuff gump."),
                item("765", "Macro: ToggleECStateGump", "EC-style state gump."),
                item("765", "Macro: ToggleModernCooldownBar", "Modern cooldown bar."),
                sec("Simple Macros"),
                item(
                    "765",
                    "LastTargetRC + range slider",
                    "Last target with max tile range.",
                ),
                item("765", "ObjectInfo", "Object inspect macro (-info style)."),
                item("765", "HideX", "Client-hide land/static/item/mobile."),
                item("765", "HealOnHPChange", "Hold: heal when HP changes."),
                item("765", "HarmOnSwing", "Hold: harm on next swing anim."),
                item("765", "CureGH", "Cure if poisoned else Greater Heal."),
                item("765", "SetTargetClientSide", "Local last target only."),
                item("765", "OpenJournal2", "Second journal window."),
                item("765", "OpenBackpack2", "Second backpack (classic view)."),
                item("765", "OpenCorpses", "Open corpses 0x2006 within 2 tiles."),
                sec("Advanced Macros"),
                item(
                    "765",
                    "OpenCorpsesSafeLoot",
                    "Opens non-innocent corpses within 2 tiles.",
                ),
                item("765", "EquipManager", "Equip workflow macro."),
                item(
                    "765",
                    "SetMimic_PlayerSerial",
                    "Serial for mimic / defend flows.",
                ),
                item("765", "AutoPot", "Disarm/pot chain per UI description."),
                item("765", "DefendPartyKey", "Party defend logic macro."),
                item("765", "DefendSelfKey", "Self defend logic macro."),
                item("765", "CustomInterrupt", "Fast interrupt casting."),
                item(
                    "765",
                    "GrabFriendlyBars — drag coords",
                    "X Y start and FX FY dock for innocent bars.",
                ),
                item(
                    "765",
                    "GrabEnemyBars — drag coords",
                    "X Y and FX FY for criminal/enemy/murderer bars.",
                ),
                item(
                    "765",
                    "GrabPartyAllyBars — drag coords",
                    "X Y and FX FY for party/ally bars.",
                ),
                sec("Automations"),
                item("765", "Chat / macro -automed", "Background meditate."),
                item("765", "Chat / macro -aibot", "AI-bot toggle."),
                item("765", "Chat / macro -engange", "Pathfind engage last target."),
                sec("Misc4"),
                item("765", "Chat -mimic", "Harmful mimic with defend macros."),
                item("765", "Chat -marker X Y", "World map marker line."),
                item(
                    "765",
                    "Auto world-map marker",
                    "Checkbox for map gumps (e.g. treasure maps).",
                ),
                item("765", "Chat -df", "Reactive GH on big hits (see UI text)."),
                item("765", "Chat -autorange", "Weapon range rings; autorange.txt."),
                item("765", "Autorange always on", "Checkbox + hue picker."),
                sec("Lobby"),
                item(
                    "765",
                    "Lobby chat commands",
                    "-lobby help/status/connect/disconnect/target/cast/drop/attack; -autohid.",
                ),
                item("765", "Lobby IP field", "Default IP for LobbyConnect macro."),
                item("765", "Lobby Port field", "Default port."),
                item("765", "Lobby macros", "LobbyDisconnect, LobbyTarget, cast Lightning/EB, LobbyDrop."),
            ],
        )
        + page(
            "wiki-opt-mods",
            "Mods (Options)",
            "Dust765 <code>BuildMods()</code> (page 18). UCC UI suite.",
            [
                sec("UI GUMPS"),
                item("Mods", "UCC LastTarget bar", "Enable; double-click locks position."),
                item("Mods", "Bandage gump", "Show timer gump when bandaging."),
                item("Mods", "Bandage timer offset X / Y", "Pixel placement."),
                item("Mods", "Bandage count up / down", "Toggle count direction."),
                item("Mods", "OnCasting gump", "Anti-rubberband cursor helper."),
                item("Mods", "OnCasting hidden", "Hide the gump while active."),
                item("Mods", "Cast bar under player", "4px bar under character."),
                item("Mods", "Visual response manager", "Popup feedback manager."),
                sec("LINES UI"),
                item("Mods", "Enable UCC Lines", "Master lines overlay toggle."),
                sec("AUTOLOOT UI"),
                item("Mods", "Enable UCC AutoLoot", "Master auto-loot UI."),
                item("Mods", "Enable GridLootColoring", "Tint loot grid matches."),
                item("Mods", "Enable LootAboveID", "Target items above an ID."),
                sec("COOLDOWN UI"),
                item("Mods", "Enable UCC Buffbar", "Combat buff bar gump."),
                item("Mods", "Enable UCC Self", "Self-status bar gump."),
                item("Mods", "Show Swing Line", "Swing timing line."),
                item("Mods", "Show Do Disarm Line", "You disarmed someone."),
                item("Mods", "Show Got Disarmed Line", "You were disarmed."),
                item("Mods", "Lock buff/self bars", "Freeze gump position."),
                sec("BUFFBAR AND SELF SETTINGS"),
                item(
                    "Mods",
                    "Disarmed cooldown (general)",
                    "Milliseconds after disarm state.",
                ),
                item(
                    "Mods",
                    "Disarm strike cooldown",
                    "Ms after successful disarm.",
                ),
                item(
                    "Mods",
                    "Disarm attempt cooldown",
                    "Ms after failed disarm.",
                ),
                sec("SETTINGS (THRESHOLDS)"),
                item("Mods", "Bandage HP threshold", "diff hits ≥ value."),
                item("Mods", "Bandage when poisoned", "Checkbox."),
                item("Mods", "Cure pot HP threshold", "Field."),
                item("Mods", "Heal pot HP threshold", "Field."),
                item("Mods", "Refresh pot stamina threshold", "Field."),
                sec("SETTINGS (MISC)"),
                item(
                    "Mods",
                    "Auto rearm after disarm",
                    "Milliseconds before rearm.",
                ),
                item("Mods", "Cliloc triggers", "Use cliloc-based UCC triggers."),
                item("Mods", "Macro triggers", "Use macro-based UCC triggers."),
                item("Mods", "Strength pot cooldown", "Ms field."),
                item("Mods", "Agility pot cooldown", "Ms field."),
                item("Mods", "RNG min delay", "Ms humanization."),
                item("Mods", "RNG max delay", "Ms humanization."),
                sec("TABGRID"),
                item("Mods", "Enable TabGrid gump", "Master toggle."),
                item("Mods", "Grid rows", "Numeric field."),
                item("Mods", "Number of tabs", "Numeric field."),
                item("Mods", "Tab name list", "Text field with client format."),
            ],
        ),
        encoding="utf-8",
    )
    print("wrote tools/wiki_dust765_fragment.html")

    aux = (
        page(
            "wiki-nameplate-options",
            "Nameplate Options",
            "Options page 13 — <code>BuildNameOverhead()</code>. Pick a nameplate rule row, then configure.",
            [
                item(
                    "Nameplate Options",
                    "Nameplate row list",
                    "Left column: select which overhead name rule to edit.",
                ),
                item(
                    "Nameplate Options",
                    "Assign / editor panel",
                    "Right side: conditions, hues, and text for the selected row.",
                ),
                item(
                    "Nameplate Options",
                    "Per-option controls",
                    "Each field in the assign panel (visibility, color, etc.).",
                ),
            ],
        )
        + page(
            "wiki-cooldowns",
            "Cooldowns",
            "Sidebar <code>BuildCooldowns()</code>.",
            [
                item("Cooldowns", "Bar position X / Y", "Numeric placement."),
                item(
                    "Cooldowns",
                    "Use last moved bar position",
                    "Prefer dragged position over fields.",
                ),
                item("Cooldowns", "+ Condition", "Add a new cooldown condition row."),
                item(
                    "Cooldowns",
                    "Condition row editor",
                    "Each row’s rules and visuals (expand per slot in client).",
                ),
            ],
        )
        + page(
            "wiki-grid-container",
            "Grid Container",
            "Sidebar <code>BuildGridContainer()</code>.",
            [
                item("Grid Container", "Use grid containers", "Enable grid layout gumps."),
                item("Grid Container", "Grid container scale", "Slider 50–200%."),
                item("Grid Container", "Also scale items", "Scale art inside cells."),
                item("Grid Container", "Border opacity", "Slider."),
                item("Grid Container", "Border hue", "Color picker."),
                item("Grid Container", "Background opacity", "Slider."),
                item("Grid Container", "Background hue", "Color picker."),
                item(
                    "Grid Container",
                    "Override hue with container hue",
                    "Use server container hue.",
                ),
                item(
                    "Grid Container",
                    "Search style",
                    "Only show vs Highlight matching items.",
                ),
                item(
                    "Grid Container",
                    "Enable container preview",
                    "Hover preview for known containers.",
                ),
                item("Grid Container", "Make anchorable", "Join anchor chains."),
                item(
                    "Grid Container",
                    "Container style",
                    "BorderStyle enum preset.",
                ),
                item("Grid Container", "Hide border around gump", "Checkbox."),
                item(
                    "Grid Container",
                    "Default rows × columns",
                    "Two numeric fields.",
                ),
                item(
                    "Grid Container",
                    "Grid highlight settings button",
                    "Opens GridHightlightMenu gump (client spelling).",
                ),
                item(
                    "Grid Container",
                    "Grid highlight line size",
                    "Slider 1–10.",
                ),
            ],
        )
        + page(
            "wiki-profiles",
            "Profiles",
            "Sidebar <code>BuildProfiles()</code>.",
            [
                item(
                    "Profiles",
                    "Profile description / selector",
                    "Active profile and notes (as shown in client).",
                ),
                item(
                    "Profiles",
                    "Override ALL other profiles",
                    "Copies settings to every profile file.",
                ),
                item(
                    "Profiles",
                    "Override profiles on same server",
                    "Copies only to profiles matching current server.",
                ),
            ],
        )
    )
    Path("tools/wiki_aux_fragment.html").write_text(aux, encoding="utf-8")
    print("wrote tools/wiki_aux_fragment.html")


if __name__ == "__main__":
    main()
